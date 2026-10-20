import os
import subprocess

def create_p2_pgm(filename, width, height, pixels, max_val=255):
    """Creates a P2 ASCII PGM file from pixel values."""
    print(f"[LOG] Generating PGM file: {filename}")
    print(f"[LOG] Grid size: {width}x{height}, Max value: {max_val}")
    
    with open(filename, "w") as f:
        f.write(f"P2\n{width} {height}\n{max_val}\n")
        
        for i, val in enumerate(pixels):
            f.write(f"{val} ")
            if (i + 1) % width == 0:
                f.write("\n")
                
    print(f"[LOG] Successfully wrote {len(pixels)} pixel values to {filename}.")

