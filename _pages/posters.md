---
sitemap: false
permalink: /posters.html
layout: plain
title: Poster Gallery
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
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
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

# Poster Gallery
<em>(Auto-generated on {{ site.time }}).</em>

{% assign years = site.data.talks.talks | concat: site.data.papers.pubs | where_exp: "item", "item.poster" | group_by: "year" %}
{% assign posters = "" %}
{% for y in years %}
{% for p in y.items %}
    {% if p.poster == true %}
      {% assign pdf = "files/" | append: p.id | append: "-poster.pdf" %}
    {% else %}
      {% assign pdf = p.poster %}
    {% endif %}
    {% assign posters = posters | append: ', ' | append: pdf %}
{% endfor %}
{% endfor %}
{% assign posters = posters | remove_first: ', ' |  remove_first: ', files/phd-thesis-poster.pdf' | split: ', ' | uniq %}

<div class="grid">
{% for pdf in posters %}
    <div class="item">
      {% assign pdf_name = pdf | remove: "files/" | remove: ".pdf" %}

      <a href="{{pdf}}">
        <img src="images/previews/{{ pdf_name }}.jpg" alt="{{ p.title }}">
        <div>{{ pdf_name }}</div>
      </a>
    </div>
{% endfor %}
</div>