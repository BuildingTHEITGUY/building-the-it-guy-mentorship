# Setup Guide

## Prerequisites
- Python 3.11+
- Conda (Miniconda or Anaconda) OR Docker
- A free ESA Earth Online account: https://earth.esa.int/eogateway

---

## Option A: Conda Setup

    conda env create -f environment.yml
    conda activate p-band-sar
    jupyter lab

---

## Option B: Docker Setup

    docker build -t pband-sar .
    docker run -p 8888:8888 pband-sar

Then open http://localhost:8888 in your browser.

---

## ESA Account Setup

1. Go to https://earth.esa.int/eogateway
2. Click **Login** then **Register**
3. Fill in your details (use your university/research email)
4. You will need this account to download BIOMASS products in Mission 1

---

## Verify Installation

After activating your environment, run this in Python:

    import rasterio
    import geopandas
    import matplotlib
    import numpy
    print("All core libraries installed successfully!")
