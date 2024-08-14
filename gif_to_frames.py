from PIL import Image, ImageSequence

def gif_to_frames(gif_path: str, output_path: str):
    gif = Image.open(gif_path)
    for i, frame in enumerate(ImageSequence.Iterator(gif)):
        # Create a new frame with mode 'L' for grayscale to manipulate pixels
        frame = frame.convert('L')
        
        # Correcting errors in pixel colors (deviation from black and white)
        for j in range(frame.width):
            for k in range(frame.height):
                pixel = frame.getpixel((j, k))
                # Assuming threshold for conversion based on gray scale
                frame.putpixel((j, k), 255 if pixel > 128 else 0)

        # Correct path handling and file saving
        frame.save(f"{output_path}/frame_{i}.png")

    print(f"Frames extracted from {gif_path} and saved to {output_path}")

# Example usage
gif_to_frames(r"C:\Users\vipin\Downloads\larger.gif", r"D:\Coding\My Stupidity Palace\PYTHON\Arbitrary Codes\frames")
