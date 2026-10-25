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

Make sure Python is installed and navigate to the project directory. Execute the following command in your terminal:

```bash
python main.py
```

### 2. View the Output Files

Running `main.py` generates two processed PGM images in the project directory:

- `output_thresholded.pgm` — A high-contrast, black-and-white image produced through thresholding.
- `output_inverted.pgm` — A grayscale negative produced by inverting the original pixel intensities.

### 3. Convert Outputs to PNG (Optional)

To convert the PGM files into PNG images for easier viewing in web browsers and image viewers, use ImageMagick:

```bash
magick output_thresholded.pgm output_thresholded.png
magick output_inverted.pgm output_inverted.png
```

You can then open the generated PNG files using any compatible image viewer.

## Requirements

- Python 3
- ImageMagick (optional, only required for converting PGM outputs to PNG)

## Project Goals

This project demonstrates the fundamentals of image processing and file handling in Python, including:

- Parsing structured image file formats.
- Working with 2D lists and matrix-based data.
- Implementing basic image transformations using mathematical operations.
- Reading and writing image files without external image processing libraries.
