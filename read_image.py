from load_image import load_pgm

def read_image(filename):
    """
    Calls load_pgm to get the dictionary, then extracts 
    width, height, and the 2D pixel grid.
    """
    # 1. Call load_pgm to get the raw dictionary
    image_dict = load_pgm(filename)
    
    # 2. Extract dimensions and pixel data
    width = image_dict["width"]
    height = image_dict["height"]
    pixels = image_dict["data"]
    
    # 3. Return values to caller
    return width, height, pixels