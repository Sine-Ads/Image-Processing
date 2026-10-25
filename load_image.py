def load_pgm(filename):
    with open(filename, 'rb') as f:
        # 1. Read the magic number to determine format
        header = f.readline().decode('utf-8').strip()
        if header not in ('P2', 'P5'):
            raise ValueError("Not a valid P2 or P5 PGM file")
        
        # 2. Skip comments and read dimensions (width, height)
        line = f.readline().decode('utf-8').strip()
        while line.startswith('#'):
            line = f.readline().decode('utf-8').strip()
        
        width, height = map(int, line.split())
        
        # 3. Read the maximum pixel value (max_val)
        line = f.readline().decode('utf-8').strip()
        while line.startswith('#'):
            line = f.readline().decode('utf-8').strip()
        max_val = int(line)
        
        # 4. Read the pixel data
        pixels = []
        if header == 'P2':
            # P2 is ASCII: read whitespace-separated integers
            data = f.read().decode('utf-8').split()
            # Convert string numbers to integers
            flat_pixels = [int(val) for val in data]
        elif header == 'P5':
            # P5 is Binary: read raw bytes
            data = f.read()
            # If max_val < 256, each pixel is 1 byte; otherwise 2 bytes
            if max_val < 256:
                flat_pixels = list(data)
            else:
                # Handle 16-bit binary data (MSB first / Big Endian)
                flat_pixels = []
                for i in range(0, len(data), 2):
                    flat_pixels.append((data[i] << 8) + data[i+1])

        # 5. Reshape the flat list into a 2D list (rows x columns)
        for i in range(0, len(flat_pixels), width):
            pixels.append(flat_pixels[i:i + width])
            
        return {
            "width": width,
            "height": height,
            "max_val": max_val,
            "data": pixels  # This is your 2D grid of grayscale values
        }

