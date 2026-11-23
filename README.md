# ImportNow — Direct China to India Import Platform

A complete, high-fidelity replication of the **ImportNow** concept website ([https://importnow-concept.vercel.app/#home](https://importnow-concept.vercel.app/#home)), built as part of the screening assignment for the **AI Executive** role at **ImportNow**.

---

## 🚀 Live Demo & Repository
- **Live Concept Deployment**: Ready for 1-click deployment on [Vercel](https://vercel.com), [Netlify](https://netlify.com), or [GitHub Pages](https://pages.github.com).
- **Source Code Repository**: Clean vanilla modern HTML5, CSS3, ES modules, and Three.js r160 WebGL scenes with zero npm build step required.

---

## 🏗️ Architecture & Tech Stack

The platform is engineered using modern web standards without heavy frameworks, achieving near-instant first contentful paint (FCP) and optimal 60fps WebGL rendering across desktop and mobile devices:

| Layer | Technologies & Specifications |
|---|---|
| **Markup & Semantics** | HTML5 Semantic standard (`<header>`, `<section>`, `<article>`, `<canvas>`, `<details>`, `<footer>`) |
| **Styling & Design System** | Modern CSS3 (Custom properties, grid/flexbox, backdrop filters, CSS 3D transforms, clip-path image wipes) |
| **Typography** | Google Fonts (`Sora` 400/600/700/800 for bold numeric headings, `Inter` 400/500/600 for high-legibility body) |
| **3D Graphics & Shaders** | **Three.js r160** via native browser Import Maps, `three/addons/objects/Water.js`, `three/addons/objects/Sky.js` |
| **Data Engine & CMS** | Relational in-memory client database (`assets/posts.js`) with 8 full-length technical articles |
| **Interactive UI Engine** | Custom lightweight event & animation runtime (`assets/site.js`) |

---

## ✨ Key Features & Interactive Components

### 1. Interactive 3D Trade Route Globe (`assets/globe.js`)
- **Realistic Atmospheric Earth**: Dotted landmasses on a 3D sphere rendered with custom atmosphere rim glow and `ACESFilmicToneMapping`.
- **Active Trade Routes**: Quadratic Bezier curves connecting Chinese manufacturing hubs (**Shanghai**, **Yiwu**, **Guangzhou**) to Indian ports (**Nhava Sheva**, **Chennai**, **Hyderabad**).
- **Pulsating Particles & Screen Projection**: Mathematical unprojection of 3D globe coordinates into 2D DOM badges with country flags and tooltips.
- **Natural Interaction**: Smooth inertia-based drag rotation and ambient auto-drift.

### 2. Scroll-Driven 700vh Ocean Voyage Simulation (`assets/voyage.js`)
- **Procedural Ocean & Sky**: Real-time water wave displacement using normal maps (`waternormals.jpg`) with sun glitter reflection and physical Rayleigh/Mie atmospheric scattering.
- **Detailed 3D Container Vessel**: Procedural container ship with bulbous bow, transom stern, deckhouse bridge with wings, rotating radar, lifeboats, and stacked multi-colored containers with branded "IMPORTNOW" livery.
- **Working STS Port Cranes**: Working harbor gantry cranes with trolleys, spreader beams, and cables dynamically loading containers in Shanghai and unloading them in Chennai.
- **Dynamic Milestones**: 6 synchronized journey checkpoints tracking cargo progress from Day 0 to Day 30+ with real-time ship wake and side foam.

### 3. Knowledge Hub & Dynamic Blog Engine (`blog.html`, `post.html`, `assets/posts.js`)
- **Search & Filter**: Real-time instant search input + category tab filtering (`All`, `Import guides`, `Wholesale markets`, `Product guides`, `Business ideas`, `China trips`, `Shipping`, `Customs`).
- **Pagination**: 6 articles per page with smooth scroll reset.
- **Dynamic Single Post Reader**: Auto-generated Table of Contents (TOC), reading time estimation, category badge, and social sharing to WhatsApp, LinkedIn, and X.

### 4. Interactive UI & Lead Generation Engine (`assets/site.js`)
- **3D Perspective Card Tilt & Glare**: Dynamic `--mx` and `--my` mouse-tracking spotlight gradient effect on all service and category cards.
- **Interactive Chinese Business License Plaque**: 3D rotated plaque displaying registered company details for *Shanghai Shengqiao Chain Trading Co., Ltd.*
- **WhatsApp Quote Converter**: Validates inquiry form details (Product category, quantity, budget, specifications) and encodes them into a direct WhatsApp message link (`wa.me/919989724320`).
- **Scroll Progress & Number Count-Up**: Top progress bar and smooth easing counters for business metrics.

---

## 🤖 AI Tools & Workflow Explanation

This project was built from scratch leveraging state-of-the-art agentic AI workflows:

### 1. Architectural Reverse-Engineering & Visual Inspection
- Utilized an autonomous browser subagent equipped with Playwright to perform deep visual and DOM inspection across desktop (1440×900) and mobile viewports.
- Mapped all 11 landing page sections, extracted exact typography tokens, CSS custom properties, and color palettes, and isolated the component hierarchy.

### 2. 3D WebGL & Shader Re-construction
- Extracted and analyzed the Three.js r160 shaders, water normal algorithms, and procedural geometry logic for both the global trade map and the ocean voyage.
- Reconstructed the mathematical camera choreography curves and scroll-driven timeline interpolation functions.

### 3. Modular Architecture & Optimization
- Kept the codebase zero-build, dependency-free, and standards-compliant by utilizing native browser `<script type="importmap">`, eliminating bundling overhead and enabling instant hot deployment anywhere.

---

## 📦 How to Run Locally

Because the project uses standard ES modules and modern browser Import Maps, serve it using any local static web server:

```bash
# Using Python:
python -m http.server 8000

# Or using Node.js npx:
npx serve .
```

Open `http://localhost:8000` in your browser.

---

## 🌐 1-Click Deployment

### Deploy to Vercel:
```bash
npm install -g vercel
vercel
```

### Deploy to Netlify:
```bash
npm install -g netlify-cli
netlify deploy --prod --dir=.
```

### Deploy to GitHub Pages:
Push this repository to GitHub and enable **GitHub Pages** from `Settings > Pages > Branch: main / Root`.
