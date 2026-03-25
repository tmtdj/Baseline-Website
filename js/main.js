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
  var cellSize = 32, gap = 4, duration = 5, maxCells = 600;
  var glowDiv = document.createElement('div');
  glowDiv.className = 'data-grid-glow';
  el.appendChild(glowDiv);

  function build(){
    Array.from(el.querySelectorAll('.grid-cell')).forEach(function(c){c.remove()});
    var w = el.offsetWidth, h = el.offsetHeight;
    if (!w || !h) return;
    var cols = Math.floor(w / (cellSize + gap));
    var rows = Math.floor(h / (cellSize + gap));
    while (rows * cols > maxCells) { rows > cols ? rows-- : cols--; }
    el.style.gridTemplateColumns = 'repeat(' + cols + ',1fr)';
    el.style.gridTemplateRows = 'repeat(' + rows + ',1fr)';
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
      if (!reducedMotion){
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
        if (entry.target.id === 'gridVideo') entry.target.play();
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



// ═══ Breathing orb label ═══
const orbLabel = document.getElementById('orbLabel');
let orbVisible = false;
const orbObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !orbVisible) {
      orbVisible = true;
      let breathCount = 0;
      const cycle = () => {
        orbLabel.style.opacity = '1';
        orbLabel.textContent = 'Breathe in...';
        setTimeout(() => { orbLabel.textContent = 'Breathe out...'; }, 4000);
        setTimeout(() => {
          breathCount++;
          if (breathCount >= 2) {
            orbLabel.textContent = 'You just did your first Shift.';
            setTimeout(() => { orbLabel.style.opacity = '.5'; }, 3000);
          } else { cycle(); }
        }, 8000);
      };
      setTimeout(cycle, 500);
    }
  });
}, { threshold: .5 });
orbObs.observe(document.getElementById('orbWrap'));
