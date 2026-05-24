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
    panels: [
      {
        image: "01_dark_screens.png",
        text: "<strong>KIP:</strong> Stan... the scanner is dead. It's completely dark. No 'Stationary Events.' No Algorithm tracking my heart rate. Is this... is the Table 2 Curse broken? Is this the end of the world?<br><br><strong>STAN:</strong> No, kid. The end of the world involves way more Amazon packages. This is worse. The Algorithm didn't crash. It was subpoenaed. Hold onto your ass."
      },
      {
        image: "02_the_silence.png",
        text: "<strong>NARRATOR:</strong> For 43 minutes, the Post Office was completely silent. The Machine Communion of the sorting floor had ceased. The 204b Parasites were nowhere to be seen."
      },
      {
        image: "03_false_peace.png",
        text: "<strong>HEATHER:</strong> Okay, this stationary event is literally mid. My 4K Aegis Shield is picking up zero management signals. Should I call the Union or just take an unauthorized nap?<br><br><strong>STAN:</strong> Don't get comfortable. If Management is quiet, they aren't retreating. They’re just reloading a bigger gun."
      },
      {
        image: "04_the_sedan.png",
        text: "<strong>NARRATOR:</strong> At exactly 17:00, the temperature on the loading dock dropped to absolute zero. The Federal Sedan phased through the gates, radiating an aura so cold and rigidly bureaucratic that it froze the concrete."
      },
      {
        image: "05_agent_vance.png",
        text: "<strong>AGENT VANCE:</strong> I am Special Agent Vance, Office of the Inspector General. Your 'Solidarity Mandate' anomaly has triggered a Level 5 Audit. Your mana is now federal property. Provide your badge, or I will sublimate your marrow."
      }
    ]
  },
  12: {
    title: "EP.12 — THE WEINGARTEN WARD",
    endLine: "PURE POLICY CAN DEFEAT MAGIC",
    endSub: "THE AUDIT BARRIER IS ERECTED",
    pdfFile: "",
    panels: [
      {
        image: "01_vance_bypass.png",
        text: "Agent Vance arrives. The ambient temperature plummets as his terrifying, perfectly sterile grid aura immediately flattens Chuck's shadowy dominance."
      },
      {
        image: "02_target.png",
        text: "Bypassing the veterans entirely, Vance targets the weakest link: Kip Baxter. The 'Investigative Interview' begins without warning or union representation."
      },
      {
        image: "03_logic_loop.png",
        text: "Kip is caught in a 'Logic-Loop.' His yellow anxiety aura is brutally crushed under a suffocating cage of pure mathematical efficiency."
      },
      {
        image: "04_the_slam.png",
        text: "A thunderous impact echoes across the sorting floor. The Union Paladin has arrived."
      },
      {
        image: "05_weingarten_smite.png",
        text: "THE WEINGARTEN SMITE! Barb slams the Master Contract down. An explosion of blinding Contractual Logic erupts across the Sorting Floor, physically blasting the OIG Agent's aura backward!"
      }
    ]
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
    { id: 11, title: "EP.11 — THE DEAD SCANNERS", available: true },
    { id: 12, title: "EP.12 — THE WEINGARTEN WARD", available: true },
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
  else if (state.view === 'continuity') renderContinuity()
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
      <button class="download-btn" onclick="window.__openContinuity()" style="border-color: #33ff33; color: #33ff33;">[ ⚲ OPEN CONTINUITY BIBLE ]</button>
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
  window.__openContinuity = () => { state.view = 'continuity'; state.activeConsoleTab = state.activeConsoleTab || 'chars'; render() }
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
  epData.panels.forEach(item => {
    const isObj = typeof item === 'object';
    const file = isObj ? item.image : item;
    const text = isObj ? item.text : null;

    const wrapper = document.createElement('div')
    wrapper.className = 'panel-wrapper'
    const img = document.createElement('img')
    img.src = `/comics/${folder}/${file}`
    img.alt = file.replace('.png','').replace('.jpg','').replace(/_/g,' ')
    img.loading = 'lazy'
    img.onload = () => img.classList.add('loaded')
    wrapper.appendChild(img)

    if (text) {
      const caption = document.createElement('div');
      caption.className = 'panel-caption';
      caption.innerHTML = text;
      wrapper.appendChild(caption);
    }

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

// === CONTINUITY DATA ===
const CONTINUITY_CHARS = {
  stan: {
    name: "Stan",
    class: "City Carrier (Level 42 Regular)",
    alignment: "Lawful Apathetic",
    statName: "Street Efficiency",
    statVal: 95,
    mana: 80,
    specialVal: 10,
    specialLabel: "Rookie Tolerance",
    buffs: ["Caffeine Fortress", "Unbreakable Stride"],
    debuffs: ["Lower Back Strain"],
    relics: "Stained Mug, Heavy Satchel"
  },
  kip: {
    name: "Kip Baxter",
    class: "City Carrier Assistant (Level 5)",
    alignment: "Anxious Ascendant",
    statName: "Anxiety Margin",
    statVal: 85,
    mana: 20,
    specialVal: 90,
    specialLabel: "Algorithm Panic",
    buffs: ["Youth Agility"],
    debuffs: ["Table 2 Curse (Bone-Marrow Burn)"],
    relics: "Green Tag Bag"
  },
  barb: {
    name: "Barb",
    class: "Shop Steward (Level 55 Union Paladin)",
    alignment: "Contractual Enforcer",
    statName: "Defense Rating",
    statVal: 98,
    mana: 90,
    specialVal: 95,
    specialLabel: "Grievance Artillery",
    buffs: ["Article 16 Shield", "Unbreakable Union Contract"],
    debuffs: ["Excessive Meetings"],
    relics: "Master Contract, Steward Gavel"
  },
  chuck: {
    name: "Chuck",
    class: "Supervisor (Level 45 Controller)",
    alignment: "Petty Demonic",
    statName: "Audacity Level",
    statVal: 80,
    mana: 15,
    specialVal: 85,
    specialLabel: "Algorithm Vigilance",
    buffs: ["Vance's Backing"],
    debuffs: ["Incompetence Loop", "Lost 1767 Forms"],
    relics: "MDD Scanner, Clip-On Badge"
  },
  heather: {
    name: "Heather",
    class: "Rural Carrier (Level 12 Berserker)",
    alignment: "Chaotic Apathetic",
    statName: "Velocity Metric",
    statVal: 90,
    mana: 40,
    specialVal: 95,
    specialLabel: "Gen Z Disdain",
    buffs: ["Apathy Shield", "Evaluation Blitz"],
    debuffs: ["Glued to Screen"],
    relics: "Subaru Outback, 4K Aegis Satchel"
  },
  sparky: {
    name: "Sparky",
    class: "Maintenance Tech (Level 38 Artificer)",
    alignment: "Support Wildcard",
    statName: "Repair Spite",
    statVal: 85,
    mana: 50,
    specialVal: 75,
    specialLabel: "Sober Withdrawal Rage",
    buffs: ["Technical Recall", "Tool Mastery"],
    debuffs: ["Severe Nicotine Deprivation"],
    relics: "Hydraulic Jack, Lock Wrench"
  }
};

const CONTINUITY_TIMELINE = [
  { id: 1, title: "EP.01 — THE SHADOW DAY", released: true, location: "Carrier Cases", milestone: "Kip gets hired; Stan performs the Shadow Day ritual.", grievance: "None", relic: "Stan's Stained Mug" },
  { id: 2, title: "EP.02 — TABLE 2 BLOODLINE", released: true, location: "Carrier Cases", milestone: "Kip experiences the Table 2 Curse (Bone-Marrow Burn).", grievance: "None", relic: "Green Tag Bag" },
  { id: 3, title: "EP.03 — THE PIVOT DIMENSION", released: true, location: "The LLV Graveyard", milestone: "Kip and Stan enter the time-dilated Pivot Dimension.", grievance: "None", relic: "64-Wraps" },
  { id: 4, title: "EP.04 — THE CBA SHIELD", released: true, location: "Carrier Cases", milestone: "Union Steward Barb defends carriers from Chuck's scanner sweeps.", grievance: "Article 8 Vow", relic: "Master Contract" },
  { id: 5, title: "EP.05 — DEAD LETTER DEEP-DIVE", released: true, location: "Carrier Cases", milestone: "Descent into the Dead Letter Office (DLO) to find Benjamin Franklin's ghost.", grievance: "Article 16 Shield", relic: "Golden Arrow Key" },
  { id: 6, title: "EP.06 — THE RURAL FRONTIER", released: true, location: "The LLV Graveyard", milestone: "Alliance with Heather and the Rural Carrier rangers.", grievance: "None", relic: "RHD Subaru Outback" },
  { id: 7, title: "EP.07 — THE 204B PARASITE", released: true, location: "The Supervisor's Podium", milestone: "A 204b tries to infect the carriers but is rejected.", grievance: "Weingarten Rite", relic: "None" },
  { id: 8, title: "EP.08 — THE IRON LIFTERS", released: true, location: "The Loading Dock", milestone: "Mail Handlers defend the dock during the Siege of Tour 3.", grievance: "None", relic: "Tub Shield" },
  { id: 9, title: "EP.09 — THE ALL-CALL BLIZZARD", released: true, location: "The Loading Dock", milestone: "All guilds unite to survive the freezing of the Algorithm.", grievance: "None", relic: "Postal Beanie" },
  { id: 10, title: "EP.10 — THE SOLIDARITY MANDATE", released: true, location: "Carrier Cases", milestone: "The four guilds assemble to sever the localized Algorithm.", grievance: "Step 4 National Strike", relic: "Solidarity Mandate Key" },
  { id: 11, title: "EP.11 — THE DEAD SCANNERS", released: true, location: "The Loading Dock", milestone: "Silence falls on the post office as OIG Agent Vance arrives.", grievance: "None", relic: "Dark Scanner" },
  { id: 12, title: "EP.12 — THE WEINGARTEN WARD", released: true, location: "Carrier Cases", milestone: "Barb uses the Weingarten Smite to blast Agent Vance's aura.", grievance: "Weingarten Rite Summon", relic: "Weingarten Smite" },
  { id: 13, title: "EP.13 — THE INVESTIGATIVE INTERVIEW", released: false, location: "The Supervisor's Podium", milestone: "Kip must survive Vance and Chuck's interrogation without cracking.", grievance: "Weingarten Rite Summon", relic: "Union Contract Shield" },
  { id: 14, title: "EP.14 — THE RIDE-ALONG REAPER", released: false, location: "The LLV Graveyard", milestone: "Vance forces a street ride-along. Kip must deliver flawlessly under surveillance pressure.", grievance: "Article 14 Safety Shield", relic: "Orange Ward" },
  { id: 15, title: "EP.15 — THE AUTOMATION SCHISM", released: false, location: "Carrier Cases", milestone: "Sorting machines go wild; Clerks (APWU) and Carriers clash over floor control.", grievance: "Machine Override", relic: "DBCS Sorting Machine" },
  { id: 16, title: "EP.16 — THE AUDIT DIMENSION", released: false, location: "Front Lobby", milestone: "Vance pulls Kip into the Audit Dimension; Stan steps in to trigger the Founding Mandate.", grievance: "Step 4 National Strike", relic: "Solidarity Mandate Key" }
];

const FACILITY_MAP = {
  "Front Lobby": { x: "15%", y: "20%" },
  "Carrier Cases": { x: "50%", y: "40%" },
  "The Supervisor's Podium": { x: "80%", y: "25%" },
  "The Loading Dock": { x: "50%", y: "75%" },
  "The LLV Graveyard": { x: "15%", y: "80%" },
  "The Breakroom": { x: "85%", y: "75%" }
};

const LORE_VIOLATIONS = [
  { term: "vape", warning: "[SOBRIETY LOG WARNING] Ensure Stan stays clean. Standard sobriety metrics are reset to Day 0 if a vape/hash is purchased." },
  { term: "marijuana", warning: "[SOBRIETY LOG WARNING] Ensure Stan stays clean. Standard sobriety metrics are reset to Day 0 if a vape/hash is purchased." },
  { term: "hash", warning: "[SOBRIETY LOG WARNING] Ensure Stan stays clean. Standard sobriety metrics are reset to Day 0 if a vape/hash is purchased." },
  { speaker: "KIP", term: "8 & skate", warning: "[LORE CONTRADICTION] Kip (CCA) cannot perform the 8 & Skate teleportation jutsu without Career status. Only Level 11+ Regulars can cast this spell." },
  { speaker: "KIP", term: "eight and skate", warning: "[LORE CONTRADICTION] Kip (CCA) cannot perform the 8 & Skate teleportation jutsu without Career status. Only Level 11+ Regulars can cast this spell." },
  { speaker: "KIP", term: "plant", warning: "[GEOGRAPHY CONTRADICTION] Kip is a CCA and works out of a local Delivery Station, not the Processing Plant. Plant floors sort bulk mail using APWU Clerks, PSEs, and NPMHU Mail Handlers." },
  { speaker: "KIP", term: "pdc", warning: "[GEOGRAPHY CONTRADICTION] Kip is a CCA and works out of a local Delivery Station, not the P&DC. Plant floors sort bulk mail using APWU Clerks, PSEs, and NPMHU Mail Handlers." },
  { speaker: "STAN", term: "plant", warning: "[GEOGRAPHY CONTRADICTION] Stan is a City Carrier and works out of a local Delivery Station, not the Processing Plant. Plant floors sort bulk mail using APWU Clerks, PSEs, and NPMHU Mail Handlers." },
  { speaker: "STAN", term: "pdc", warning: "[GEOGRAPHY CONTRADICTION] Stan is a City Carrier and works out of a local Delivery Station, not the P&DC. Plant floors sort bulk mail using APWU Clerks, PSEs, and NPMHU Mail Handlers." },
  { speaker: "STAN", term: "run", warning: "[CHARACTER ANOMALY] Stan's Lawful Apathetic alignment prevents him from running or rushing. Maintain the Unbreakable Stride passive." },
  { speaker: "STAN", term: "rushed", warning: "[CHARACTER ANOMALY] Stan's Lawful Apathetic alignment prevents him from running or rushing. Maintain the Unbreakable Stride passive." },
  { speaker: "STAN", term: "sprinted", warning: "[CHARACTER ANOMALY] Stan's Lawful Apathetic alignment prevents him from running or rushing. Maintain the Unbreakable Stride passive." },
  { term: "investigation", require: "Weingarten", warning: "[UNION VIOLATION WARNING] Disciplinary interviews must trigger the Weingarten Rite. A Shop Steward must be summoned." },
  { term: "disciplinary", require: "Weingarten", warning: "[UNION VIOLATION WARNING] Disciplinary interviews must trigger the Weingarten Rite. A Shop Steward must be summoned." }
];

function renderContinuity() {
  app.innerHTML = '';
  
  const container = document.createElement('div');
  container.className = 'continuity-container';
  
  container.innerHTML = `
    <div class="console-header">
      <div>
        <div class="console-title">ABYSSAL CENTRAL MAINFRAME // CONTINUITY BIBLE</div>
        <div class="console-subtitle">SYSTEM STATUS: OPERATIONAL // DIRECTIVES UNCOMPROMISED</div>
      </div>
      <button class="download-btn" onclick="window.__closeContinuity()" style="margin:0; border-color:#888; color:#888; padding: 0.4rem 1.5rem; font-size: 0.8rem;">← BACK TO PORTAL</button>
    </div>
    <div class="console-body">
      <div class="console-sidebar">
        <button class="console-tab-btn ${state.activeConsoleTab === 'chars' ? 'active' : ''}" onclick="window.__setTab('chars')">[ CHARACTER MATRIX ]</button>
        <button class="console-tab-btn ${state.activeConsoleTab === 'timeline' ? 'active' : ''}" onclick="window.__setTab('timeline')">[ EPISODE LEDGER ]</button>
        <button class="console-tab-btn ${state.activeConsoleTab === 'map' ? 'active' : ''}" onclick="window.__setTab('map')">[ METRO HUB MAP ]</button>
        <button class="console-tab-btn ${state.activeConsoleTab === 'analyzer' ? 'active' : ''}" onclick="window.__setTab('analyzer')">[ SCRIPT AUDITOR ]</button>
      </div>
      <div class="console-main-pane" id="console-pane"></div>
    </div>
  `;
  
  app.appendChild(container);
  
  // Render active pane content
  const pane = document.getElementById('console-pane');
  if (state.activeConsoleTab === 'chars') renderCharTab(pane);
  else if (state.activeConsoleTab === 'timeline') renderTimelineTab(pane);
  else if (state.activeConsoleTab === 'map') renderMapTab(pane);
  else if (state.activeConsoleTab === 'analyzer') renderAnalyzerTab(pane);
  
  window.__setTab = (tab) => {
    state.activeConsoleTab = tab;
    renderContinuity();
  };
}

function renderCharTab(pane) {
  pane.innerHTML = '';
  const grid = document.createElement('div');
  grid.className = 'character-matrix';
  
  Object.keys(CONTINUITY_CHARS).forEach(key => {
    const char = CONTINUITY_CHARS[key];
    const card = document.createElement('div');
    card.className = 'char-card';
    
    card.innerHTML = `
      <div class="char-card-header">
        <div class="char-name">${char.name}</div>
        <div class="char-class">${char.class}</div>
      </div>
      <div style="font-size:0.8rem;color:#888;margin-bottom:1rem;">
        Alignment: <span style="color:#ffb000;">${char.alignment}</span>
      </div>
      
      <div class="char-stat-row">
        <div class="char-stat-label">
          <span>${char.statName}</span>
          <span id="${key}-stat-val">${char.statVal}%</span>
        </div>
        <div class="char-stat-bar-container">
          <div class="char-stat-bar" id="${key}-stat-bar" style="width: ${char.statVal}%;"></div>
        </div>
        <div class="char-slider-label">
          <input type="range" min="0" max="100" class="char-slider" value="${char.statVal}" oninput="window.__updateCharStat('${key}', this.value)">
        </div>
      </div>
      
      <div class="char-stat-row">
        <div class="char-stat-label">
          <span>Grievance Mana</span>
          <span id="${key}-mana-val">${char.mana} / 100</span>
        </div>
        <div class="char-stat-bar-container">
          <div class="char-stat-bar mana" id="${key}-mana-bar" style="width: ${char.mana}%;"></div>
        </div>
        <div class="char-slider-label">
          <input type="range" min="0" max="100" class="char-slider" value="${char.mana}" oninput="window.__updateCharMana('${key}', this.value)">
        </div>
      </div>
      
      <div style="font-size: 0.8rem; margin-top: 1rem; border-top: 1px solid #222; padding-top: 0.5rem;">
        <strong>Relics:</strong> <span style="color:#aaa;">${char.relics}</span>
      </div>
      
      <div style="font-size: 0.8rem; margin-top: 0.5rem;">
        <strong>Active Buffs:</strong> 
        ${char.buffs.map(b => `<span class="status-badge active" style="margin-right:4px; font-size: 0.65rem;">${b}</span>`).join('')}
      </div>
      
      <div style="font-size: 0.8rem; margin-top: 0.5rem;">
        <strong>Active Debuffs:</strong> 
        ${char.debuffs.map(d => `<span class="status-badge inactive" style="margin-right:4px; font-size: 0.65rem;">${d}</span>`).join('')}
      </div>
    `;
    
    grid.appendChild(card);
  });
  
  pane.appendChild(grid);
  
  window.__updateCharStat = (key, val) => {
    CONTINUITY_CHARS[key].statVal = val;
    document.getElementById(`${key}-stat-val`).innerText = val + '%';
    document.getElementById(`${key}-stat-bar`).style.width = val + '%';
  };
  
  window.__updateCharMana = (key, val) => {
    CONTINUITY_CHARS[key].mana = val;
    document.getElementById(`${key}-mana-val`).innerText = val + ' / 100';
    document.getElementById(`${key}-mana-bar`).style.width = val + '%';
  };
}

function renderTimelineTab(pane) {
  pane.innerHTML = '';
  const ledger = document.createElement('div');
  ledger.className = 'timeline-ledger';
  
  CONTINUITY_TIMELINE.forEach(ep => {
    const item = document.createElement('div');
    item.className = 'timeline-item';
    
    // USPS package tracking scan statuses
    let scanText = "IN TRANSIT";
    let badgeClass = "inactive";
    
    if (ep.released) {
      scanText = "DELIVERED";
      badgeClass = "active";
    } else if (ep.id === 13) {
      scanText = "OUT FOR DELIVERY";
      badgeClass = "warning";
    }
    
    item.innerHTML = `
      <div class="timeline-item-header">
        <div class="timeline-ep-title">${ep.title}</div>
        <span class="status-badge ${badgeClass}">${scanText}</span>
      </div>
      <div style="font-size: 0.85rem; margin-bottom: 0.8rem; color:#aaa;">
        <strong>Facility Location:</strong> <span style="color:#ffb000;">${ep.location}</span>
      </div>
      <div style="font-size: 0.9rem; line-height: 1.5; color:#eee; margin-bottom: 1rem;">
        <strong>Plot Milestone:</strong> ${ep.milestone}
      </div>
      <div class="ledger-rules-grid">
        <div class="ledger-rule-box">
          <h4>Union Contract Clause invoked</h4>
          <p>${ep.grievance}</p>
        </div>
        <div class="ledger-rule-box">
          <h4>Active Relic Introduced</h4>
          <p>${ep.relic}</p>
        </div>
      </div>
    `;
    
    ledger.appendChild(item);
  });
  
  pane.appendChild(ledger);
}

function renderMapTab(pane) {
  pane.innerHTML = '';
  
  const container = document.createElement('div');
  container.className = 'map-container';
  
  container.innerHTML = `
    <div class="map-controls">
      <h3 style="margin-top:0; color:#fff; font-size:1.1rem; border-bottom:1px solid #222; padding-bottom: 0.5rem;">LOCATE EPISODE</h3>
      <select id="map-episode-select" style="background:#111; border:1px solid #333; color:#33ff33; padding: 0.8rem; font-family:monospace; width:100%; cursor:pointer;">
        ${CONTINUITY_TIMELINE.map(ep => `<option value="${ep.id}">${ep.title}</option>`).join('')}
      </select>
      <div style="font-size:0.8rem; color:#666; margin-top:1rem; line-height:1.4;">
        Observe how characters move through the non-Euclidean coordinates of Metro Hub South as the plot nodes progress.
      </div>
    </div>
    <div class="map-viewport" id="map-viewport">
      <!-- Retro grid blueprint map -->
      <svg id="blueprint-svg" width="100%" height="450px" style="border:1px solid #222; background: #080808;">
        <!-- Grid pattern -->
        <defs>
          <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#111" stroke-width="1"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid)" />
        
        <!-- Blueprint walls -->
        <rect x="5%" y="10%" width="90%" height="80%" fill="none" stroke="#222" stroke-width="2" stroke-dasharray="5 5"/>
        <line x1="40%" y1="10%" x2="40%" y2="90%" stroke="#222" stroke-width="1.5" stroke-dasharray="5 5" />
        <line x1="5%" y1="60%" x2="95%" y2="60%" stroke="#222" stroke-width="1.5" stroke-dasharray="5 5" />
        
        <!-- Zone text labels -->
        <text x="22.5%" y="35%" fill="#444" font-size="12px" text-anchor="middle" font-family="monospace">FRONT LOBBY</text>
        <text x="22.5%" y="75%" fill="#444" font-size="12px" text-anchor="middle" font-family="monospace">LLV GRAVEYARD</text>
        <text x="67.5%" y="42%" fill="#444" font-size="12px" text-anchor="middle" font-family="monospace">CARRIER CASES</text>
        <text x="80%" y="15%" fill="#444" font-size="12px" text-anchor="middle" font-family="monospace">SUPERVISOR PODIUM</text>
        <text x="67.5%" y="80%" fill="#444" font-size="12px" text-anchor="middle" font-family="monospace">LOADING DOCK</text>
        <text x="90%" y="85%" fill="#444" font-size="12px" text-anchor="middle" font-family="monospace">BREAKROOM</text>
        
        <!-- SVG Interactive tokens will be drawn here dynamically -->
        <g id="map-tokens"></g>
      </svg>
      <div class="map-legend">GREEN = ACTIVE // CRT BLUEPRINT AT DEPTH 61</div>
    </div>
  `;
  
  pane.appendChild(container);
  
  const select = document.getElementById('map-episode-select');
  select.addEventListener('change', (e) => {
    updateMapTokens(parseInt(e.target.value));
  });
  
  // Set default selection
  updateMapTokens(1);
}

function updateMapTokens(epId) {
  const g = document.getElementById('map-tokens');
  if(!g) return;
  g.innerHTML = '';
  
  const ep = CONTINUITY_TIMELINE.find(item => item.id === epId);
  if(!ep) return;
  
  // Positions mapping
  const positions = {
    1: { stan: "Carrier Cases", kip: "Front Lobby", chuck: "The Supervisor's Podium" },
    2: { stan: "Carrier Cases", kip: "Carrier Cases", chuck: "The Supervisor's Podium" },
    3: { stan: "Carrier Cases", kip: "The LLV Graveyard", chuck: "The Supervisor's Podium" },
    4: { stan: "Carrier Cases", kip: "Carrier Cases", barb: "Carrier Cases", chuck: "The Supervisor's Podium" },
    5: { stan: "Carrier Cases", kip: "Carrier Cases", sparky: "Carrier Cases" },
    6: { heather: "The LLV Graveyard", stan: "The Loading Dock", kip: "The LLV Graveyard" },
    7: { chuck: "The Supervisor's Podium", barb: "Carrier Cases", kip: "Carrier Cases" },
    8: { stan: "The Loading Dock", chuck: "The Supervisor's Podium", sparky: "The Loading Dock" },
    9: { stan: "The Loading Dock", kip: "The Loading Dock", heather: "The Loading Dock", barb: "The Loading Dock", chuck: "The Supervisor's Podium" },
    10: { stan: "Carrier Cases", kip: "Carrier Cases", barb: "Carrier Cases", heather: "Carrier Cases", chuck: "The Supervisor's Podium", sparky: "Carrier Cases" },
    11: { stan: "The Loading Dock", kip: "The Loading Dock", heather: "The Loading Dock", chuck: "The Supervisor's Podium" },
    12: { stan: "Carrier Cases", kip: "Carrier Cases", barb: "Carrier Cases", chuck: "The Supervisor's Podium" },
    13: { chuck: "The Supervisor's Podium", kip: "The Supervisor's Podium", stan: "Carrier Cases" },
    14: { kip: "The LLV Graveyard", chuck: "The Supervisor's Podium", stan: "Carrier Cases" },
    15: { stan: "Carrier Cases", kip: "Carrier Cases", sparky: "Carrier Cases" },
    16: { kip: "Front Lobby", stan: "Front Lobby", chuck: "The Supervisor's Podium", barb: "Front Lobby" }
  };
  
  const mapping = positions[epId] || {};
  
  let tokenCount = 0;
  Object.keys(mapping).forEach(name => {
    const loc = mapping[name];
    const coords = FACILITY_MAP[loc];
    if (coords) {
      tokenCount++;
      // Parse coordinates as numbers from percentage
      const xPercent = parseFloat(coords.x);
      const yPercent = parseFloat(coords.y);
      
      const cx = (xPercent / 100) * 100; // keep in percentage for SVG mapping
      const cy = (yPercent / 100) * 100;
      
      // Draw token dot
      const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      circle.setAttribute("cx", cx + "%");
      circle.setAttribute("cy", (cy + (tokenCount * 4 - 8)) + "%"); // slight vertical offset for overlap prevention
      circle.setAttribute("r", "10");
      circle.setAttribute("fill", "#050505");
      circle.setAttribute("stroke", "#33ff33");
      circle.setAttribute("stroke-width", "2");
      circle.style.cursor = "pointer";
      
      // Draw glow ring
      const pulse = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      pulse.setAttribute("cx", cx + "%");
      pulse.setAttribute("cy", (cy + (tokenCount * 4 - 8)) + "%");
      pulse.setAttribute("r", "16");
      pulse.setAttribute("fill", "none");
      pulse.setAttribute("stroke", "#33ff33");
      pulse.setAttribute("stroke-dasharray", "2 2");
      pulse.setAttribute("opacity", "0.4");
      
      // Draw text token label
      const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
      text.setAttribute("x", cx + "%");
      text.setAttribute("y", (cy + (tokenCount * 4 - 14)) + "%");
      text.setAttribute("fill", "#fff");
      text.setAttribute("font-size", "10px");
      text.setAttribute("text-anchor", "middle");
      text.setAttribute("font-family", "monospace");
      text.textContent = name.toUpperCase();
      
      g.appendChild(pulse);
      g.appendChild(circle);
      g.appendChild(text);
    }
  });
}

function renderAnalyzerTab(pane) {
  pane.innerHTML = '';
  
  const container = document.createElement('div');
  container.className = 'analyzer-container';
  
  container.innerHTML = `
    <div class="analyzer-input-area">
      <h3 style="margin-top:0; color:#fff; font-size:1.1rem; border-bottom:1px solid #222; padding-bottom: 0.5rem;">CONTINUITY SCRIPT AUDITOR</h3>
      <div style="font-size:0.8rem; color:#888; margin-bottom:0.5rem;">
        Paste your script or dialogue down below to run a real-time sanity check against the established lore rules.
      </div>
      <textarea id="analyzer-text" class="analyzer-textarea" placeholder="STAN: I'm not moving a muscle until Barb gets down here..."></textarea>
      <button class="analyzer-btn" id="run-audit-btn">RUN LORE AUDIT</button>
    </div>
    <div class="analyzer-results">
      <div style="font-size:0.8rem; color:#888; border-bottom:1px solid #222; padding-bottom: 0.5rem; margin-bottom: 0.8rem; text-transform: uppercase;">Audit Output Console</div>
      <div id="analyzer-logs">
        <div class="audit-log-line info">[CONSOLE READY] Awaiting script load...</div>
      </div>
    </div>
  `;
  
  pane.appendChild(container);
  
  document.getElementById('run-audit-btn').addEventListener('click', () => {
    const text = document.getElementById('analyzer-text').value;
    runScriptAudit(text);
  });
}

function runScriptAudit(text) {
  const logs = document.getElementById('analyzer-logs');
  if(!logs) return;
  
  logs.innerHTML = '';
  
  if(!text || text.trim() === '') {
    logs.innerHTML = `<div class="audit-log-line error">[AUDIT ERROR] Script payload is empty. Insert dialogue lines first.</div>`;
    return;
  }
  
  let lineCount = 0;
  let violationCount = 0;
  
  // Split into lines
  const lines = text.split('\n');
  
  // Calculate vulgarity count
  const vulgarWords = ["shit", "fuck", "dick", "ass", "bastard", "bitch", "damn"];
  let vulgarCount = 0;
  const words = text.toLowerCase().split(/\s+/);
  words.forEach(w => {
    const cleaned = w.replace(/[^a-z]/g, '');
    if(vulgarWords.includes(cleaned)) vulgarCount++;
  });
  
  const vulgarRatio = Math.round((vulgarCount / (words.length || 1)) * 100);
  
  // Process lore rules
  const auditLogs = [];
  
  lines.forEach((line, index) => {
    if(line.trim() === '') return;
    lineCount++;
    
    // Check speaker if line follows "SPEAKER: dialogue"
    const parts = line.split(':');
    let speaker = null;
    let dialogue = line;
    if(parts.length > 1 && parts[0].trim().toUpperCase() === parts[0].trim()) {
      speaker = parts[0].trim().toUpperCase();
      dialogue = parts.slice(1).join(':').toLowerCase();
    } else {
      dialogue = line.toLowerCase();
    }
    
    // Run checks
    LORE_VIOLATIONS.forEach(rule => {
      // Rule checks speaker match if specified
      if(rule.speaker && rule.speaker !== speaker) return;
      
      // Rule check keyword match
      if(dialogue.includes(rule.term)) {
        // If require rule check
        if(rule.require && !dialogue.includes(rule.require.toLowerCase())) {
          violationCount++;
          auditLogs.push({
            type: 'warning',
            msg: `Line ${index + 1}: ${rule.warning}`
          });
          return;
        }
        
        if(!rule.require) {
          violationCount++;
          auditLogs.push({
            type: 'warning',
            msg: `Line ${index + 1}: ${rule.warning}`
          });
        }
      }
    });
  });
  
  // Render results
  const summaryLine = document.createElement('div');
  summaryLine.className = 'audit-log-line info';
  summaryLine.innerHTML = `[AUDIT RUNNING] Parsed ${lineCount} script lines. Vulgarity-to-Lore ratio: <span style="color:#ff00ff;">${vulgarRatio}%</span>.`;
  logs.appendChild(summaryLine);
  
  if(vulgarRatio === 0 && lineCount > 0) {
    const toneWarning = document.createElement('div');
    toneWarning.className = 'audit-log-line warning';
    toneWarning.innerText = `[TONE ADVICE] Script has 0% vulgarity. Add more dark-comedy workplace flavor and corporate spite.`;
    logs.appendChild(toneWarning);
  } else if(vulgarRatio > 0) {
    const toneSuccess = document.createElement('div');
    toneSuccess.className = 'audit-log-line success';
    toneSuccess.innerText = `[TONE SUCCESS] Vulgarity-to-Lore ratio is optimal. Workplace misery levels verified.`;
    logs.appendChild(toneSuccess);
  }
  
  if(auditLogs.length === 0) {
    const successLine = document.createElement('div');
    successLine.className = 'audit-log-line success';
    successLine.innerText = `[AUDIT COMPLETE] 0 continuity conflicts found. Script matches established lore.`;
    logs.appendChild(successLine);
  } else {
    auditLogs.forEach(log => {
      const el = document.createElement('div');
      el.className = `audit-log-line ${log.type}`;
      el.innerText = log.msg;
      logs.appendChild(el);
    });
    
    const failLine = document.createElement('div');
    failLine.className = 'audit-log-line error';
    failLine.innerText = `[AUDIT COMPLETE] ${violationCount} continuity conflicts detected. Correction advised.`;
    logs.appendChild(failLine);
  }
}

window.__closeContinuity = () => {
  state.view = 'home';
  render();
};

render()
