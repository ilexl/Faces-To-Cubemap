# Faces-To-Cubemap
Simple python tool that turns 6 faces (.png) from a .zip file into a single cubemap texture (.png)

# ZIP → Flax Cubemap Tool

A simple python tool (tested in Python 3.13) that converts a ZIP archive containing six cubemap face images into a single cubemap texture using a horizontal cross layout.

Designed specifically for fast cubemap preparation for **Flax Engine** but could be useful elsewhere.

---

## Requirements

- **Python 3.13.5+**
- Pillow (PIL fork)

Install Pillow:

```bash
pip install pillow
```

---

## Features

- Accepts a `.zip` file containing cubemap faces
- Validates required images and resolutions
- Outputs a **single stitched cubemap image**
- Uses **Horizontal Cross layout**
- Minimal dependencies
- Fails fast on errors

---

## Required Input Files

The ZIP archive **must contain exactly these files**:

```
front.png
back.png
left.png
right.png
top.png
bottom.png

```

### Rules
- All images **must be PNG**
- All images **must be the same resolution**
- File names are **case-sensitive**

---

## Cubemap Layout (Horizontal Cross)

The output image is arranged as:

```
        [ top ]
[ left ][ front ][ right ][ back ]
        [ bottom ]
```

Final image resolution will be:

```
(width × 4) by (height × 3)
```

This layout is supported directly by **Flax Engine** when importing cubemaps.

---

## Usage

```bash
python zip_to_flax_cubemap.py input.zip output.png
```

### Example

```bash
python zip_to_flax_cubemap.py skybox.zip skybox_cubemap.png
```

---

## Importing into Flax Engine

1. Drag the generated PNG into your Flax project
2. Select the texture asset
3. Set:
   - **Texture Type:** `Cube Texture`
   - **Layout:** `Horizontal Cross`
4. Save the asset

The cubemap is now ready for use in skyboxes, reflections, or lighting.

---

## Error Handling

The tool will stop with a clear error if:

- A required face image is missing
- Image resolutions do not match
- The ZIP file cannot be read

---

## Notes

- No image rotation is applied — face orientation must already be correct
- Alpha channel is preserved
- Output format is PNG (lossless)

---

## Possible Extensions

If needed, this tool can be extended to support:
- DDS export
- Vertical cross layout
- Face rotation correction
- Batch processing
- CLI installation via `pip`

---

## License

This tool is provided as-is, free to modify and use in personal or commercial projects.
