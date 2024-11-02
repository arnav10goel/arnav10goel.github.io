---
permalink: /
title: "Arnav Goel"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hi! I am Arnav, a final year undergraduate student at IIIT Delhi, where I am pursuing a B.Tech in Computer Science and Artificial Intelligence. Currently, I am working as a Research Intern at the [INK-Lab](https://inklab.usc.edu/index.html), under the guidance of [Dr. Xiang Ren](https://www.seanre.com/). In parallel, I serve as a Research Assistant at McGill University and MILA, supervised by [Dr. Jackie Chi Kit Cheung](https://www.cs.mcgill.ca/~jcheung/). My work here includes a collaboration with the FATE Team at Microsoft Research Montreal. In the past, I have been fortunate to have work with [Dr. Sameep Mehta](https://research.ibm.com/people/sameep-mehta) and [Dr. Nishtha Madaan](https://nishthaa.github.io/) from IBM Research India and [Dr. Anubha Gupta](https://www.iiitd.ac.in/anubha) and [Dr. Rajiv Ratn Shah](https://midas.iiitd.ac.in/) at IIIT Delhi. 

My research interests vary across language models, machine learning and speech processing. I am currently interested in investigating trustworthiness and fairness in LLMs with 

News
------
- June 2024: Paper titled "Exploring Multilingual Unseen Speaker Emotion Recognition: Leveraging Co-Attention Cues in Multitask Learning" accepted at INTERSPEECH 2024. This work was done as part of my undergraduate thesis. See you in Greece!
- May 2024: Started my internship at the INK-Lab in the USC NLP Group. Hit me up if you wanna meet :)
- March 2024: Thrilled to share that I have been selected as one of the **15 IUSSTF-Viterbi Research Scholars** from all over India. Looking forward to a great summer in LA.
- February 2024: 2 papers on speech processing and prosody transfer accepted at the Tiny Track at ICLR 2024!
- November 2023: Paper titled "LLMGuard: Guarding Against Unsafe LLM Behavior" accepted at the Demonstrations Track at AAAI 2024. This work was done as part of my GRM internship at IBM Research India.
- August 2023: Started working on my undergraduate thesis on speech processing at the SBILab in CAI-IIIT Delhi.
- May 2023: Started my research internship at IBM Research India. I will be working on guardrails for large language models.
- January 2023: Started my research journey as an undergraduate researcher at MIDAS-IIIT Delhi.

A data-driven personal website
======


Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
