---
layout: page
permalink: /publications/
title: Publications
description: <h5>You may also checkout <a href="https://www.andrew.cmu.edu/user/kunz1/Publications.html"><u>publications before 2019</u></a> and our <a href="https://www.andrew.cmu.edu/user/kunz1/Research.html"><u>research overview</u></a>.</h5>
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019]
nav: true
---

<div class="publications">


{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}


</div>




