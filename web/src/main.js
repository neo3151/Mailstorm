import './style.css'

const app = document.querySelector('#app')

// State
const state = {
  view: 'home', // 'home' | 'reader'
  currentEpisode: 1,
  episodes: [
    { id: 1, title: "Episode 1: The New Hire" },
    { id: 2, title: "Episode 2: The Algorithm's Gaze" },
    { id: 3, title: "Episode 3: The Route" },
    { id: 4, title: "Episode 4: The Audit" },
    { id: 5, title: "Episode 5: Dead Letter" },
    { id: 6, title: "Episode 6: The Strike" },
    { id: 7, title: "Episode 7: Black Friday" },
    { id: 8, title: "Episode 8: The Mandate (Season Finale)" }
  ]
}

// Router
function render() {
  app.innerHTML = ''
  if (state.view === 'home') {
    renderHome()
  } else if (state.view === 'reader') {
    renderReader()
  }
}

// Views
function renderHome() {
  const container = document.createElement('div')
  container.className = 'container'

  container.innerHTML = `
    <header>
      <h1>Mailstorm</h1>
      <p style="color: var(--color-primary); font-weight: bold; letter-spacing: 2px;">THE CORPORATE BATTLE MANGA</p>
    </header>
    <div class="hero">
      <img src="/logo.png" alt="Mailstorm Logo" style="max-width: 80%; border-radius: 10px; box-shadow: 0 0 20px rgba(0,0,0,0.5);">
      <p style="max-width: 600px; margin: 2rem auto; line-height: 1.6; font-size: 1.1rem;">
        In a world where corporate stress manifests as physical power, one man dares to do the bare minimum.
        Join <strong>Stan</strong>, <strong>Heather</strong>, and the crew of <strong>Omni-Corp Logistics</strong>.
      </p>
      
      <div class="episode-list" style="display: flex; flex-direction: column; gap: 1rem; margin-top: 2rem;">
        <h3>Select an Episode:</h3>
        ${state.episodes.map(ep => `
          <button onclick="window.startEpisode(${ep.id})" style="width: 100%; max-width: 400px; margin: 0 auto;">
            ${ep.title}
          </button>
        `).join('')}
      </div>
    </div>
  `

  app.appendChild(container)

  // Expose function to window for the onclick handlers
  window.startEpisode = (epId) => {
    state.currentEpisode = epId
    state.view = 'reader'
    render()
  }
}

async function renderReader() {
  const container = document.createElement('div')
  container.className = 'comic-viewer'

  // Header/Nav
  const header = document.createElement('div')
  header.style.padding = '1rem'
  header.style.background = '#000'
  header.style.position = 'sticky'
  header.style.top = '0'
  header.style.zIndex = '100'
  header.style.display = 'flex'
  header.style.justifyContent = 'space-between'
  header.style.alignItems = 'center'

  const currentEpTitle = state.episodes.find(e => e.id === state.currentEpisode)?.title || `Episode ${state.currentEpisode}`

  header.innerHTML = `
    <button id="home-btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Home</button>
    <span style="font-weight: bold;">${currentEpTitle}</span>
    <div style="width: 60px;"></div> <!-- Spacer -->
  `

  container.appendChild(header)

  // Load Pages
  try {
    const response = await fetch(`/comics/episode_${state.currentEpisode}/manifest.json`)
    const data = await response.json()

    data.pages.forEach(page => {
      const filename = typeof page === 'string' ? page : page.file
      const caption = typeof page === 'object' ? page.caption : null

      const wrapper = document.createElement('div')
      wrapper.style.marginBottom = '0.5rem'

      const img = document.createElement('img')
      img.src = `/comics/episode_${state.currentEpisode}/${filename}`
      img.className = 'comic-panel'
      img.loading = 'lazy'
      wrapper.appendChild(img)

      if (caption) {
        const cap = document.createElement('p')
        cap.textContent = caption
        cap.style.cssText = 'text-align:center;color:#aaa;font-style:italic;font-size:0.9rem;padding:0.25rem 1rem;margin:0;'
        wrapper.appendChild(cap)
      }

      container.appendChild(wrapper)
    })

    // Footer Nav
    const controls = document.createElement('div')
    controls.className = 'controls'

    const nextEp = state.currentEpisode + 1
    const hasNext = state.episodes.find(e => e.id === nextEp)

    controls.innerHTML = `
      <button onclick="window.startEpisode(${state.currentEpisode - 1})" ${state.currentEpisode === 1 ? 'disabled' : ''}>Prev Episode</button>
      <button onclick="window.startEpisode(${nextEp})" ${!hasNext ? 'disabled' : ''}>Next Episode</button>
    `
    container.appendChild(controls)

  } catch (e) {
    container.innerHTML += `<p style="text-align: center; padding: 2rem; color: red;">Error loading comic: ${e.message}</p>`
  }

  app.appendChild(container)

  document.querySelector('#home-btn').addEventListener('click', () => {
    state.view = 'home'
    render()
  })
}

// Init
render()
