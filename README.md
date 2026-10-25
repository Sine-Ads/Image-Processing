# Image Processing in Pure Python

A lightweight, dependency-free Python project that parses, processes, and exports grayscale PGM (Portable GrayMap) images using basic data structures (2D lists) without external libraries like PIL/Pillow or OpenCV.

---

## Features

- **Header & Pixel Parsing (`load_image.py`):** Parses both ASCII (**P2**) and Binary (**P5**) PGM images, ignoring header comments.
- **2D Grid Transformation (`read_image.py`):** Constructs a clean 2D pixel grid (`rows x columns`) for downstream operations.
- **Image Processing Operations (`process_image.py`):**
  - **Thresholding:** Computes the average pixel intensity $T$ across the image and converts pixels $\ge T$ to $255$ (white) and $< T$ to $0$ (black).
  - **Inversion:** Flips image pixel values using $255 - \text{pixel\_value}$.
  - **Terminal Preview:** Renders an ASCII art representation of pixel grids in the console window.
- **PGM File Export (`save_image.py`):** Writes processed 2D pixel matrices back to disk in standard P2 ASCII format.

---

## File Structure

```text
.
├── load_image.py      # Low-level PGM parser (P2 & P5 formats)
├── read_image.py      # Module interface returning dimensions and 2D pixel grid
├── process_image.py   # Core math routines (thresholding, inversion, ASCII preview)
├── save_image.py      # Writes pixel grids back to P2 PGM files
├── main.py            # Execution pipeline entry point
└── Dog.pgm            # Sample input image

 Usage
1. Run the Pipeline
Execute main.py directly from your terminal:

Bash
python main.py
2. View Output Files
Running main.py generates two processed PGM images in your repository directory:

output_thresholded.pgm — High-contrast binary image (Thresholded)

output_inverted.pgm — Grayscale negative image (Inverted)

Converted Outputs (Optional)
If you convert the outputs using ImageMagick for easier browser viewing:

Bash
magick output_thresholded.pgm output_thresholded.png
magick output_inverted.pgm output_inverted.png
You can view the resulting PNG files directly:

output_thresholded.png

output_inverted.png