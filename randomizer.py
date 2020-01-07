import random 
from pathlib import Path
from shutil import copy2 as copyfile
from tqdm import tqdm
import os 

p = Path('.')
# Path.mkdir('./data/tian/', exist_ok=True)
# Path.mkdir('./data/bertus/',exist_ok=True)
image_file = []

for file in p.glob('./data/images/*.jpg'): 
    image_file.append(file)

for t, b in tqdm(zip(image_file[:len(image_file)//2], image_file[len(image_file)//2:])): 
    nama_t = str(t).split('\\')[-1]
    copyfile(t, f'./data/tian/{nama_t}')
    nama_b = str(b).split('\\')[-1]
    copyfile(b, f'./data/bertus/{nama_b}')
