---
sitemap: false
permalink: /videos.html
layout: plain
title: Talk Recordings
---
{% include base_path %}

<style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      text-align: center;
      padding-top: 10px;
    }
    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      padding: 20px;
      max-width: 1200px;
      margin: 0 auto;
    }
    .talk {
      background: white;
      padding: 15px;
      border-radius: 10px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .talk h2 {
      font-size: .8em;
      margin: 0 0 10px;
      font-weight: normal;
    }
    iframe, video {
      width: 100%;
      height: 200px;
      border: none;
      border-radius: 8px;
    }
    video {
      background: black;
    }
</style>

# Talk Recordings

<em>(Auto-generated on {{ site.time }})</em>

<div class="gallery">
  {% for talk in site.data.talks.talks %}
    {% if talk.recording %}
        {% assign video_id = "" %}

        {% if talk.recording contains "youtube.com/watch?v=" %}
          {% assign query = talk.recording | split: '?' | last %}
          {% assign params = query | split: '&' %}
          {% for param in params %}
            {% assign pair = param | split: '=' %}
            {% if pair[0] == "v" %}
              {% assign video_id = pair[1] %}
            {% endif %}
          {% endfor %}
        {% elsif talk.recording contains "youtu.be/" %}
          {% assign video_id = talk.recording | split: '/' | last %}
        {% endif %}

        {% if video_id != "" or talk.recording contains ".webm" %}
        <div class="talk">
            <h2><b>{{ talk.title }}</b> <em>@{{ talk.venue }}</em> ({{ talk.month }}, {{ talk.year }})</h2>
            {% if video_id != "" %}
                <iframe src="https://www.youtube.com/embed/{{ video_id }}" allowfullscreen></iframe>
            {% elsif talk.recording contains ".webm" %}
                <video controls>
                  <source src="{{ talk.recording }}" type="video/webm">
                  Your browser does not support the video tag.
                </video>
            {% endif %}
        </div>
        {% endif %}
    {% endif %}
  {% endfor %}
</div>