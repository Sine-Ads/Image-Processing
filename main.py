from read_image import read_image

def main():
    filename = "Dog.pgm"
    
    # Call read_image, which internally calls load_pgm
    width, height, pixel_grid = read_image(filename)
    
    print(f"Loaded image '{filename}': {width}x{height}")
    


if __name__ == "__main__":
    main()