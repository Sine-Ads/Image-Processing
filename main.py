# main.py
from read_image import read_image
from process_image import threshold_image, invert_image, average_intensity, print_ascii_preview
from save_image import save_pgm_p2

def main():
    filename = "Dog.pgm"
    
    # 1. Read input image
    width, height, pixel_grid = read_image(filename)
    print(f"Loaded '{filename}' ({width}x{height})\n")
    
    # 2. Process & Save Thresholded Image
    avg_val = average_intensity(pixel_grid, width, height)
    print(f"Average intensity threshold: {avg_val:.2f}")
    thresholded_grid = threshold_image(pixel_grid, width, height)
    save_pgm_p2("output_thresholded.pgm", width, height, thresholded_grid)
    print("Saved 'output_thresholded.pgm'")
    
    # 3. Process & Save Inverted Image
    inverted_grid = invert_image(pixel_grid)
    save_pgm_p2("output_inverted.pgm", width, height, inverted_grid)
    print("Saved 'output_inverted.pgm'\n")

    # 4. Terminal Previews
    print("--- Terminal Preview: Thresholded Image ---")
    print_ascii_preview(thresholded_grid)
    
    print("\n--- Terminal Preview: Inverted Image ---")
    print_ascii_preview(inverted_grid)

if __name__ == "__main__":
    main()