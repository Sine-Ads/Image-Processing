# Image Processing in Pure Python

A lightweight, dependency-free Python project that parses, processes, and exports grayscale PGM (Portable GrayMap) images using basic data structures such as 2D lists. The project implements fundamental image processing operations without external libraries like PIL/Pillow or OpenCV.

## Features

### 1. Header and Pixel Parsing (`load_image.py`)
- Parses both ASCII (`P2`) and binary (`P5`) PGM image formats.
- Handles comments in PGM headers.
- Extracts image dimensions, maximum pixel intensity, and pixel data.

### 2. 2D Grid Transformation (`read_image.py`)
- Converts parsed pixel data into a structured 2D grid.
- Represents the image as a matrix of rows and columns for further processing.

### 3. Image Processing Operations (`process_image.py`)
- **Thresholding:** Calculates the average pixel intensity \(T\) of the image and converts pixels greater than or equal to \(T\) to white (`255`) and pixels below \(T\) to black (`0`).
- **Inversion:** Inverts pixel intensities using the formula `255 - pixel_value`.
- **Terminal Preview:** Displays an ASCII representation of the pixel grid directly in the console.

### 4. PGM File Export (`save_image.py`)
- Exports processed 2D pixel matrices as standard ASCII (`P2`) PGM files.
- Preserves image dimensions and pixel intensity information.

## Project Structure

```text
.
├── load_image.py      # Low-level PGM parser (P2 and P5 formats)
├── read_image.py      # Converts parsed data into a 2D pixel grid
├── process_image.py   # Image processing and ASCII preview functions
├── save_image.py      # Exports pixel grids as P2 PGM files
├── main.py            # Main execution pipeline
└── Dog.pgm            # Sample input image
```

## Usage

### 1. Run the Pipeline

Execute `main.py` directly from your terminal:

```bash
python main.py
```

### 2. View Output Files

Running `main.py` generates two processed PGM images in the project directory:

- `output_thresholded.pgm` — High-contrast, black-and-white image produced through thresholding.
- `output_inverted.pgm` — Grayscale negative image produced through inversion.

### 3. Convert Outputs to PNG (Optional)

If you have ImageMagick installed, convert the PGM files to PNG format for easier viewing:

```bash
magick output_thresholded.pgm output_thresholded.png
magick output_inverted.pgm output_inverted.png
```

### 4. View the Converted Images

Open the generated PNG files using any compatible image viewer:

- `output_thresholded.png`
- `output_inverted.png`

## Requirements

- Python 3
- ImageMagick (optional, required only for converting PGM files to PNG)

