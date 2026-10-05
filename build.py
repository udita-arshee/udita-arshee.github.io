"""Generate the static academic site. Run with: python build.py"""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent
EMAIL = "uditrahman2001@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/udita-arshee-65b411240/"
GITHUB = "https://github.com/udita-arshee"


def network_figure(label="Sensor network with energy-aware control"):
    return f"""<svg class="research-art" viewBox="0 0 560 280" role="img" aria-label="{escape(label)}" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="netbg" x2="1" y2="1"><stop stop-color="#eef6f7"/><stop offset="1" stop-color="#f8fbf8"/></linearGradient></defs>
      <rect x="1" y="1" width="558" height="278" rx="15" fill="url(#netbg)" stroke="#dce9e7"/>
      <g fill="none" stroke="#a8c9cb" stroke-width="2"><path d="M95 65 178 103 263 56 353 100 452 61M95 65 104 183 196 210 178 103 263 56 278 177 353 100 452 61 457 202 370 216 278 177 196 210 104 183M178 103 278 177 353 100M263 56 353 100 370 216"/></g>
      <g fill="#fff" stroke="#2f7890" stroke-width="3"><circle cx="95" cy="65" r="12"/><circle cx="178" cy="103" r="12"/><circle cx="263" cy="56" r="12"/><circle cx="353" cy="100" r="12"/><circle cx="452" cy="61" r="12"/><circle cx="104" cy="183" r="12"/><circle cx="196" cy="210" r="12"/><circle cx="278" cy="177" r="12"/><circle cx="370" cy="216" r="12"/><circle cx="457" cy="202" r="12"/></g>
      <circle cx="278" cy="177" r="27" fill="#2f7890" opacity=".13"/><circle cx="278" cy="177" r="12" fill="#2f7890"/>
      <g fill="#24566a" font-family="Inter,Arial,sans-serif" font-size="12" font-weight="600"><text x="22" y="250">SENSOR NODES</text><text x="397" y="250">ENERGY-AWARE ROUTING</text></g>
    </svg>"""


def hierarchy_figure():
    return """<svg class="research-art" viewBox="0 0 560 280" role="img" aria-label="Hierarchical network controller with strategic and tactical layers" xmlns="http://www.w3.org/2000/svg">
      <rect x="1" y="1" width="558" height="278" rx="15" fill="#f5f9f8" stroke="#dce9e7"/>
      <path d="M280 88V118M280 176V199M162 199V185H398V199" fill="none" stroke="#9dbfc5" stroke-width="3"/>
      <g font-family="Inter,Arial,sans-serif" text-anchor="middle">
        <rect x="174" y="35" width="212" height="54" rx="10" fill="#173b52"/><text x="280" y="58" fill="#fff" font-size="15" font-weight="700">Strategic control</text><text x="280" y="76" fill="#c6e7e8" font-size="11">event-driven PPO</text>
        <rect x="174" y="120" width="212" height="56" rx="10" fill="#287788"/><text x="280" y="143" fill="#fff" font-size="15" font-weight="700">Tactical decisions</text><text x="280" y="161" fill="#d9f0ef" font-size="11">shared DDQN agents</text>
        <rect x="72" y="199" width="180" height="51" rx="10" fill="#e5f1ef" stroke="#9dbfc5"/><text x="162" y="230" fill="#24566a" font-size="13" font-weight="600">Region A · energy budget</text>
        <rect x="308" y="199" width="180" height="51" rx="10" fill="#e5f1ef" stroke="#9dbfc5"/><text x="398" y="230" fill="#24566a" font-size="13" font-weight="600">Region B · energy budget</text>
      </g>
    </svg>"""


def page(title, desc, active, body):
    nav = [("Home", "index.html"), ("Research", "research.html"), ("Publications", "publications.html"),
           ("Projects", "projects.html"), ("Education", "education.html")]
    links = "".join(f'<a href="{url}"' + (' class="active" aria-current="page"' if label == active else "")
                    + f'>{label}</a>' for label, url in nav)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#173b52">
  <meta name="description" content="{escape(desc, quote=True)}">
  <title>{escape(title)} · Udita Rahman Arshee</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=Source+Serif+4:wght@500;600;700&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
</head>
<body>
  <div class="focus-bar">Wireless Sensor Networks · IoT · Learning-Based Optimization</div>
  <header class="site-header"><div class="wrap header-row">
    <a class="brand" href="index.html" aria-label="Udita Rahman Arshee home">URA</a>
    <nav aria-label="Primary navigation">{links}</nav>
  </div></header>
  <main class="wrap">{body}</main>
  <footer class="site-footer"><div class="wrap footer-grid">
    <div><strong>© 2026 Udita Rahman Arshee</strong><span>Wireless networks research · Khulna, Bangladesh</span></div>
    <div class="footer-links"><a href="mailto:{EMAIL}">✉ Email</a><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a><a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a></div>
  </div></footer>
</body>
</html>
"""


home = f"""
<section class="hero">
  <div class="portrait-frame"><div class="portrait-monogram" role="img" aria-label="Udita Rahman Arshee monogram">URA</div></div>
  <div>
    <p class="kicker">ECE Graduate · KUET</p>
    <h1>Udita Rahman Arshee</h1>
    <p class="role">Wireless Sensor Networks · IoT · Network Optimization</p>
    <p>I am an Electronics and Communication Engineering graduate from Khulna University of Engineering &amp; Technology (KUET). I study energy-efficient wireless sensor networks, network resource management, and intelligent decision-making for connected systems.</p>
    <p>My undergraduate thesis explores how event-driven hierarchical reinforcement learning and spatial energy constraints can balance network lifetime, energy fairness, latency, and packet delivery.</p>
    <div class="identity-links" aria-label="Contact and academic profiles">
      <a href="mailto:{EMAIL}"><span class="contact-icon">✉</span>Email</a>
      <a href="{LINKEDIN}" target="_blank" rel="noopener"><span class="contact-icon text-icon">in</span>LinkedIn</a>
      <a href="{GITHUB}" target="_blank" rel="noopener"><span class="contact-icon text-icon">GH</span>GitHub</a>
    </div>
  </div>
</section>
<section>
  <div class="section-head split-head"><div><p class="kicker">Featured Research Directions</p><h2>Wireless Networks &amp; Intelligent Control</h2></div><a class="section-link" href="research.html">Explore all research →</a></div>
  <div class="featured-grid">
    <article class="feature-card">
      <div class="feature-visual">{network_figure()}</div>
      <div class="feature-body"><div class="status-row compact-status"><span class="badge submitted">Thesis Research</span></div><p class="kicker">Wireless Sensor Networks</p><h3>Energy Optimization in Sensor Networks</h3><p>A spatially constrained framework for extending network lifetime while accounting for regional energy balance and communication quality.</p><a href="research.html#sced-hrl">Explore research →</a></div>
    </article>
    <article class="feature-card">
      <div class="feature-visual">{hierarchy_figure()}</div>
      <div class="feature-body"><div class="status-row compact-status"><span class="badge submitted">Manuscript Submitted</span></div><p class="kicker">Learning-Based Network Control</p><h3>Event-Driven Hierarchical RL</h3><p>Strategic PPO and tactical DDQN decisions respond to network conditions while respecting spatial budgets and feasible actions.</p><a href="research.html#control">Explore research →</a></div>
    </article>
  </div>
</section>
<section>
  <div class="section-head"><p class="kicker">Academic Snapshot</p><h2>Highlights</h2></div>
  <div class="highlight-box">
    <div class="highlight-item"><strong>3.26 / 4.00</strong><span>CGPA</span></div>
    <div class="highlight-item"><strong>KUET</strong><span>B.Sc. in Electronics &amp; Communication Engineering</span></div>
    <div class="highlight-item"><strong>2026</strong><span>Graduation year</span></div>
    <div class="highlight-item"><strong>1</strong><span>Peer-reviewed conference publication</span></div>
    <div class="highlight-item"><strong>SCED-HRL</strong><span>Undergraduate thesis on WSN energy optimization</span></div>
    <div class="highlight-item"><strong>Research Society</strong><span>Department Executive, KUET</span></div>
  </div>
</section>
<section id="news">
  <div class="section-head split-head"><div><p class="kicker">Research Activity</p><h2>News</h2></div><a class="section-link" href="publications.html">View publications →</a></div>
  <div class="news-box">
    <div class="timeline-item"><span class="timeline-dot" aria-hidden="true"></span><time>2026</time><p><strong>WSN research.</strong> SCED-HRL manuscript submitted to ICEEICT 2027.</p></div>
    <div class="timeline-item"><span class="timeline-dot" aria-hidden="true"></span><time>2026</time><p><strong>Publication.</strong> Coauthored <em>SenseStick</em> published at IEEE BECITHCON 2026.</p></div>
    <div class="timeline-item"><span class="timeline-dot" aria-hidden="true"></span><time>2025</time><p><strong>Recognition.</strong> Champion in Technical Writing at EUREKA S/1, KUET Research Society.</p></div>
  </div>
</section>
"""

research = f"""
<div class="page-intro"><p class="kicker">Research</p><h1>Energy-Aware Wireless Systems</h1><p class="section-intro">My work connects wireless sensor network performance with constrained, learning-based resource allocation. The central question is how adaptive decisions can preserve scarce energy without neglecting latency, reliability, or fairness.</p></div>
<section id="sced-hrl">
  <div class="research-card"><div class="research-visual">{network_figure()}<span>Sensor network topology and energy-aware control (conceptual illustration)</span></div><div class="research-copy">
    <div class="status-row"><span class="badge">Undergraduate Thesis</span><span class="badge submitted">Manuscript Submitted</span></div>
    <p class="meta">Wireless Sensor Networks · Energy Optimization</p>
    <h2>Spatially-Constrained Event-Driven Hierarchical Deep Reinforcement Learning (SCED-HRL)</h2>
    <p>My B.Sc. thesis develops a hierarchical controller for energy optimization in wireless sensor networks. It combines a strategic, event-driven PPO layer with parameter-shared DDQN tactical agents and spatial energy budgeting.</p>
    <div class="research-question"><strong>Research goal:</strong> improve network lifetime and regional energy balance while tracking latency and packet delivery.</div>
    <ul><li>Feasible actions and regional budgets help prevent short-term gains from exhausting parts of the network.</li><li>Evaluation uses Intel Berkeley sensor data-derived and synthetic traffic alongside baseline control strategies.</li></ul>
  </div></div>
</section>
<section id="control">
  <div class="research-card"><div class="research-visual">{hierarchy_figure()}<span>Strategic and tactical layers (conceptual illustration)</span></div><div class="research-copy">
    <p class="meta">Hierarchical Reinforcement Learning</p><h2>Adaptive Control Under Network Constraints</h2>
    <p>Event-driven strategic decisions and shared tactical policies respond to changes in network conditions. Spatial energy constraints and action masking keep decisions tied to feasible deployment behavior.</p>
    <ul><li>Strategic layer: event-driven PPO.</li><li>Tactical layer: parameter-shared DDQN agents.</li><li>Evaluation dimensions: lifetime, fairness, latency, and packet delivery.</li></ul>
  </div></div>
</section>
<section><div class="section-head"><p class="kicker">Related Interests</p><h2>Beyond the Thesis</h2></div>
  <div class="grid-2">
    <div class="card"><h3>IoT &amp; Wireless Communications</h3><p>Connected sensor systems, communication reliability, and resource-aware design across changing traffic and deployment conditions.</p></div>
    <div class="card"><h3>Learning for Resource Management</h3><p>Reinforcement learning and optimization methods evaluated through practical network outcomes and feasibility constraints.</p></div>
  </div>
</section>
"""

publications = """
<div class="page-intro"><p class="kicker">Research Output</p><h1>Publications &amp; Manuscripts</h1><p class="section-intro">Peer-reviewed work and manuscripts are listed separately. Submission and revision do not imply acceptance.</p></div>
<section><div class="section-head"><p class="kicker">Peer Reviewed</p><h2>Conference Publication</h2></div>
  <div class="publication-stack"><article class="publication-card published-card"><div class="publication-topline"><span class="pub-type">Conference paper · 2026</span><div class="status-row"><span class="badge">Published</span></div></div><h3>SenseStick: A Bangla-English Edge-AI Cane for Road Safety and Biomedical Reliability Monitoring</h3><p class="byline">A. R. Aditta, P. K. Das, <strong>U. R. Arshee</strong>, A. B. M. Aowlad Hossain</p><p class="venue">IEEE BECITHCON 2026</p></article></div>
</section>
<section class="manuscript-head"><div class="section-head"><p class="kicker">Current Work</p><h2>Submitted Manuscripts</h2></div>
  <div class="publication-stack">
    <article class="publication-card manuscript-card"><div class="publication-topline"><span class="pub-type">Wireless Sensor Networks</span><span class="badge submitted">Submitted</span></div><h3>Event-Driven Hierarchical Deep Reinforcement Learning with Spatial Energy Constraints for Wireless Sensor Network Optimization</h3><p class="byline"><strong>U. R. Arshee</strong>, M. Hossen, S. I. Mumu</p><p class="venue">ICEEICT 2027 · submitted</p></article>
    <article class="publication-card manuscript-card"><div class="publication-topline"><span class="pub-type">WSN Security</span><span class="badge submitted">Submitted</span></div><h3>THRIFT: Selective Graph-Teacher Knowledge Transfer for Federated Intrusion Detection in Wireless Sensor Networks</h3><p class="byline">S. I. Mumu, M. Hossen, <strong>U. R. Arshee</strong></p><p class="venue">ICEEICT 2027 · submitted</p></article>
    <article class="publication-card manuscript-card"><div class="publication-topline"><span class="pub-type">Industrial WSN</span><span class="badge submitted">Submitted</span></div><h3>Adaptive PSO-Weighted Grey Wolf Optimized Deep-Q Network Framework for Balancing Energy Consumption and Anomaly Detection Performance in Industrial Wireless Sensor Networks</h3><p class="byline">Most. U. Jannat, <strong>U. R. Arshee</strong>, M. S. Tanvir, D. Aich, A. K. M. B. Haque, X. Xu, G. Muhammad</p><p class="venue">IEEE Internet of Things Journal · submitted</p></article>
    <article class="publication-card manuscript-card"><div class="publication-topline"><span class="pub-type">Smart Cities</span><span class="badge submitted">Submitted</span></div><h3>Deployment of Smart City Concept: Components, Architecture, Applications, Security Issues and Future Directions</h3><p class="byline">A. K. M. B. Haque, B. Bhushan, Most. U. Jannat, <strong>U. R. Arshee</strong>, P. Bhattacharya</p><p class="venue">Manuscript submitted, 2026</p></article>
  </div>
</section>
<section><div class="section-head"><p class="kicker">In Revision</p><h2>Journal Manuscript</h2></div>
  <div class="publication-stack"><article class="publication-card manuscript-card"><div class="publication-topline"><span class="pub-type">Bioinformatics &amp; Deep Learning</span><span class="badge revision">Under Revision</span></div><h3>Transformer-Based Modeling of DNA Enhancers: A Controlled Evaluation of DNABERT and Longformer for Identification and Strength Prediction</h3><p class="byline">A. R. Aditta, <strong>U. R. Arshee</strong>, S. M. R. Islam, N. Taaha</p><p class="venue">Under revision for journal resubmission</p></article></div>
</section>
"""

projects = """
<div class="page-intro"><p class="kicker">Selected Work</p><h1>Projects &amp; Technical Experience</h1><p class="section-intro">Selected projects spanning wireless communication, sensing, RF analysis, and connected hardware.</p></div>
<section><div class="project-grid">
  <article class="project-card featured-project"><span class="project-number">01</span><p class="kicker">Network Research</p><h2>SCED-HRL for Wireless Sensor Networks</h2><p>Developed a hierarchical learning framework for WSN energy optimization, with regional budgets and feasibility constraints.</p><p class="project-meta">PPO · DDQN · Python · Intel Berkeley data-derived traffic</p><a href="research.html#sced-hrl">Research details →</a></article>
  <article class="project-card"><span class="project-number">02</span><p class="kicker">Wireless Systems</p><h2>Satellite Link Performance Analysis</h2><p>Studied link performance across frequency, path loss, and signal-to-noise conditions.</p><p class="project-meta">Wireless communication · Link analysis</p></article>
  <article class="project-card"><span class="project-number">03</span><p class="kicker">RF &amp; Antennas</p><h2>Dual-Band Microstrip Antenna</h2><p>Simulated a microstrip antenna operating around 3 GHz and 7 GHz and examined the frequency response.</p><p class="project-meta">Antenna simulation · RF analysis</p></article>
  <article class="project-card"><span class="project-number">04</span><p class="kicker">IoT Prototype</p><h2>RFID-Based Smart Parking</h2><p>Built a connected parking prototype using RFID, ESP8266, Arduino, and Blynk.</p><p class="project-meta">RFID · ESP8266 · Arduino · IoT</p></article>
</div></section>
<section><div class="section-head"><p class="kicker">Methods &amp; Tools</p><h2>Technical Toolkit</h2></div><div class="tool-grid">
  <div class="panel"><span class="tool-index">01</span><h3>Programming &amp; Analysis</h3><p>Python, C, MATLAB, SQL, MATLAB/Simulink.</p></div>
  <div class="panel"><span class="tool-index">02</span><h3>Learning Methods</h3><p>PyTorch, TensorFlow/Keras, scikit-learn, XGBoost.</p></div>
  <div class="panel"><span class="tool-index">03</span><h3>Simulation &amp; Networking</h3><p>Multisim, Cisco Packet Tracer, wireless communication laboratory work.</p></div>
  <div class="panel"><span class="tool-index">04</span><h3>Embedded Platforms</h3><p>ESP32, ESP8266, Raspberry Pi, Arduino.</p></div>
</div></section>
"""

education = """
<div class="page-intro"><p class="kicker">Academic Profile</p><h1>Education &amp; Background</h1><p class="section-intro">Engineering education, research involvement, and selected recognition.</p></div>
<section><div class="section-head"><p class="kicker">Education</p><h2>Khulna University of Engineering &amp; Technology</h2></div>
  <div class="edu-box"><p class="degree">B.Sc. in Electronics and Communication Engineering · 2026</p><p>Department of Electronics and Communication Engineering, KUET, Bangladesh.</p>
    <div class="highlight-box">
      <div class="highlight-item"><strong>3.26 / 4.00</strong><span>CGPA</span></div>
      <div class="highlight-item"><strong>3.65 · 3.74<br>3.65 · 3.70</strong><span>Final four term GPAs</span></div>
      <div class="highlight-item"><strong>2026</strong><span>Graduation</span></div>
    </div>
    <p class="callout"><strong>Undergraduate thesis:</strong> Spatially-Constrained Event-Driven Hierarchical Deep Reinforcement Learning (SCED-HRL) Framework for Energy Optimization in Wireless Sensor Networks.</p>
  </div>
</section>
<section><div class="section-head"><p class="kicker">Leadership</p><h2>Research Community</h2></div><div class="experience-list">
  <div class="experience-row highlight-row"><span class="experience-date">KUET Research Society</span><div><h3>Department Executive</h3><p>Engaged with the research community through department-level activities and student collaboration.</p></div></div>
  <div class="experience-row"><span class="experience-date">SheSTEM</span><div><h3>Campus Ambassador</h3><p>Supported student engagement with STEM opportunities and initiatives.</p></div></div>
</div></section>
<section><div class="section-head"><p class="kicker">Recognition</p><h2>Selected Award</h2></div><div class="card honor-card"><h3>Champion · Technical Writing</h3><p>EUREKA S/1, KUET Research Society · 2025.</p></div></section>
"""

pages = {
    "index.html": page("Home", "Academic homepage of Udita Rahman Arshee: wireless sensor networks, IoT and energy-efficient intelligent communication systems.", "Home", home),
    "research.html": page("Research", "Research by Udita Rahman Arshee on energy-efficient wireless sensor networks and hierarchical reinforcement learning.", "Research", research),
    "publications.html": page("Publications", "Peer-reviewed publication and submitted or under-revision manuscripts by Udita Rahman Arshee.", "Publications", publications),
    "projects.html": page("Projects", "Selected wireless communication, antenna, IoT and sensor network projects by Udita Rahman Arshee.", "Projects", projects),
    "education.html": page("Education", "Education, leadership and recognition of Udita Rahman Arshee, KUET ECE graduate.", "Education", education),
}
for filename, content in pages.items():
    (OUT / filename).write_text(content, encoding="utf-8")
print("Generated", ", ".join(pages))
