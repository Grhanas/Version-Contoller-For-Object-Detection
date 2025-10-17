# Version-Contoller-For-Object-Detection
Automated versioning system for image datasets. Users simply drop new data into the add_version folder, and the system creates a new version, updates the manifest.csv, and integrates the data without conflicts.

# 📦 Automated Image Dataset Versioning System

This project provides a lightweight and automated versioning system for image datasets. Users simply place new data into the `add_version` folder, and the system handles everything: creating a new version folder, updating the manifest, copying new images, and organizing metadata — all without overwriting existing data.

---

## 🚀 Features

- Automatic version folder creation (`v1`, `v2`, `v3`, ...)
- Adds new images to the central `images/` folder (with duplication check)
- Moves JSON annotation files into the version folder
- Stores `metadata.csv` alongside each version
- Updates `manifest.csv` with version info and timestamp
- Cleans up the `add_version/` folder after successful processing

---

## 📁 Folder Structure

```plaintext
version/
├── manifest.csv
├── images/                # All unique images are stored here
├── v1/
│   ├── jsons/
│   └── metadata.csv
├── v2/
│   ├── jsons/
│   └── metadata.csv
└── add_version/           # User drops new data here
    ├── images/
    ├── jsons/
    └── metadata.csv

