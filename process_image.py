def average_intensity(pixel_grid, width, height):
    total_sum = 0
    for row in pixel_grid:
        for pixel in row:
            total_sum += pixel
    return total_sum / (width * height)


def threshold_image(pixel_grid, width, height):
    T = average_intensity(pixel_grid, width, height)
    thresholded_grid = []
    
    for row in pixel_grid:
        new_row = []
        for pixel in row:
            if pixel >= T:
                new_row.append(255)
            else:
                new_row.append(0)
        thresholded_grid.append(new_row)
        
    return thresholded_grid


def invert_image(pixel_grid, max_val=255):
    inverted_grid = []
    
    for row in pixel_grid:
        new_row = []
        for pixel in row:
            new_row.append(max_val - pixel)
        inverted_grid.append(new_row)
        
    return inverted_grid

def print_ascii_preview(pixel_grid, scale_step=1):
    """
    Prints a coarse ASCII text representation of the image in the terminal.
    Set scale_step higher (e.g. 2 or 4) for large images to fit in terminal.
    """
    chars = " .:-=+*#%@"
    
    for row in pixel_grid[::scale_step]:
        line = ""
        for pixel in row[::scale_step]:
            char_idx = int((pixel / 255) * (len(chars) - 1))
            line += chars[char_idx] * 2  # Double characters to balance aspect ratio
        print(line)