const content = {
  home: `
    <section class="home-hero">
      <div class="portrait-wrap"><img class="portrait" src="../assets/arnav-goel.jpeg" alt="Arnav Goel" /></div>
      <div class="intro-copy">
        <p class="kicker">Carnegie Mellon University · Pittsburgh, PA</p>
        <h1>Hi, I am Arnav.</h1>
        <p>I am an M.S. in Machine Learning student at Carnegie Mellon University. My current work studies reliable and efficient reasoning in LLM and agentic systems.</p>
        <p>I am also an Applied Scientist Intern at AWS Agentic AI. Previously, I worked at Microsoft Research, IBM Research, and USC NLP.</p>
        <div class="inline-links"><a href="mailto:arnavgoe@cs.cmu.edu">Email</a><a href="https://scholar.google.com/citations?user=PPozs9sAAAAJ&hl=en&oi=ao" target="_blank" rel="noreferrer">Google Scholar</a><a href="https://github.com/arnav10goel" target="_blank" rel="noreferrer">GitHub</a><a href="https://www.linkedin.com/in/arnavg10/" target="_blank" rel="noreferrer">LinkedIn</a></div>
      </div>
    </section>

    <section class="research-section">
      <div class="section-label">Research</div>
      <div class="research-copy">
        <p>I build dependable ML systems where correctness matters, with emphasis on agent reliability, verification, and scalable reasoning.</p>
        <div class="interest-list">
          <article><h2>Reliable multi-agent systems</h2><p>Improving instruction following, context routing, and coordination for long-horizon enterprise workflows.</p></article>
          <article><h2>Verification and alignment</h2><p>Using autoformalization, LLM judges, and policy optimization to make model behavior more robust and auditable.</p></article>
          <article><h2>Efficient reasoning at scale</h2><p>Designing data, training, and distillation pipelines that preserve quality while drastically reducing inference cost.</p></article>
        </div>
      </div>
    </section>

    <section class="updates-section">
      <div class="section-label">Updates</div>
      <details open><summary>Recent updates <span>+</span></summary>
        <div class="updates-scroll">
          <p><time>Summer 2026</time> Applied Scientist Intern, AWS Agentic AI (Seattle).</p>
          <p><time>2026</time> HORIZON accepted to NeurIPS 2025 workshop and Findings of ACL 2026.</p>
          <p><time>2025</time> Research Engineering Intern at Microsoft Research (Extreme Classification Group).</p>
          <p><time>2025</time> Started M.S. in Machine Learning at Carnegie Mellon University (GPA 4.0).</p>
          <p><time>2024</time> First-author publications at ICLR and INTERSPEECH tracks on multilingual and cultural LLM behavior.</p>
        </div>
      </details>
    </section>
  `,
  cv: `
    <section class="page-head"><p class="kicker">Curriculum vitae</p><h1>Experience and education</h1><p class="page-lede">Download: <a href="../assets/Arnav_Goel_CV.pdf" target="_blank" rel="noreferrer">1-page resume</a> · <a href="../assets/Arnav_Goel_CV_2page.pdf" target="_blank" rel="noreferrer">2-page CV</a></p></section>
    <section class="cv-section"><h2>Education</h2><div class="cv-entry"><div class="cv-date">2025-2026</div><div><h3>Carnegie Mellon University</h3><p>M.S. in Machine Learning, School of Computer Science</p><p class="muted">GPA: 4.0. Ongoing research on RL for efficient LLM and agentic reasoning with Daniel Fried and Sean Welleck.</p></div></div><div class="cv-entry"><div class="cv-date">2021-2025</div><div><h3>IIIT Delhi</h3><p>B.Tech. in Computer Science and AI</p><p class="muted">CGPA: 9.50/10.00 (Class Rank: 2).</p></div></div></section>
    <section class="cv-section"><h2>Work experience</h2><div class="cv-entry"><div class="cv-date">May-Aug 2026</div><div><h3>Amazon Web Services</h3><p>Applied Scientist Intern, AWS Agentic AI</p><p class="muted">Built context routing and verification pipelines to improve reliability in multi-agent enterprise tasks.</p></div></div><div class="cv-entry"><div class="cv-date">Jan-Jul 2025</div><div><h3>Microsoft Research</h3><p>Research Engineering Intern</p><p class="muted">Built HORIZON, improved Bing Ads recommendation reasoning, and led migration from GPT-4o to efficient 8B models with 100x inference speedup.</p></div></div><div class="cv-entry"><div class="cv-date">May-Oct 2023</div><div><h3>IBM Research</h3><p>Research Engineering Intern</p><p class="muted">Developed LLM guardrails for topic filtering, toxicity detection, and hallucination grounding workflows.</p></div></div></section>
    <section class="cv-section"><h2>Research experience</h2><div class="cv-entry"><div class="cv-date">2024-2025</div><div><h3>University of Southern California</h3><p>IUSSTF-Viterbi ML Research Intern</p><p class="muted">Designed MEMOED for attributing cultural LLM behavior to memorization versus generalization; scaled analysis to billions of documents.</p></div></div><div class="cv-entry"><div class="cv-date">2023-2024</div><div><h3>Infosys Center for AI, IIIT Delhi</h3><p>Undergraduate Researcher</p><p class="muted">Published work on multilingual speech transfer and speaker emotion recognition.</p></div></div></section>
    <section class="cv-section"><h2>Selected achievements</h2><ul class="plain-list"><li>Google DeepMind Research Symposium 2025 - selected among top 150 undergraduates in India.</li><li>Amazon ML Challenge 2024 - ranked 6th out of 20,000+ teams in India.</li><li>IUSSTF-Viterbi India Program 2024 - selected among 15 scholars nationwide.</li><li>MITACS Globalink Research Scholarship 2024.</li></ul></section>
  `,
  publications: `
    <section class="page-head"><p class="kicker">Publications</p><h1>Research papers</h1><p class="page-lede">For the most up-to-date full list, see <a href="https://scholar.google.com/citations?user=PPozs9sAAAAJ&hl=en&oi=ao" target="_blank" rel="noreferrer">Google Scholar</a>.</p></section>
    <div class="pub-list">
      <article class="pub"><div class="pub-year">2026</div><div><h2>HORIZON: A Benchmark for In-the-wild User Behaviour Modeling</h2><p>First/co-first author</p><p class="venue">NeurIPS 2025 Workshop, Findings of ACL 2026</p></div></article>
      <article class="pub"><div class="pub-year">2025</div><div><h2>Attributing Culture-Conditioned LLM Generations to Pretraining Corpora</h2><p>First/co-first author</p><p class="venue">ICLR 2025</p></div></article>
      <article class="pub"><div class="pub-year">2025</div><div><h2>Optimizing Vision Language Models for Scientific VQA through Caption-Aware Supervised Training</h2><p>First/co-first author</p><p class="venue">ACM MM 2025</p></div></article>
      <article class="pub"><div class="pub-year">2024</div><div><h2>Exploring Multilingual Speaker Emotion Recognition: Leveraging Co-Attention Cues in Multitask Learning</h2><p>First/co-first author</p><p class="venue">INTERSPEECH 2024</p></div></article>
      <article class="pub"><div class="pub-year">2024</div><div><h2>Multilingual Prosody Transfer: Comparing Supervised and Transfer Learning</h2><p>First/co-first author</p><p class="venue">ICLR 2024</p></div></article>
      <article class="pub"><div class="pub-year">2024</div><div><h2>LLMGuard: Guarding Against Unsafe LLM Behavior</h2><p>First/co-first author</p><p class="venue">AAAI 2024</p></div></article>
    </div>
  `,
  blog: `
    <section class="page-head"><p class="kicker">Blog</p><h1>Notes and writing</h1><p class="page-lede">Short notes on model reliability, efficient reasoning, and ML systems practice.</p></section>
    <article class="blog-post featured-post"><p class="post-meta">Draft</p><h2>What makes an LLM agent reliable?</h2><p>A running note on coordination failures, verifier design, and what practical reliability should mean in real deployments.</p><a class="read-more" href="#">Read draft -></a></article>
    <article class="blog-post"><p class="post-meta">Coming soon</p><h2>Distilling reasoning into efficient small models</h2><p>Lessons from model migration work and where quality drops first.</p></article>
    <article class="blog-post"><p class="post-meta">Coming soon</p><h2>Benchmarks that reflect long-horizon behavior</h2><p>Why realistic user history and retrieval setup can change model ranking conclusions.</p></article>
  `
};

const activePage = () => (location.hash.slice(1) || "home");

function render() {
  const page = activePage();
  const resolved = Object.prototype.hasOwnProperty.call(content, page) ? page : "home";
  document.querySelector("#page-content").innerHTML = content[resolved];
  document.querySelectorAll("[data-page]").forEach((link) => link.classList.toggle("active", link.dataset.page === resolved));
  document.title = `${document.body.dataset.name} - ${resolved[0].toUpperCase()}${resolved.slice(1)}`;
  window.scrollTo({ top: 0, behavior: "instant" });
}

document.querySelector("#site").innerHTML = `
  <header class="site-header"><a class="name" href="#home">Arnav Goel</a><nav aria-label="Primary navigation"><a data-page="home" href="#home">Home</a><a data-page="cv" href="#cv">CV</a><a data-page="publications" href="#publications">Publications</a><a data-page="blog" href="#blog">Blog</a></nav></header>
  <main id="page-content"></main>
  <footer><span>© ${new Date().getFullYear()} Arnav Goel</span><span>ML research · CMU</span></footer>`;
window.addEventListener("hashchange", render);
render();
