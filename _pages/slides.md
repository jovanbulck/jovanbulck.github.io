---
sitemap: false
permalink: /slides.html
layout: plain
title: Slides Gallery
---
{% include base_path %}

<style>
  body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      text-align: center;
      padding-top: 10px;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 16px;
  }
  .item {
    text-align: center;
  }
  img {
    width: 100%;
    border-radius: 6px;
    box-shadow: 0 2px 6px rgba(0,0,0,.15);
  }
  a {
    margin-top: 6px;
    font-size: 0.9rem;
    word-break: break-word;
    text-decoration: none; color: #000;
  }
</style>

# Slides Gallery
<em>(Auto-generated on {{ site.time }} -- click on preview image to open slide deck PDF).</em>

{% assign years = site.data.talks.talks | group_by: "year" %}

{% for y in years %}
{% for p in y.items %}
  {% if forloop.first == true %}
  <h2>{{y.name}}</h2>
  <div class="grid">
  {% endif %}
    {% unless p.no-slides or p.ext-id %}
    <div class="item">
      <a href="files/{{ p.id }}.pdf">
        <img src="images/previews/{{ p.id }}.jpg" alt="{{ p.title }}">
      </a>
    </div>
    {% endunless %}
  {% if forloop.last == true %}
  </div>
  {% endif %}
{% endfor %}
{% endfor %}