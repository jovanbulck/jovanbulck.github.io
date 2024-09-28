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

I am a professor in the [DistriNet](https://distrinet.cs.kuleuven.be/) lab at
the Department of Computer Science of [KU Leuven](https://www.kuleuven.be/english/), Belgium.
My research explores attacks and defenses at the hardware-software boundary,
with particular attention to privileged side channels in trusted execution
environments.

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

<a name="foss"></a>
# Selected Open-Source Contributions

{% include fmt-foss.html %}

<a name="cve"></a>
# Vulnerability Disclosures

{% include fmt-cve.html %}
