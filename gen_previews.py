#!/usr/bin/python3
import glob
import subprocess
from pathlib import Path

MAX_WIDTH = 900
JPEG_QUALITY = 65
out_dir =  Path('images/previews/')

for pdf in sorted(glob.glob("files/*-poster.pdf")):
    name = Path(pdf).stem
    img = out_dir / f"{name}.jpg"

    if not img.exists():
        print(f'.. generating {img}')
        tmp = out_dir / f"{name}_tmp"
        subprocess.run([
            "pdftoppm",
            "-jpeg",
            "-f", "1", "-l", "1",
            "-scale-to-x", str(MAX_WIDTH),
            "-scale-to-y", "-1",
            "-singlefile",
            pdf,
            str(tmp)
        ], check=True)

        tmp_img = tmp.with_suffix(".jpg")
        tmp_img.rename(img)

        subprocess.run([
            "jpegoptim",
            "--max", str(JPEG_QUALITY),
            "--strip-all",
            str(img)
        ], check=True)
