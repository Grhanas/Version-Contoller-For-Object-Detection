import os
import shutil
import csv
from datetime import datetime

# Ana dizinler
BASE_DIR = 'version'
ADD_VERSION_DIR = os.path.join(BASE_DIR, 'add_version')
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
MANIFEST_PATH = os.path.join(BASE_DIR, 'manifest.csv')

def get_next_version():
    versions = [d for d in os.listdir(BASE_DIR) if d.startswith('v') and os.path.isdir(os.path.join(BASE_DIR, d))]
    version_numbers = [int(v[1:]) for v in versions if v[1:].isdigit()]
    next_version = max(version_numbers, default=0) + 1
    return f'v{next_version}'

def copy_new_images():
    new_images = os.listdir(os.path.join(ADD_VERSION_DIR, 'images'))
    existing_images = set(os.listdir(IMAGES_DIR))
    for img in new_images:
        if img not in existing_images:
            shutil.copy(os.path.join(ADD_VERSION_DIR, 'images', img), IMAGES_DIR)

def create_version_folder(version_name):
    version_path = os.path.join(BASE_DIR, version_name)
    os.makedirs(version_path, exist_ok=True)
    jsons_src = os.path.join(ADD_VERSION_DIR, 'jsons')
    jsons_dst = os.path.join(version_path, 'jsons')
    shutil.copytree(jsons_src, jsons_dst)
    shutil.copy(os.path.join(ADD_VERSION_DIR, 'metadata.csv'), os.path.join(version_path, 'metadata.csv'))
    return version_path

def update_manifest(version_name, version_path, note=''):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open(MANIFEST_PATH, 'a', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow([version_name, timestamp, version_path.replace('\\', '/'), note])
        
def clear_add_version():
    for subfolder in ['images', 'jsons']:
        folder_path = os.path.join(ADD_VERSION_DIR, subfolder)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
    metadata_path = os.path.join(ADD_VERSION_DIR, 'metadata.csv')
    if os.path.exists(metadata_path):
        os.remove(metadata_path)


def main():
    version_name = get_next_version()
    copy_new_images()
    version_path = create_version_folder(version_name)
    update_manifest(version_name, f'version/{version_name}', note=f'DAY{version_name[1:].zfill(3)}')
    print(f'{version_name} başarıyla eklendi.')
    clear_add_version()
    print('add_version klasörü temizlendi.')

if __name__ == '__main__':
    main()

