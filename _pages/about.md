---
permalink: /
#title: "About me"
#excerpt: "About me"
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---
{% include base_path %}

{% if page.author and site.data.authors[page.author] %}
  {% assign author = site.data.authors[page.author] %}{% else %}{% assign author = site.author %}
{% endif %}

<div style="display:flex; align-items:center; gap:1.5em;">
  <div class="author__avatar">
    	<img src="{{ author.avatar | prepend: "/images/" | prepend: base_path }}" class="author__avatar" alt="{{ author.name }}"  fetchpriority="high" />
  </div>

  <div>
    <p>
      I am a professor in the <a href="https://distrinet.cs.kuleuven.be/">DistriNet</a> lab at
      the Department of Computer Science of <a href="https://www.kuleuven.be/english/">KU Leuven</a>, Belgium.
      My research explores attacks and defenses at the hardware-software boundary,
      with particular attention to privileged side channels in trusted execution
      environments.
    </p>
  
    <div class="author__urls social-icons" style="display:flex; flex-wrap:wrap; gap:0.5em 1em; align-items:center;">
        <div><i class="fas fa-fw fa-location-dot icon-pad-right" aria-hidden="true"></i>{{ author.location }}</div>
        <div><a href="mailto:{{ author.email }}"><i class="fas fa-fw fa-envelope icon-pad-right" aria-hidden="true"></i>{{ site.data.ui-text[site.locale].email_label | default: "Email" }}</a></div>
        <div><a href="{{ author.googlescholar }}"><i class="ai ai-google-scholar ai-fw icon-pad-right"></i>Google Scholar</a></div>
        <div><a href="{{ author.orcid }}"><i class="ai ai-orcid ai-fw icon-pad-right"></i>ORCID</a></div>
        <div><a href="https://github.com/{{ author.github }}"><i class="fab fa-fw fa-github icon-pad-right" aria-hidden="true"></i>GitHub</a></div>
    </div>
  </div>
</div>



<a name="pubs" id="pubs"></a>
{% include fmt-pub.html %}

<a name="talks" id="talks"></a>
# Talks

{% include fmt-talk.html %}

<a name="awards" id="awards"></a>
# Awards and Recognitions

{% include fmt-award.html %}

<a name="service" id="service"></a>
# Academic Service

{% include fmt-service.html %}

<a name="edu" id="edu"></a>
# Teaching

{% include fmt-edu.html %}

<a name="foss" id="foss"></a>
# Selected Open-Source Contributions

{% include fmt-foss.html %}

<a name="cve" id="cve"></a>
# Vulnerability Disclosures

{% include fmt-cve.html %}
