---
title: Software Tools
layout: default
nav: true
order: 4
---

## R

### [MarTel](https://gitlab.com/RTbecard/toal) (Marine Telemetry)

> Note: This package is currently undergoing a major overhaul, so functionality is changing on a weekly basis and many functions are temporarily broken or incomplete.  Expect a more polished/stable version to be ready around the start of July 2019... and hopefully a more imaginative package name.

#### Features 
An R package containing tools for:
- Reading HTI `.RAT` files
- Cleaning false detections from HTI hydrophone arrays
- Positioning
    - **Time difference of arrival**. We employ the spherical interpolation method which is a robust closed form solution for geometric positioning.  This allows for positioning in 2 or 3 dimensions so long as there are `dims + 1` hydrophones detecting a given tag pulse.
    - **Modified YAPS**. A flavor of YAPS with some slight differences.  Currently a work in progress.
    
For a broad overview of the package functionality, check out the following vignettes:
- [Cleaning HTI data](https://gitlab.com/RTbecard/toal/-/jobs/artifacts/dev/raw/toal.Rcheck/toal/doc/data_cleaning.html?job=build_package)

#### Installation
```r
require(devtools)
install_git(url = "https://gitlab.com/RTbecard/toal", build_vignettes = T)
## Disable build_vignettes if your installation runs into errors 
```

## Python

> Possibility to have PIP or conda packages listed here?  -James
