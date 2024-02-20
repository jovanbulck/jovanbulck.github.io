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
[imec-DistriNet](https://distrinet.cs.kuleuven.be/)
lab at [KU Leuven](https://www.kuleuven.be/english/), Belgium.
My research explores microarchitectural security limitations along the
hardware-software boundary, with a particular attention for privileged
side-channel attacks in trusted execution environments.
I obtained my PhD entitled ["Microarchitectural Side-Channel Attacks for Privileged
Software Adversaries"](https://jovanbulck.github.io/files/phd-thesis.pdf)
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

* <span style="font-weight: 500;">Program Chair:</span> SysTEX 2024 (co-chair).
* <span style="font-weight: 500;">Technical Program Committee:</span> USENIX Security (2024), ACM CCS (2023, 2022), DIMVA (2023, 2022), IEEE SEED (2024), SysTEX (2023, 2022), PAVeTrust (2023, 2022, 2021).
* <span style="font-weight: 500;">Journal Reviewer:</span> Computers & Security (2022, 2021), ACM Computing Surveys (2020), IEEE Transactions on Dependable and Secure Computing (2020), IEEE Access (2019).
* <span style="font-weight: 500;">Subreviewer:</span> IEEE S&P (2023, 2021, 2020, 2019, 2017), ACM CCS (2019, 2018), USENIX Security (2017), ESORICS (2017), POST (2017), SysTEX (2017).
* <span style="font-weight: 500;">(Co-)organizer:</span> FOSDEM Open-Source <em>Confidential Computing Devroom</em> (2024-2020).
    <div>
      {% assign editions = "
          2024, https://fosdem.org/2024/schedule/track/confidential-computing/;
          2023, https://archive.fosdem.org/2023/schedule/track/confidential_computing/;
          2022, https://archive.fosdem.org/2022/schedule/track/hardware_aided_trusted_computing/;
          2021, https://archive.fosdem.org/2021/schedule/track/hardware_aided_trusted_computing/;
          2020, https://archive.fosdem.org/2020/schedule/track/hardware_aided_trusted_computing/"| split: ";"  %}
      {% for ed in editions %}
        {% assign e = ed | split: ", " %}
            <a href="{{e[1]}}"><button class="ref-btn"><img src="images/fosdem.ico" style="height:1em;">{{e[0]}} program</button></a>
      {% endfor %}
    </div>

<a name="teaching"></a>
# Teaching

* <span style="font-weight: 500;">Lecturer:</span> Operating Systems 2023-2024 (co-taught with Frank Piessens).
    <div>
      <a href="https://onderwijsaanbod.kuleuven.be//2023/syllabi/n/G0Q35AN.htm"><button class="ref-btn"><i class="fas fa-info-circle" style="color:#35798e"></i> B-KUL-G0Q35A - 6 ECTS</button></a>
      <a href="https://onderwijsaanbod.kuleuven.be//2023/syllabi/n/H04G1BN.htm"><button class="ref-btn"><i class="fas fa-info-circle" style="color:#35798e"></i> B-KUL-H04G1BN - 3 ECTS</button></a>
      <a href="https://os.edu.distrinet-research.be/"><button class="ref-btn"><i class="fa fa-globe" aria-hidden="true" style="color:#3793ae"></i> Lab sessions</button></a>
      <a href="https://gitlab.kuleuven.be/distrinet/education/operating-systems/kul-os-homework-student"><button class="ref-btn"><i class="fab fa-github" style="color:#171516;" title="Code"></i> Homeworks</button></a>
    </div>
* <span style="font-weight: 500;">Guest Lectures:</span> Graz Summer School (2022), Operating Systems (2022, 2021), COSIC Hardware Security Course (2019), Computer Architecture and System Software (2018).
* <span style="font-weight: 500;">Tutorials:</span> SPACE 2018, DSN 2018.
* <span style="font-weight: 500;">Teaching Assistant:</span> Operating Systems (2023-2021), Computer Architecture and System Software (2020-2018), Structuur en Organisatie van Systeemsoftware (2017-2015), Informatica Werktuigen (2018-2015), Data Structures and Algorithms (2018-2016).
* <span style="font-weight: 500;">Co-supervised PhD Theses:</span>
  <ul class="compact-lst">
    {% assign phd = site.data.supervision.phd %}
    {% for p in phd %}
      <li>
        <span style="font-weight: 500;">{{p.start}} - {{p.end}}:</span>
        <a href="{{p.home}}" class="nocolor">{{p.name}}</a>{% if p.title %}
          – <em>{{p.title}}</em>, KU Leuven.
            <a href="{{p.pdf}}" class="nounderline">
                <i class="fa fa-file-pdf-o" style="color:#bb0000;" title="PhD thesis"></i>
            </a>
        {% else %}.
        {% endif %}
      </li>
    {% endfor %}
  </ul>
* <span style="font-weight: 500;">Master Thesis Supervision:</span>
  <ul class="compact-lst">
    {% assign msc = site.data.supervision.msc | group_by: "year" %}
    {% for my in msc %}
      <li>
        <span style="font-weight: 500;">{{my.items[0].year}}:</span>
        {% for m in my.items %}
          {{m.name}}{% if forloop.last == true %}.{% else %},{% endif %}
        {% endfor %}
      </li>
    {% endfor %}
  </ul>

<a name="cve"></a>
# Vulnerability Disclosures

{% include fmt-cve.html %}
