import argparse
import sys

import filters as f
import numpy as np
from PIL import Image

def run_filter(
    file: str,
    out_file: str = None,
    filter: str = "grayScaleFilter",
    scale: float = 1.0,
    filter_amount: float = 1.0
) -> None:
    """Run the selected filter"""
    
    # load the image from a file
    try:
        image = Image.open(file)
    except FileNotFoundError:
        print("File not found. Enter a valid filename and path")
        sys.exit(1)

    if filter_amount < 0:
        filter_amount = 0.0
        print("Filter amount must be a value in range [0, 1].\nFilter_amount automatically adjusted to 0 due to input lower than 0.")
    elif filter_amount > 1:
        filter_amount = 1.0
        print("Filter amount must be a value in range [0, 1].\nFilter_amount automatically adjusted to 1 due to input higher than 1.")

    if scale != 1 and not scale == None:
        # Resize image, if this option is used:
        image = image.resize((int(image.width*scale), int(image.height*scale)))
    
    # converting image to np.array
    image = np.asarray(image, dtype="uint8")

    # Applying the filter 
    
    if filter == "grayScaleFilter":
        filtered = f.grayScaleFilter(image, filter_amount)
    elif filter == "sepiaFilter":
        filtered = f.sepiaFilter(image, filter_amount)
    else:
        print("Not a valid choice of filter")


    if out_file:
        # save the file
        Image.fromarray(filtered).save(out_file)
        print("----------------- Success: File saved to disk -----------------")
        Image.fromarray(filtered).show()
    else:
        # not asked to save, display it instead
        Image.fromarray(filtered).show()


if __name__ == "__main__":
    
    argv = sys.argv[1:]
    parser = argparse.ArgumentParser(description="Takes an image and applies gray tone or sepia filter")

    parser.add_argument("file", help="The filename of a picture to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    group = parser.add_mutually_exclusive_group()
    
    # Add required arguments
    group.add_argument("-g", "--gray", help="Select gray filter", action="store_true")
    group.add_argument("-se", "--sepia", help="Select sepia filter", action="store_true")
    parser.add_argument("-sc", "--scale", help="Scale factor to resize image", type=float)
    parser.add_argument("-fa", "--filter_amount", help="Scale factor to scale the amount of filter you want", type=float)


    # parse arguments and call run_filter
    args = parser.parse_args()
    
    filter = "grayScaleFilter"
    
    if args.sepia:
        filter = "sepiaFilter"
    if args.gray:
        filter = "grayScaleFilter"
    
    if args.filter_amount is None:
        filter_amount = 1.0
    else:
        filter_amount = args.filter_amount
    
    run_filter(file=args.file, out_file=args.out, filter=filter, scale=args.scale, filter_amount=filter_amount)
  

    
