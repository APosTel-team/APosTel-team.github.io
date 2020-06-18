---
title: Positioning
layout: default
nav: true
order: 3
---

## Positioning

Traditionally, positioning is based on the time difference of arrival (TDOA) method, using hyperbolic triangulation. The R package [MarTel](https://gitlab.com/RTbecard/toal) provides a tool for this.

A new approach is to start from time of arrival and include the information of an animal behaviour model. This approach is used in the [YAPS algorithm](https://github.com/baktoft/yaps), presented in Baktoft, Gjelland, Økland & Thygesen (2017): [Positioning of aquatic animals based on time-of-arrival and random walk models using YAPS (Yet Another Positioning Solver)](https://www.nature.com/articles/s41598-017-14278-z.pdf). A step-by-step guide for using YAPS can be found [here](https://www.biorxiv.org/content/10.1101/2019.12.16.877688v1).

[MarTel](https://gitlab.com/RTbecard/toal) provides a modified version of YAPS for HTI data.


<!---
Link to all kinds of adapted YAPS versions for different systems (e.g. James’ code for HTI system)
Link to TDOA algorithm code
-->
