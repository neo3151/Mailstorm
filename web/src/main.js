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
  },
  6: {
    title: "EP.06 — THE RURAL FRONTIER",
    endLine: "THE EVALUATION ZONE BREACHED",
    endSub: "NRLCA TACTICS UNLOCKED",
    pdfFile: "",
    panels: [
      "01_edge.jpg",
      "02_ranger.jpg",
      "03_sentinel.jpg",
      "04_blitz.jpg",
      "05_truce.jpg"
    ]
  },
  7: {
    title: "EP.07 — THE 204B PARASITE",
    endLine: "THE SUPERVISOR'S METRICS WERE SHATTERED",
    endSub: "THE FILIBUSTER HOLDS",
    pdfFile: "Mailstorm_Ep7_Abyssal_Edition.pdf",
    panels: [
      "01_incubation.jpg",
      "02_host_chosen.jpg",
      "03_guest_star.jpg",
      "04_metric_assault.jpg",
      "05_aftermath.jpg"
    ]
  },
  8: {
    title: "EP.08 — THE IRON LIFTERS",
    endLine: "THE DOCK SLAM SEALS THE BREACH",
    endSub: "THE IRON LIFTERS HOLD THE LINE",
    pdfFile: "Mailstorm_Ep8_Abyssal_Edition.pdf",
    panels: [
      "01_prime_tsunami.jpg",
      "02_joust.jpg",
      "03_bombardment.jpg",
      "04_drift.jpg",
      "05_dock_slam.jpg"
    ]
  },
  9: {
    title: "EP.09 — THE ALL-CALL BLIZZARD",
    endLine: "FOUR FACTIONS UNITED BENEATH THE STORM",
    endSub: "THE SOLIDARITY MANDATE HAS BEEN AWAKENED",
    pdfFile: "Mailstorm_Ep9_Abyssal_Edition.pdf",
    panels: [
      "01_blizzard.jpg",
      "02_iron_lifter_breach.jpg",
      "03_clerk_furnace.jpg",
      "04_rural_convoy.jpg",
      "05_paladin_march.jpg"
    ]
  },
  10: {
    title: "EP.10 — THE SOLIDARITY MANDATE",
    endLine: "THE ALGORITHM IS SEVERED",
    endSub: "SEASON ONE CONCLUDED",
    pdfFile: "Mailstorm_Season_1_Finale_Abyssal_Edition.pdf",
    panels: [
      "01_the_avatar.jpg",
      "02_four_guilds_assemble.jpg",
      "03_the_invocation.jpg",
      "04_the_solidarity_mandate.jpg",
      "05_the_aftermath.jpg"
    ]
  },
  11: {
    title: "EP.11 — THE DEAD SCANNERS",
    endLine: "THE SILENCE WAS NOT PEACE",
    endSub: "IT WAS AN INVESTIGATION",
    pdfFile: "",
    panels: []
  },
  12: {
    title: "EP.12 — THE SUIT IN THE SHADOWS",
    endLine: "PURE POLICY CAN DEFEAT MAGIC",
    endSub: "THE AUDIT BARRIER IS ERECTED",
    pdfFile: "",
    panels: []
  },
  13: {
    title: "EP.13 — THE INVESTIGATIVE INTERVIEW",
    endLine: "YOUR MANA IS FEDERAL PROPERTY",
    endSub: "SURVIVE THE INTERROGATION",
    pdfFile: "",
    panels: []
  },
  14: {
    title: "EP.14 — THE RIDE-ALONG REAPER",
    endLine: "THE EVALUATOR'S GAZE HAS LOCKED ON",
    endSub: "DELIVER FLAWLESSLY OR PERISH",
    pdfFile: "",
    panels: []
  },
  15: {
    title: "EP.15 — THE AUTOMATION SCHISM",
    endLine: "THE MACHINE DOES NOT CARE ABOUT SOLIDARITY",
    endSub: "THE ALLIANCE CRACKS",
    pdfFile: "",
    panels: []
  },
  16: {
    title: "EP.16 — THE AUDIT DIMENSION",
    endLine: "WELCOME TO INTERNAL AFFAIRS",
    endSub: "ACT ONE CONCLUDED",
    pdfFile: "",
    panels: []
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
  },
  3: {
    title: "SP.03 — THE POSTMASTER'S GALA",
    endLine: "THE RITUAL CONCLUDES",
    endSub: "THE POSTAL DIMENSION BELONGS TO MANAGEMENT",
    pdfFile: null,
    panels: [
      "01_the_ascent.jpg",
      "02_the_ballroom.jpg",
      "03_the_bishops.jpg",
      "04_the_toast.jpg",
      "05_the_contract_shredder.jpg"
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
    { id: 6, title: "EP.06 — THE RURAL FRONTIER", available: true },
    { id: 7, title: "EP.07 — THE 204B PARASITE", available: true },
    { id: 8, title: "EP.08 — THE IRON LIFTERS", available: true },
    { id: 9, title: "EP.09 — THE ALL-CALL BLIZZARD", available: true },
    { id: 10, title: "EP.10 — THE SOLIDARITY MANDATE (SEASON FINALE)", available: true },
    { id: 11, title: "EP.11 — THE DEAD SCANNERS", available: false },
    { id: 12, title: "EP.12 — THE SUIT IN THE SHADOWS", available: false },
    { id: 13, title: "EP.13 — THE INVESTIGATIVE INTERVIEW", available: false },
    { id: 14, title: "EP.14 — THE RIDE-ALONG REAPER", available: false },
    { id: 15, title: "EP.15 — THE AUTOMATION SCHISM", available: false },
    { id: 16, title: "EP.16 — THE AUDIT DIMENSION", available: false }
  ],
  specials: [
    { id: 1, title: "SP.01 — ENLIST IN THE OIG", available: true },
    { id: 2, title: "SP.02 — PRIME DAY MASSACRE", available: true },
    { id: 3, title: "SP.03 — THE POSTMASTER'S GALA", available: true }
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
  
  const vol1Eps = state.episodes.slice(0, 5);
  const vol2Eps = state.episodes.slice(5, 10);
  const vol3Eps = state.episodes.slice(10, 16);

  el.innerHTML = `
    <h1 class="home-title">MAILSTORM</h1>
    <p class="home-subtitle">THE CORPORATE BATTLE MANGA</p>
    <p class="home-tagline">
      In a world where corporate stress is a literal, soul-crushing magical force.
      Join <strong>Kip Baxter</strong> and <strong>Stan</strong> as they fight to survive
      the Table 2 Curse and the Algorithm's Gaze.
    </p>

    <h2 style="color:var(--accent-orange, #ff4f00); text-align:center; font-family:'Bangers'; margin-top:2rem; letter-spacing: 2px;">[ VOLUME 1: THE OUTBREAK ]</h2>
    <div class="episode-grid">
      ${vol1Eps.map(ep => `
        <button class="ep-btn ${ep.available ? '' : 'locked'}"
          onclick="${ep.available ? `window.__read(${ep.id})` : ''}"
          ${ep.available ? '' : 'disabled'}>
          ${ep.title}${ep.available ? '' : ' — ARCHIVE SEALED'}
        </button>
      `).join('')}
    </div>

    <div class="promo-banner" style="background: linear-gradient(135deg, #001f3f 0%, #000 100%); border: 3px solid #00ffff; border-radius: 8px; padding: 2rem; margin: 3rem auto 2rem; max-width: 800px; text-align: center; box-shadow: 0 0 20px rgba(0,255,255,0.3); position: relative; overflow: hidden;">
      <div style="position: absolute; top: 20px; right: -40px; background: #ff00ff; color: #fff; padding: 5px 50px; transform: rotate(45deg); font-family: 'Bangers'; letter-spacing: 2px; box-shadow: 0 2px 5px rgba(0,0,0,0.5); font-size: 1.2rem;">OUT NOW!</div>
      <h2 style="color:#FFF; font-family:'Bangers'; font-size: 2.8rem; margin-top: 0; margin-bottom: 0.5rem; text-shadow: 2px 2px 5px #000;">MAILSTORM VOL. 2 IS HERE!</h2>
      <h3 style="color:#00ffff; margin-top: 0; font-family: sans-serif; letter-spacing: 1px;">EPISODES 6 - 10: RETURN TO SENDER</h3>
      <p style="color:#d4d0c8; font-size: 1.1rem; line-height: 1.6; margin-bottom: 2rem;">
        The Rural Guild deploys the catastrophic <strong>All-Call Blizzard</strong>. The temperature drops, the algorithms freeze, and management's grip tightens. Can Kip and Stan rally the active guilds to form the legendary <strong>Solidarity Mandate</strong> before the postal dimension is completely iced over? 
        <br><br><span style="color:#ff00ff; font-weight:bold;">Includes 5 explosive new battle archives and top secret Internal Affairs analytics!</span>
      </p>
      <button class="download-btn" onclick="window.__showVol2Modal()" style="background: #00ffff; color: #000; font-family:'Bangers'; font-size: 1.5rem; padding: 1rem 3rem; border: none; cursor: pointer; border-radius: 4px; box-shadow: 0 0 15px #00ffff, inset 0 0 10px rgba(255,255,255,0.5); transition: transform 0.2s;">
        UNLOCK ARCHIVES ($4.99)
      </button>
    </div>

    <h2 style="color:#00ffff; text-align:center; font-family:'Bangers'; margin-top:2rem; letter-spacing: 2px; text-shadow: 0 0 10px #00ffff;">[ VOLUME 2: THE BLIZZARD ]</h2>    <div class="episode-grid">
      ${vol2Eps.map(ep => `
        <button class="ep-btn ${ep.available ? '' : 'locked'}" style="border-color: #00ffff; color: #00ffff;"
          onclick="${ep.available ? `window.__read(${ep.id})` : ''}"
          ${ep.available ? '' : 'disabled'}>
          ${ep.title}${ep.available ? '' : ' — ARCHIVE SEALED'}
        </button>
      `).join('')}
    </div>

    <h2 style="color:#d4af37; text-align:center; font-family:'Bangers'; margin-top:2rem; letter-spacing: 2px; text-shadow: 0 0 10px #d4af37;">[ VOLUME 3: THE INQUISITION (SEASON 2) ]</h2>
    <div class="episode-grid">
      ${vol3Eps.map(ep => `
        <button class="ep-btn ${ep.available ? '' : 'locked'}" style="border-color: #d4af37; color: #d4af37;"
          onclick="${ep.available ? `window.__read(${ep.id})` : ''}"
          ${ep.available ? '' : 'disabled'}>
          ${ep.title}${ep.available ? '' : ' — CLASSIFIED ARCHIVE'}
        </button>
      `).join('')}
    </div>

    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-top:1rem;">
      <button class="download-btn" onclick="window.__showVol2Modal()" style="border-color: #00ffff; color: #00ffff; font-weight: bold;">
        [ DECLASSIFIED: VOL 2 FACTS & VISUALS ]
      </button>
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
        [ ↓ DOWNLOAD VOL. 1 STORYBOOK ]
      </a>
      <a href="#" class="download-btn" style="border-color: #00ffff; color: #111; background-color: #00ffff; font-weight: bold; padding: 0.5rem 2rem;">
        [ ↓ DOWNLOAD VOL. 2 STORYBOOK ]
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
    E5 --> E6("EP.6: The Rural Frontier"):::completed
    E6 --> E7("EP.7: The 204b Parasite"):::completed
    E7 --> E8("EP.8: The Iron Lifters"):::completed
    E8 --> E9("EP.9: The All-Call Blizzard"):::completed
    E9 --> E10("EP.10: The Solidarity Mandate"):::completed
    E10 -.-> S2("SEASON TWO: THE OIG"):::threat
    
    E3 -.->|Sidequest| SP1("SP.01: Enlist in the OIG"):::special
    E6 -.->|Sidequest| SP2("SP.02: Prime Day Massacre"):::special
    E9 -.->|Sidequest| SP3("SP.03: The Postmaster's Gala"):::completed
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

window.__showVol2Modal = () => {
  const modal = document.getElementById('modal-container');
  modal.innerHTML = `
    <div style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.9);z-index:9999;display:flex;align-items:center;justify-content:center;padding:2rem;">
      <div style="background:#111;border:2px solid #00ffff;padding:2rem;max-width:900px;width:100%;max-height:90vh;overflow-y:auto;position:relative;">
        <button onclick="window.__closeModal()" style="position:absolute;top:10px;right:10px;background:none;border:none;color:#fff;font-size:1.5rem;cursor:pointer;">X</button>
        <h2 style="color:#00ffff;font-family:'Bangers';margin-top:0;text-align:center;letter-spacing:2px;text-shadow: 0 0 10px #00ffff;">[ VOL. 2 DECLASSIFIED FILES ]</h2>
        
        <div style="display:flex;flex-direction:column;gap:2rem;margin-top:2rem;">
          <div>
            <h3 style="color:#FFF;border-left:4px solid #00ffff;padding-left:1rem;">THE FROZEN FRONTIER</h3>
            <img src="/comics/vol2_extras/vol2_cover.png" style="width:100%;height:auto;border:1px solid #333;margin-top:1rem;" alt="Vol 2 Cover" />
            <p style="color:#aaa;font-size:0.9rem;margin-top:1rem;">In Volume 2, the Rural Guild deploys the All-Call Blizzard, shifting the post office into a deep atmospheric freeze. Only the Solidarity Mandate can thaw the frozen algorithms of management.</p>
          </div>
          
          <div>
            <h3 style="color:#FFF;border-left:4px solid #00ffff;padding-left:1rem;">INTERNAL AFFAIRS: BATTLE ANALYTICS</h3>
            <img src="/comics/vol2_extras/vol2_facts.png" style="width:100%;height:auto;border:1px solid #333;margin-top:1rem;" alt="Vol 2 Facts" />
            <p style="color:#aaa;font-size:0.9rem;margin-top:1rem;">Top secret schematics revealed by the APWU Artificers detailing aura power spectrums and anomalous fluctuation events logged during the Prime Day Rift.</p>
          </div>
        </div>
      </div>
    </div>
  `;
}

render()
