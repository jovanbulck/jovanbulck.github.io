---
permalink: /
#title: "About me"
#excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
{% include base_path %}

{% if page.author and site.data.authors[page.author] %}
  {% assign author = site.data.authors[page.author] %}{% else %}{% assign author = site.author %}
{% endif %}

# About me

I am a postdoctoral researcher in the 
[DistriNet](https://distrinet.cs.kuleuven.be/)
lab at [KU Leuven](https://www.kuleuven.be/english/), Belgium.
My research explores microarchitectural security limitations along the
hardware-software boundary, with a particular attention for privileged
side-channel attacks in trusted execution environments.
I obtained my PhD entitled ["Microarchitectural Side-Channel Attacks for Privileged
Software Adversaries"](https://vanbulck.net/files/phd-thesis.pdf)
at KU Leuven in September 2020.

<a name="pubs"></a>
# Publications

{% include fmt-pub.html %}

<a name="talks"></a>
# Talks

{% include fmt-talk.html %}

<a name="awards"></a>
# Awards

{% include fmt-award.html %}

<a name="service"></a>
# Academic Service

{% include fmt-service.html %}

<a name="teaching"></a>
# Teaching

{% include fmt-edu.html %}

<a name="cve"></a>
# Vulnerability Disclosures

{% include fmt-cve.html %}
