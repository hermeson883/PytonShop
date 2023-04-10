import os
from PIL import Image

reduce_fact = 0.5

compressed_path = 'compressed_images'

images_path = 'Pictures'

base_path = os.path.expanduser('~')

total_path = os.path.join(base_path,images_path)

directory_path = os.path.join(total_path, compressed_path)

photos_path = os.path.join(total_path, 'fotos')

files = [i for i in os.listdir(photos_path) if 'jpg' in i]

size_before = 0

size_after = 0

# print(total_path)

if compressed_path not in os.listdir(total_path):
    os.mkdir(directory_path)


for file in files:
    file_path = os.path.join(photos_path, file)
    new_path = os.path.join(directory_path, file)

    size_before += os.stat(file_path).st_size
    img = Image.open(file_path)

    new_w = int(reduce_fact * img.size[0])
    new_h = int(reduce_fact * img.size[1])

    img = img.resize((new_w, new_h), Image.LANCZOS)

    img.save(new_path, 'JPEG', optmize=True, quality=90)

    file_stats = os.stat(new_path)
    size_after += file_stats.st_size

# Reducion of image in bytes
print(f'{size_before} - {size_after} == {size_before - size_after}')

# Reducion in MB

reducion = (size_before - size_after) / (1024 * 1024)
percent = 100 * reducion / size_before * (1024 * 1024)
print(f'Diference im MB {reducion}')
print(f'Size of the file reduce in {percent}')
