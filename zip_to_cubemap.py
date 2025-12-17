import zipfile
import tempfile
import sys
from pathlib import Path
from PIL import Image

REQUIRED_FILES = {
    "front.png",
    "back.png",
    "left.png",
    "right.png",
    "top.png",
    "bottom.png",
}

def extract_zip(zip_path: Path, extract_to: Path):
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(extract_to)

def load_faces(folder: Path):
    faces = {}
    for name in REQUIRED_FILES:
        path = folder / name
        if not path.exists():
            raise FileNotFoundError(f"Missing required file: {name}")
        faces[name] = Image.open(path).convert("RGBA")
    return faces

def validate_sizes(faces: dict):
    sizes = {img.size for img in faces.values()}
    if len(sizes) != 1:
        raise ValueError("All cubemap face images must be the same resolution.")
    return sizes.pop()

def build_horizontal_cross(faces: dict, face_size):
    w, h = face_size
    out = Image.new("RGBA", (w * 4, h * 3), (0, 0, 0, 0))

    out.paste(faces["top.png"],    (w, 0))
    out.paste(faces["left.png"],   (0, h))
    out.paste(faces["front.png"],  (w, h))
    out.paste(faces["right.png"],  (w * 2, h))
    out.paste(faces["back.png"],   (w * 3, h))
    out.paste(faces["bottom.png"], (w, h * 2))

    return out

def main(zip_path: str, output_path: str):
    zip_path = Path(zip_path)
    output_path = Path(output_path)

    if not zip_path.exists():
        raise FileNotFoundError(zip_path)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        extract_zip(zip_path, tmp_path)

        faces = load_faces(tmp_path)
        face_size = validate_sizes(faces)
        cubemap = build_horizontal_cross(faces, face_size)

        cubemap.save(output_path)
        print(f"✔ Cubemap created: {output_path}")
        print(f"✔ Layout: Horizontal Cross (Flax compatible)")
        print(f"✔ Resolution: {cubemap.size[0]}x{cubemap.size[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python zip_to_cubemap.py input.zip output.png")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
