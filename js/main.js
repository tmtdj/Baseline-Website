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

// ═══ Hero figure rotation ═══
(function(){
  const imgs = document.querySelectorAll('#heroModel img');
  const glowEl = document.getElementById('heroGlow');
  const catGlows = {
    mobility:'radial-gradient(circle,rgba(48,209,88,.25),transparent)',
    bodyweight:'radial-gradient(circle,rgba(255,111,44,.25),transparent)',
    breathwork:'radial-gradient(circle,rgba(99,102,241,.25),transparent)'
  };
  let current = 0;
  function next(){
    imgs[current].classList.remove('active');
    current = (current + 1) % imgs.length;
    const img = imgs[current];
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
