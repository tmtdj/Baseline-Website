// ═══ Bottom bar: show after scrolling past hero email form ═══
(function(){
  const bar = document.querySelector('.bottom-bar');
  const notify = document.getElementById('notify');
  if (!bar || !notify) return;
  const obs = new IntersectionObserver(([e]) => {
    bar.classList.toggle('visible', !e.isIntersecting);
  }, {threshold:0});
  obs.observe(notify);
})();

// ═══ Mobile nav toggle ═══
(function(){
  const burger = document.getElementById('navBurger');
  const nav = document.getElementById('mobileNav');
  if (!burger || !nav) return;
  burger.addEventListener('click', () => {
    burger.classList.toggle('open');
    nav.classList.toggle('open');
  });
  nav.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      burger.classList.remove('open');
      nav.classList.remove('open');
    });
  });
})();

// ═══ DataGrid Hero ═══
(function(){
  var el = document.getElementById('dataGridHero');
  if (!el) return;
  var colors = ['var(--green)','var(--tangerine)','var(--ice)','var(--solar)','var(--lavender)','var(--indigo)','var(--accent)'];
  var gap = 4, duration = 5, maxCells = 800;
  var glowDiv = document.createElement('div');
  glowDiv.className = 'data-grid-glow';
  el.appendChild(glowDiv);

  function build(){
    Array.from(el.querySelectorAll('.grid-cell')).forEach(function(c){c.remove()});
    var w = el.offsetWidth, h = el.offsetHeight;
    if (!w || !h) return;
    // Scale cell size: smaller on wider screens so grid stays dense
    var cellSize = w > 1200 ? 28 : w > 768 ? 32 : 36;
    var cols = Math.floor(w / (cellSize + gap));
    var rows = Math.floor(h / (cellSize + gap));
    while (rows * cols > maxCells) { rows > cols ? rows-- : cols--; }
    el.style.gridTemplateColumns = 'repeat(' + cols + ',1fr)';
    el.style.gridTemplateRows = 'repeat(' + rows + ',1fr)';
    el.style.justifyContent = 'stretch';
    el.style.alignContent = 'stretch';
    el.style.gap = gap + 'px';
    var centerR = Math.floor(rows / 2), centerC = Math.floor(cols / 2);
    var frag = document.createDocumentFragment();
    var reducedMotion = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
    for (var i = 0; i < rows * cols; i++){
      var cell = document.createElement('div');
      cell.className = 'grid-cell';
      cell.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
      cell.style.setProperty('--opacity-min','0.04');
      cell.style.setProperty('--opacity-max','0.20');
      if (!reducedMotion && Math.random() < 0.4){
        var r = Math.floor(i / cols), c = i % cols;
        var dr = Math.abs(r - centerR), dc = Math.abs(c - centerC);
        cell.style.animation = 'cell-pulse ' + duration + 's infinite alternate';
        cell.style.animationDelay = (Math.sqrt(dr*dr+dc*dc)*0.15).toFixed(2) + 's';
      }
      frag.appendChild(cell);
    }
    el.appendChild(frag);
  }
  build();

  // rebuild on resize (debounced)
  var resizeTimer;
  new ResizeObserver(function(){
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(build, 200);
  }).observe(el);

  // mouse glow (desktop only)
  if (!('ontouchstart' in window)){
    el.classList.add('has-glow');
    el.addEventListener('mousemove', function(e){
      var rect = el.getBoundingClientRect();
      el.style.setProperty('--mx', (e.clientX - rect.left) + 'px');
      el.style.setProperty('--my', (e.clientY - rect.top) + 'px');
    });
  }
})();

// ═══ Hero figure rotation ═══
(function(){
  var imgs = document.querySelectorAll('#heroModel img');
  var glowEl = document.getElementById('heroGlow');
  var catGlows = {
    mobility:'radial-gradient(circle,rgba(48,209,88,.25),transparent)',
    bodyweight:'radial-gradient(circle,rgba(255,111,44,.25),transparent)',
    breathwork:'radial-gradient(circle,rgba(99,102,241,.25),transparent)'
  };
  var current = 0;
  function next(){
    imgs[current].classList.remove('active');
    current = (current + 1) % imgs.length;
    var img = imgs[current];
    img.classList.add('active');
    glowEl.style.background = catGlows[img.dataset.cat];
  }
  setInterval(next, 3500);
})();

// ═══ Scroll reveal ═══
const revealObs = new IntersectionObserver(entries => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('visible');
        if (entry.target.id === 'blockGrid') animateBlockGrid();
      }, i * 50);
      revealObs.unobserve(entry.target);
    }
  });
}, { threshold: .15, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));

// ═══ Dose card fills ═══
const doseObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.dose-row-fill').forEach((fill, i) => {
        setTimeout(() => { fill.style.width = fill.dataset.w; }, 300 + i * 200);
      });
      doseObs.unobserve(entry.target);
    }
  });
}, { threshold: .3 });
doseObs.observe(document.getElementById('doseCard'));



// ═══ Block grid animation ═══
(function(){
  var grid = document.getElementById('blockGrid');
  if (!grid) return;
  var COLS = 7, ROWS = 5;
  // Row colors bottom-to-top: green, green, tangerine, ice, indigo
  var rowColors = [
    {bg:'var(--indigo)', glow:'rgba(99,102,241,.4)'},
    {bg:'var(--ice)', glow:'rgba(103,232,249,.4)'},
    {bg:'var(--tangerine)', glow:'rgba(255,111,44,.4)'},
    {bg:'var(--green)', glow:'rgba(48,209,88,.4)'},
    {bg:'var(--green)', glow:'rgba(48,209,88,.4)'}
  ];
  // Fill pattern from the video: how many cells filled per row (bottom-to-top)
  // fillCounts[0]=bottom row .. fillCounts[4]=top row
  // All rows complete except top row (week in progress)
  var fillCounts = [7, 7, 7, 7, 3];
  var cells = [];
  for (var r = 0; r < ROWS; r++){
    for (var c = 0; c < COLS; c++){
      var cell = document.createElement('div');
      cell.className = 'block-cell empty';
      var color = rowColors[r];
      cell.dataset.row = r;
      cell.dataset.col = c;
      cell.dataset.bg = color.bg;
      cell.dataset.glow = color.glow;
      cell.style.setProperty('--cell-glow', color.glow);
      grid.appendChild(cell);
      cells.push(cell);
    }
  }
  window.animateBlockGrid = function(){
    var delay = 0;
    for (var r = ROWS - 1; r >= 0; r--){
      var count = fillCounts[ROWS - 1 - r];
      for (var c = 0; c < count; c++){
        (function(row, col, d){
          setTimeout(function(){
            var cell = cells[row * COLS + col];
            cell.style.backgroundColor = cell.dataset.bg;
            cell.style.transform = 'scale(1.1)';
            cell.style.boxShadow = '0 0 12px ' + cell.dataset.glow;
            setTimeout(function(){ cell.style.transform = 'scale(1)'; }, 150);
          }, d);
        })(r, c, delay);
        delay += 80;
      }
    }
  };
})();

// ═══ Breathing orb label ═══
const orbLabel = document.getElementById('orbLabel');
let orbVisible = false;
const orbObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !orbVisible) {
      orbVisible = true;
    }
  });
}, { threshold: .5 });
orbObs.observe(document.getElementById('orbWrap'));

// ═══ Position orb glow on the shift-orb-block center ═══
function positionOrb() {
  const block = document.querySelector('.shift-orb-block');
  const section = document.querySelector('.shift-section');
  const wrap = document.getElementById('orbWrap');
  if (!block || !section || !wrap) return;
  // Use offsetTop/offsetLeft to avoid animation transform skewing the position
  let top = 0, left = 0, el = block;
  while (el && el !== section) { top += el.offsetTop; left += el.offsetLeft; el = el.offsetParent; }
  wrap.style.top = (top + block.offsetHeight / 2) + 'px';
  wrap.style.left = (left + block.offsetWidth / 2) + 'px';
}
positionOrb();
window.addEventListener('resize', positionOrb);

// ═══ Orb color rotation: indigo → solar → ice → lavender ═══
(function() {
  const orbColors = [
    { r: 99, g: 102, b: 241 },  // indigo
    { r: 234, g: 179, b: 8 },   // solar
    { r: 103, g: 232, b: 249 }, // ice
    { r: 167, g: 139, b: 250 }  // lavender
  ];
  const orbBg = document.querySelector('.shift-orb-bg');
  const orbBlock = document.querySelector('.shift-orb-block');
  if (!orbBg || !orbBlock) return;
  const orbInner = document.querySelector('.shift-orb-inner');
  if (!orbInner) return;
  let idx = 0;
  function setOrbColor(c) {
    orbBg.style.setProperty('--orb-r', c.r);
    orbBg.style.setProperty('--orb-g', c.g);
    orbBg.style.setProperty('--orb-b', c.b);
    orbBlock.style.background = `rgba(${c.r},${c.g},${c.b},.3)`;
    orbBlock.style.borderColor = `rgba(${c.r},${c.g},${c.b},.55)`;
  }
  // Change color when the breath completes (at the smallest/quietest point)
  orbInner.addEventListener('animationiteration', function() {
    idx = (idx + 1) % orbColors.length;
    setOrbColor(orbColors[idx]);
  });
})();

// ═══ Screenshots carousel dots ═══
(function(){
  var track = document.getElementById('screenshotsTrack');
  var dots = document.querySelectorAll('#screenshotsDots .dot');
  if (!track || !dots.length) return;
  var cards = track.querySelectorAll('.screenshot-card');
  var scrollObs = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if (entry.isIntersecting) {
        var i = parseInt(entry.target.dataset.index);
        dots.forEach(function(d){ d.classList.remove('active'); });
        if (dots[i]) dots[i].classList.add('active');
      }
    });
  }, {root: track, threshold: 0.6});
  cards.forEach(function(card){ scrollObs.observe(card); });
  dots.forEach(function(dot){
    dot.addEventListener('click', function(){
      var i = parseInt(dot.dataset.index);
      if (cards[i]) cards[i].scrollIntoView({behavior:'smooth', inline:'center', block:'nearest'});
    });
  });
})();
