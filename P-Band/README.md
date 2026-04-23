# P-Band SAR & The ESA BIOMASS Mission

> A hands-on learning lab for students, researchers, and faculty exploring P-Band Synthetic Aperture Radar and the ESA BIOMASS satellite mission.

---

## What This Repo Is

This is NOT a textbook. Every folder is a **mission** -- a self-contained, practical exercise using **real satellite data** from ESA.

| # | Mission | Folder | Difficulty | Time |
|---|---------|--------|-----------|------|
| 1 | Your First SAR Image | 01-your-first-sar-image/ | Beginner | 30 min |
| 2 | BIOMASS Data Explorer | 02-biomass-data-explorer/ | Intermediate | 1 hour |
| 3 | Forest Carbon Calculator | 03-forest-carbon-calculator/ | Intermediate | 1.5 hours |
| 4 | Subsurface Detective | 04-subsurface-detective/ | Advanced | 2 hours |
| 5 | ML-Powered SAR Classifier | 05-ml-sar-classifier/ | Advanced | 3 hours |

---

## What is P-Band Radar?

P-band uses a **~70 cm wavelength** -- long enough to penetrate tree canopies, dry sand, and soil. Unlike C-band (Sentinel-1) or X-band (TerraSAR-X), P-band sees **through** vegetation to trunks, the forest floor, and even subsurface structures.

---

## The ESA BIOMASS Mission

Launched April 2025, BIOMASS is the **first P-band SAR satellite in space**. It maps global forest biomass to quantify how much carbon Earth's forests store.

### Key Applications
- **Forest Biomass Mapping:** Measure wood mass to calculate carbon storage
- **Subsurface Imaging:** Penetrate dry sand to reveal buried rivers, archaeological sites
- **Ice Sheet Mapping:** See internal structure of glaciers

---

## Quick Start

Option A - Conda:

    cd 00-setup/
    conda env create -f environment.yml
    conda activate p-band-sar
    jupyter lab

Option B - Docker:

    cd 00-setup/
    docker build -t pband-sar .
    docker run -p 8888:8888 pband-sar

---

## Key Resources

| I want to... | Go here |
|---|---|
| Download BIOMASS data | [ESA Earth Online](https://earth.esa.int/eogateway) |
| Process SAR to Biomass maps | [BioPAL (GitHub)](https://github.com/BioPAL/BioPAL) |
| Train ML models on SAR | [M3LEO (Hugging Face)](https://huggingface.co/datasets/m3leo) |
| Understand the mission | [ESA BIOMASS Official](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Biomass) |

---

## Open-Source Tools & Datasets

- **[BioPAL](https://github.com/BioPAL/BioPAL):** Official ESA library -- processes Level 1 SAR to Level 2 forest products (AGB)
- **[M3LEO Dataset](https://huggingface.co/datasets/m3leo):** ~17 million data chips combining SAR + optical imagery for AI training
- **[ESA Earth Online](https://earth.esa.int/eogateway):** Official hub for all ESA Earth observation datasets

---

## Repository Structure

    P-Band/
    |-- README.md
    |-- 00-setup/                        <- Environment setup
    |-- 01-your-first-sar-image/         <- Mission 1: Download & visualize
    |-- 02-biomass-data-explorer/        <- Mission 2: Real BIOMASS data
    |-- 03-forest-carbon-calculator/     <- Mission 3: Carbon estimation
    |-- 04-subsurface-detective/         <- Mission 4: Desert penetration
    |-- 05-ml-sar-classifier/           <- Mission 5: AI on SAR data
    |-- cheatsheets/                     <- Quick-reference cards
    |-- data/                            <- Sample datasets + scripts
    |-- resources/                       <- Links, papers, notes

---

*Maintained by Mohamed Asath as part of the [Building The IT Guy Mentorship](https://github.com/BuildingTHEITGUY/building-the-it-guy-mentorship) program.*
