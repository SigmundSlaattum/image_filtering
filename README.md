Filter your image to grayscale or sepia including options of scaling and amount of filter applied to your chosen image
---

This code offers two filters:
- Grayscale filter
- Sepia filter

Options:
- Scale your image to the size you want.\
Use a value in the range [0, 1] to get 0% to 100% size of your original picture.
- Control the filter amount.\
Use a value in the range [0, 1] to get 0% to 100% of either sepia or gray scale to your picture

## How to use
1. Clone project from Github
2. Use pip to install dependencies using command: `pip install -r requirements.txt`
3. Run file using command `python main.py -h`\
This brings you to the help menu.

## Instructions (-h)
```
usage: main.py [-h] [-o OUT] [-g | -se] [-sc SCALE] [-fa FILTER_AMOUNT] file

Takes an image and applies gray tone or sepia filter

positional arguments:
  file                  The filename of a picture to apply filter to

options:
  -h, --help            show this help message and exit
  -o OUT, --out OUT     The output filename
  -g, --gray            Select gray filter
  -se, --sepia          Select sepia filter
  -sc SCALE, --scale SCALE
                        Scale factor to resize image
  -fa FILTER_AMOUNT, --filter_amount FILTER_AMOUNT
                        Scale factor to scale the amount of filter you want
```
---
### Example of use 1:
Apply grayscale filter to an image:

`python main.py someImage.jpg -g`

### Example of use 2:
Apply sepia filter to an image:

`python main.py someImage.jpg -se`

### Example of use 3:
Apply 50% sepia filter to an image and scale it to 80% of its original size: 

`python main.py someImage.jpg -se -fa 0.5 -sc 0.8`

### Example of use 4:
Apply 80% gray scale filter to image and save to disk:

`python main.py someImage.jpg -g -fa 0.8 -o mySavedImage.jpg`

---