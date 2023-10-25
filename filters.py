import numpy as np

def grayScaleFilter(image: np.array, k: float = 1.0) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    
    weights = np.asarray([0.21, 0.72, 0.07])  # When multiplying the original rgb values with this gives a nice grayscale picture
    gray_image = np.empty_like(image)
    gray_image = (image @ weights)

    gray_image = np.repeat(gray_image[:,:,None], 3, axis=2)
    gray_image = gray_image.astype("uint8")
    
    
    # Optional amount of grayscale
    gray_image = gray_image * k + image * (1 - k)
    
    gray_image = gray_image.astype("uint8")
    return gray_image

def sepiaFilter(image: np.array, k: float = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
        you may ignore it)

    Returns:
        np.array: sepia_image
    """
    
    sepia_image = np.empty_like(image)
    sepia_image = sepia_image.astype("float64")
    
    # These values multiplied with the rgb values of the original picture gives a sepia look.
    sepia_matrix = np.array([
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.686, 0.168],
    [ 0.272, 0.534, 0.131],
    ])

    sepia_image = image @ sepia_matrix.T
   
    # Optional amount of sepia:
    sepia_image = sepia_image * k + image * (1 - k)
   
    sepia_image *= (255.0/ sepia_image.max())
    sepia_image = sepia_image.astype("uint8")
   
    return sepia_image