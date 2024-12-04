import shutil
import urllib.request
import zipfile
from pathlib import Path

import enlighten

import pycolmap
from pycolmap import logging


output_path = Path("cow gsplat/")
image_path = output_path / "cow photos"
database_path = output_path / "database.db"
sfm_path = output_path / "sfm"

output_path.mkdir(exist_ok=True)

if database_path.exists():
    database_path.unlink()

pycolmap.set_random_seed(0)
pycolmap.extract_features(database_path, image_path)
pycolmap.match_exhaustive(database_path)

if sfm_path.exists():
    shutil.rmtree(sfm_path)
sfm_path.mkdir(exist_ok=True)

num_images = pycolmap.Database(database_path).num_images


with enlighten.Manager() as manager:
    with manager.counter(
        total=num_images, desc="Images registered:"
    ) as pbar:
        pbar.update(0, force=True)
        reconstructions = pycolmap.incremental_mapping(
            database_path,
            image_path,
            sfm_path,
            initial_image_pair_callback=lambda: pbar.update(2),
            next_image_callback=lambda: pbar.update(1),
        )