# save_image.py

def save_pgm_p2(filename, width, height, pixel_grid, max_val=255):
    """
    Saves a 2D grid of pixel values to disk in P2 (ASCII PGM) format.
    """
    with open(filename, 'w', encoding='ascii') as f:
        # Write standard P2 header
        f.write("P2\n")
        f.write("# Created by Python Image Processor\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_val}\n")
        
        # Write pixel grid rows
        for row in pixel_grid:
            row_str = " ".join(str(pixel) for pixel in row)
            f.write(row_str + "\n")