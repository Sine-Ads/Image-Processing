from image_utils import create_p2_pgm

def main():
    pgm_filename = "gradient_4x4.pgm"
    png_filename = "gradient_4x4.png"
    
    width, height = 4, 4
    pixels = [
        0,   85,  170, 255,
        85,  170, 255, 170,
        170, 255, 170, 85,
        255, 170, 85,  0
    ]

    print("--- STARTING PROCESS ---")
    
    create_p2_pgm(pgm_filename, width, height, pixels)

    print("\n[LOG] Inspecting generated PGM file contents:")
    with open(pgm_filename, "r") as f:
        print(f.read().strip())

    

    print("\n--- PROCESS COMPLETED ---")

if __name__ == "__main__":
    main()