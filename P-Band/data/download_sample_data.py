"""
Sample Data Downloader for P-Band SAR Missions
Usage: cd data/ && python download_sample_data.py
"""

import os


def setup_data_folders():
    """Create organized subfolders for each mission data."""
    mission_folders = [
        "mission_01_first_sar",
        "mission_02_biomass",
        "mission_03_carbon",
        "mission_04_subsurface",
        "mission_05_ml_training",
    ]

    for folder in mission_folders:
        os.makedirs(folder, exist_ok=True)
        print(f"  Created: data/{folder}/")


def print_download_instructions():
    """Print instructions for downloading real datasets."""
    print()
    print("=" * 60)
    print("DATA DOWNLOAD INSTRUCTIONS")
    print("=" * 60)
    print()
    print("1. ESA BIOMASS Products (Missions 1-4):")
    print("   https://earth.esa.int/eogateway")
    print("   - Register for a free account")
    print("   - Search for BIOMASS in the dataset catalog")
    print("   - Download Level-1 and Level-2 products")
    print("   - Place .tif files in the appropriate mission folder")
    print()
    print("2. Sentinel-1 C-Band Data (Mission 2 comparison):")
    print("   https://browser.dataspace.copernicus.eu/")
    print("   - Search for the same region as your BIOMASS data")
    print("   - Download GRD products")
    print()
    print("3. M3LEO Dataset for ML (Mission 5):")
    print("   https://huggingface.co/datasets/m3leo")
    print()
    print("=" * 60)


if __name__ == "__main__":
    print("P-Band SAR BIOMASS - Data Setup")
    print()
    setup_data_folders()
    print_download_instructions()
