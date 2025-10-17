import os
import shutil
import csv
from datetime import datetime

def initialize_version(jsons_src, csv_src, version_name="v1"):
    version_path = os.path.join("version", version_name)
    jsons_dst = os.path.join(version_path, "jsons")
    metadata_dst = os.path.join(version_path, "metadata.csv")

    # Klasörleri oluştur
    os.makedirs(jsons_dst, exist_ok=True)

    # JSON dosyalarını taşı
    for file in os.listdir(jsons_src):
        shutil.move(os.path.join(jsons_src, file), os.path.join(jsons_dst, file))

    # CSV dosyasını taşı
    shutil.move(csv_src, metadata_dst)

    # Manifest güncelle
    manifest_path = "manifest.csv"
    if not os.path.exists(manifest_path):
        with open(manifest_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["version", "timestamp", "path", "notes"])

    with open(manifest_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            version_name,
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            version_path,
            "İlk veri seti"
        ])

def main():
    # Kaynak klasör ve dosya yollarını belirt
    jsons_src = "jsons"
    csv_src = "Day.csv"
    version_name = "v1"

    # Versiyonu başlat
    initialize_version(jsons_src, csv_src, version_name)
    print(f"{version_name} başarıyla oluşturuldu ve manifest güncellendi.")

if __name__ == "__main__":
    main()
