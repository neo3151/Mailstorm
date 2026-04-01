import './style.css'

const app = document.querySelector('#app')

const EPISODE_DATA = {
  1: {
    title: "EP.01 — THE SHADOW DAY",
    endLine: "THE SHADOW DAY IS NEVER OVER",
    endSub: "THE CYCLE CONTINUES",
    pdfFile: "Mailstorm_Ep1_Abyssal_Edition.pdf",
    panels: [
      "01_cover.jpg","05_monolith.jpg","06_kips_hands.jpg","07_doors.jpg",
      "08_pit.jpg","09_stan.jpg","10_strike.jpg","11_severance.jpg",
      "12_chuck.jpg","13_mdd.jpg","14_crush.jpg","15_nixie.jpg",
      "16_pre_strike.jpg","17_climax.jpg","18_aftermath.jpg",
      "20_dossier_kip.jpg","22_blueprint.jpg",
    ]
  },
  2: {
    title: "EP.02 — TABLE 2 BLOODLINE",
    endLine: "THE TABLE 2 CURSE NEVER STOPS",
    endSub: "AMAZON SUNDAY APPROACHES",
    pdfFile: "Mailstorm_Ep2_Abyssal_Edition.pdf",
    panels: [
      "01_cover.jpg","02_assignment.jpg","03_shadow_grin.jpg",
      "04_llv_depart.jpg","05_bone_burn.jpg","06_xray.jpg",
      "07_satchel.jpg","08_swarm.jpg","09_heather.jpg",
      "10_aegis.jpg","11_shatter.jpg","12_awe.jpg",
      "13_sunset.jpg","14_hands.jpg","15_resolution.jpg",
    ]
  },
  3: {
    title: "EP.03 — THE PIVOT DIMENSION",
    endLine: "THE PIVOT DIMENSION COLLAPSES",
    endSub: "BUT THE AUDIT LOOMS",
    pdfFile: "",
    panels: [
      "01_ziggurat.jpg",
      "02_foreign_soil.jpg",
      "03_porch_trap.jpg",
      "04_apathy.jpg",
      "05_dlo.jpg"
    ]
  },
  4: {
    title: "EP.04 — THE CBA SHIELD",
    endLine: "GRIEVANCE MANA ACQUIRED",
    endSub: "THE ALGORITHM CAN BE FOUGHT",
    pdfFile: "",
    panels: [
      "01_snare.jpg",
      "02_interrogation.jpg",
      "03_summon.jpg",
      "04_cathedral.jpg",
      "05_spite.jpg"
    ]
  },
  5: {
    title: "EP.05 — DEAD LETTER DEEP-DIVE",
    endLine: "THE SOLIDARITY MANDATE UNLOCKED",
    endSub: "DESTINATION SET: THE CORE",
    pdfFile: "",
    panels: [
      "01_descent.jpg",
      "02_swarm.jpg",
      "03_heather.jpg",
      "04_override.jpg",
      "05_coordinates.jpg"
    ]
  }
}

const SPECIAL_DATA = {
  1: {
    title: "SP.01 — ENLIST IN THE OIG",
    endLine: "WELCOME TO MANAGEMENT",
    endSub: "PLEASE DO NOT RESIST THE PARASITE",
    pdfFile: null,
    panels: [
      "01_promise.jpg",
      "02_promotion.jpg",
      "03_host.jpg",
      "04_digestion.jpg",
      "05_parasite.jpg"
    ]
  },
  2: {
    title: "SP.02 — PRIME DAY MASSACRE",
    endLine: "THE ROUTE REMAINS OPEN",
    endSub: "THE CARNAGE CONTINUES TUESDAY",
    pdfFile: null,
    panels: [
      "01_swarm.jpg",
      "02_breach.jpg",
      "03_dogspray.jpg",
      "04_tubshield.jpg",
      "05_survivor.jpg"
    ]
  }
}

const state = {
  view: 'home',
  currentEp: null,
  currentSpecial: null,
  episodes: [
    { id: 1, title: "EP.01 — THE SHADOW DAY", available: true },
    { id: 2, title: "EP.02 — TABLE 2 BLOODLINE", available: true },
    { id: 3, title: "EP.03 — THE PIVOT DIMENSION", available: true },
    { id: 4, title: "EP.04 — THE CBA SHIELD", available: true },
    { id: 5, title: "EP.05 — DEAD LETTER DEEP-DIVE", available: true },
  ],
  specials: [
    { id: 1, title: "SP.01 — ENLIST IN THE OIG", available: true },
    { id: 2, title: "SP.02 — PRIME DAY MASSACRE", available: true },
    { id: 3, title: "SP.03 — THE POSTMASTER'S GALA", available: false }
  ]
}

function render() {
  app.innerHTML = ''
  if (state.view === 'home') renderHome()
  else if (state.view === 'reader') renderReader()
}

function renderHome() {
  const el = document.createElement('div')
  el.className = 'home-container'
  el.innerHTML = `
    <h1 class="home-title">MAILSTORM</h1>
    <p class="home-subtitle">THE CORPORATE BATTLE MANGA</p>
    <p class="home-tagline">
      In a world where corporate stress is a literal, soul-crushing magical force.
      Join <strong>Kip Baxter</strong> and <strong>Stan</strong> as they fight to survive
      the Table 2 Curse and the Algorithm's Gaze.
    </p>
    <div class="episode-grid">
      ${state.episodes.map(ep => `
        <button class="ep-btn ${ep.available ? '' : 'locked'}"
          onclick="${ep.available ? `window.__read(${ep.id})` : ''}"
          ${ep.available ? '' : 'disabled'}>
          ${ep.title}${ep.available ? '' : ' — ARCHIVE SEALED'}
        </button>
      `).join('')}
    </div>

    <h2 style="color:var(--accent-magenta, #ff00ff); text-align:center; font-family:'Bangers'; margin-top:2rem; letter-spacing: 2px;">[ SPECIAL ARCHIVES ]</h2>
    <div class="episode-grid" style="margin-top: 1rem;">
      ${state.specials.map(sp => `
        <button class="ep-btn ${sp.available ? '' : 'locked'}" style="border-color: ${sp.available ? '#ff00ff' : '#333'}; color: ${sp.available ? '#ff00ff' : '#888'};"
          onclick="${sp.available ? `window.__readSpecial(${sp.id})` : ''}"
          ${sp.available ? '' : 'disabled'}>
          ${sp.title}${sp.available ? '' : ' — UNAUTHORIZED'}
        </button>
      `).join('')}
    </div>

    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-top:2rem;margin-bottom:1rem;">
      <button class="download-btn" onclick="window.__showFactions()" style="border-color: #555;">[ ACTIVE GUILDS ]</button>
      <button class="download-btn" onclick="window.__showRoadmap()" style="border-color: #555;">[ PROJECT ROADMAP ]</button>
    </div>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/encyclopedia.html" class="download-btn" target="_blank" style="border-color: var(--accent-hazard); color: var(--accent-hazard);">
        ⚲ READ LORE ENCYCLOPEDIA
      </a>
      <a href="/downloads/Mailstorm_Vol1_Storybook.pdf" class="download-btn" download style="border-color: #d4d0c8; color: #111; background-color: #d4d0c8; font-weight: bold; padding: 0.5rem 2rem;">
        [ ↓ DOWNLOAD VOL. 1 STORYBOOK (EPS 1-5) ]
      </a>
    </div>
  `
  app.appendChild(el)
  window.__read = (id) => { state.currentEp = id; state.currentSpecial = null; state.view = 'reader'; render() }
  window.__readSpecial = (id) => { state.currentSpecial = id; state.currentEp = null; state.view = 'reader'; render() }
}

function renderReader() {
  const isSpecial = state.currentSpecial !== null
  const epData = isSpecial ? SPECIAL_DATA[state.currentSpecial] : EPISODE_DATA[state.currentEp]
  if (!epData) return
  const folder = isSpecial ? `specials/sp${state.currentSpecial}` : `episode_${state.currentEp}`
  const accentColor = isSpecial ? '#ff00ff' : 'var(--accent-orange)'
  const el = document.createElement('div')

  const header = document.createElement('div')
  header.className = 'reader-header'
  header.innerHTML = `
    <button id="back-btn" style="color: ${accentColor}; border-color: ${accentColor};">← RETURN TO PORTAL</button>
    <span class="reader-title" style="color: ${accentColor};">${epData.title}</span>
    <div style="width:100px"></div>
  `
  el.appendChild(header)

  const panelsEl = document.createElement('div')
  panelsEl.className = 'reader-panels'
  epData.panels.forEach(file => {
    const wrapper = document.createElement('div')
    wrapper.className = 'panel-wrapper'
    const img = document.createElement('img')
    img.src = `/comics/${folder}/${file}`
    img.alt = file.replace('.jpg','').replace(/_/g,' ')
    img.loading = 'lazy'
    img.onload = () => img.classList.add('loaded')
    wrapper.appendChild(img)
    panelsEl.appendChild(wrapper)
  })
  el.appendChild(panelsEl)

  const end = document.createElement('div')
  end.className = 'reader-end'
  end.innerHTML = `
    <h2 style="color: ${accentColor}; border-bottom: 2px solid ${accentColor}; padding-bottom: 1rem;">${epData.endLine}</h2>
    <p>${epData.endSub}</p>
    <div style="display:flex;gap:1rem;justify-content:center;margin-top:2rem">
      ${epData.pdfFile ? `
      <a href="/comics/${folder}/${epData.pdfFile}" class="download-btn" download style="color: ${accentColor}; border-color: ${accentColor};">
        ↓ DOWNLOAD PDF
      </a>
      ` : ''}
      <button class="download-btn" onclick="window.__home()" style="color: ${accentColor}; border-color: ${accentColor};">← RETURN TO PORTAL</button>
    </div>
  `
  el.appendChild(end)

  app.appendChild(el)
  document.getElementById('back-btn').addEventListener('click', () => {
    state.view = 'home'; render()
  })
  window.__home = () => { state.view = 'home'; render() }
}

window.__closeModal = () => {
  document.getElementById('modal-container').innerHTML = '';
}

window.__showFactions = () => {
  const modal = document.getElementById('modal-container');
  modal.innerHTML = `
    <div style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.9);z-index:9999;display:flex;align-items:center;justify-content:center;padding:2rem;">
      <div style="background:#111;border:2px solid var(--accent-hazard);padding:2rem;max-width:800px;width:100%;max-height:80vh;overflow-y:auto;position:relative;">
        <button onclick="window.__closeModal()" style="position:absolute;top:10px;right:10px;background:none;border:none;color:#fff;font-size:1.5rem;cursor:pointer;">X</button>
        <h2 style="color:var(--accent-hazard);font-family:'Bangers';margin-top:0;">THE POSTAL GUILDS</h2>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1rem;">
          <div style="border:1px solid #333;padding:1rem;">
            <h3 style="color:#FFF;">NALC: City Carriers</h3>
            <p style="color:#888;font-size:0.9rem;"><strong>Class:</strong> Paladins / Tanks<br><strong>Mechanic:</strong> The Grievance Engine<br><strong>Armor:</strong> Blue/Grey Uniform Plate</p>
          </div>
          <div style="border:1px solid #333;padding:1rem;">
            <h3 style="color:#FFF;">APWU: The Clerks</h3>
            <p style="color:#888;font-size:0.9rem;"><strong>Class:</strong> Artificers / Support<br><strong>Mechanic:</strong> Machine Communion<br><strong>Armor:</strong> Total Apathy</p>
          </div>
          <div style="border:1px solid #333;padding:1rem;">
            <h3 style="color:#FFF;">NRLCA: Rural Carriers</h3>
            <p style="color:#888;font-size:0.9rem;"><strong>Class:</strong> Berserkers / Rangers<br><strong>Mechanic:</strong> Evaluation Blitz<br><strong>Armor:</strong> Personal Vehicle Shell</p>
          </div>
          <div style="border:1px solid #333;padding:1rem;">
            <h3 style="color:#FFF;">NPMHU: Mail Handlers</h3>
            <p style="color:#888;font-size:0.9rem;"><strong>Class:</strong> Heavy Infantry<br><strong>Mechanic:</strong> The Dock Slam<br><strong>Armor:</strong> Steel-Toe Wards</p>
          </div>
        </div>
      </div>
    </div>
  `;
}

window.__showRoadmap = async () => {
  const modal = document.getElementById('modal-container');
  const graphDef = `
flowchart TD
    classDef completed fill:#ff4f00,stroke:#000000,stroke-width:2px,color:#0a0a0a;
    classDef pending fill:#111111,stroke:#555555,stroke-width:2px,color:#888888;
    classDef threat fill:#0a0a0a,stroke:#c8a200,stroke-width:3px,color:#c8a200;
    classDef special fill:#2e0029,stroke:#ff00ff,stroke-width:3px,color:#ff00ff,font-weight:bold;
    Phase1[COMPLETED ARCHIVES]:::completed --> Phase2[COMPLETED DIRECTIVES]:::completed
    Phase2 --> Phase3[SYSTEM OVERRIDE: EP.10 CLIMAX]:::threat
    Phase1 --> E1("EP.1: 8 and Skate"):::completed
    Phase1 --> E2("EP.2: Table 2 Relic"):::completed
    Phase1 --> E3("EP.3: The Pivot Dimension"):::completed
    Phase2 --> E4("EP.4: The CBA Shield"):::completed
    Phase2 --> E5("EP.5: Dead Letter Void"):::completed
    E5 --> E6("EP.6: The Rural Frontier"):::pending
    E6 --> E7("EP.7: The 204b Parasite"):::pending
    E7 --> E8("EP.8: The Iron Lifters"):::pending
    E8 --> E9("EP.9: The All-Call Blizzard"):::pending
    E9 --> E10("EP.10: The Solidarity Mandate"):::threat
    
    E3 -.->|Sidequest| SP1("SP.01: Enlist in the OIG"):::special
    E6 -.->|Sidequest| SP2("SP.02: Prime Day Massacre"):::special
    E9 -.->|Sidequest| SP3("SP.03: The Postmaster's Gala"):::special
  `;
  
  modal.innerHTML = `
    <div style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.9);z-index:9999;display:flex;align-items:center;justify-content:center;padding:2rem;">
      <div style="background:#111;border:2px solid var(--accent-hazard);padding:2rem;max-width:800px;width:100%;max-height:80vh;overflow-y:auto;position:relative;text-align:center;">
        <button onclick="window.__closeModal()" style="position:absolute;top:10px;right:10px;background:none;border:none;color:#fff;font-size:1.5rem;cursor:pointer;">X</button>
        <h2 style="color:var(--accent-hazard);font-family:'Bangers';margin-top:0;">MASTER ROADMAP</h2>
        <div id="roadmap-mermaid" style="color:#d4d0c8;">Synthesizing Architecture...</div>
      </div>
    </div>
  `;
  
  try { 
      const mermaidModule = await import('https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs');
      const mermaid = mermaidModule.default;
      mermaid.initialize({ startOnLoad: false, theme: 'dark', fontFamily: 'Roboto Condensed' });
      const { svg } = await mermaid.render('roadmap-svg-generated', graphDef);
      document.getElementById('roadmap-mermaid').innerHTML = svg;
  } 
  catch(e) { 
      console.error("Mermaid render error: ", e); 
      document.getElementById('roadmap-mermaid').innerHTML = "<pre style='text-align:left; font-size: 14px;'>" + graphDef + "</pre>";
  }
}

document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('ambient-toggle');
    const audio = document.getElementById('ambient-audio');
    if(toggle && audio) {
        toggle.addEventListener('change', (e) => {
            if(e.target.checked) audio.play();
            else audio.pause();
        });
    }
});

render()
