import { translations } from './content.js';

class Portal {
  constructor() {
    this.lang = 'zh';
    this.init();
  }

  init() {
    this.render();
    this.setupEventListeners();
  }

  setupEventListeners() {
    document.getElementById('langSwitch').addEventListener('click', () => {
      this.lang = this.lang === 'zh' ? 'en' : 'zh';
      this.render();
    });
  }

  render() {
    const t = translations[this.lang];

    // Header & Status
    document.getElementById('brand').textContent = t.brand;
    document.getElementById('sys-status').textContent = t.status;

    // Navigation
    const navItems = document.querySelectorAll('.nav-link');
    t.nav.forEach((name, i) => {
      if (navItems[i]) navItems[i].textContent = name;
    });

    // Hero
    document.getElementById('hero-title').textContent = t.hero.title;
    document.getElementById('hero-subtitle').textContent = t.hero.subtitle;
    document.getElementById('hero-desc').textContent = t.hero.desc;

    // Stats
    const statsGrid = document.getElementById('stats-grid');
    statsGrid.innerHTML = t.stats.map(s => `
      <div class="tech-border p-4 bg-tech-surface/50 instrument-glow">
        <div class="text-3xl font-mono font-bold text-laser-blue">${s.value}</div>
        <div class="text-[10px] uppercase tracking-widest text-gray-500 mt-1">${s.label}</div>
        <div class="text-[9px] text-machine-grey mt-0.5">${s.unit}</div>
      </div>
    `).join('');

    // Engines
    document.getElementById('engine-title').textContent = t.engines.title;

    document.getElementById('google-engine').innerHTML = `
      <div class="text-sm font-bold text-laser-blue mb-2">${t.engines.google.name}</div>
      <div class="flex flex-wrap gap-2">
        ${t.engines.google.tags.map(tag => `<span class="px-2 py-0.5 bg-laser-blue/10 border border-laser-blue/30 text-[9px] text-laser-blue uppercase">${tag}</span>`).join('')}
      </div>
    `;

    document.getElementById('domestic-engine').innerHTML = `
      <div class="text-sm font-bold text-signal-orange mb-2">${t.engines.domestic.name}</div>
      <div class="flex flex-wrap gap-2">
        ${t.engines.domestic.tags.map(tag => `<span class="px-2 py-0.5 bg-signal-orange/10 border border-signal-orange/30 text-[9px] text-signal-orange uppercase">${tag}</span>`).join('')}
      </div>
    `;

    // Projects
    document.getElementById('projects-title').textContent = t.projects.title;
    const projectGrid = document.getElementById('project-grid');
    projectGrid.innerHTML = t.projects.items.map(p => `
      <div class="tech-border p-6 bg-tech-surface/40 hover:bg-tech-surface/80 transition-all group">
        <div class="text-[9px] font-mono text-laser-blue/60 mb-2 tracking-tighter">${p.tech}</div>
        <h4 class="text-base font-bold text-white mb-2 group-hover:text-laser-blue transition-colors">${p.name}</h4>
        <p class="text-xs text-gray-500 leading-relaxed">${p.desc}</p>
      </div>
    `).join('');

    // Philosophy
    document.getElementById('philosophy-title').textContent = t.philosophy.title;
    document.getElementById('philosophy-content').textContent = t.philosophy.content;

    // Footer
    document.getElementById('footer-text').textContent = t.footer;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new Portal();
});
