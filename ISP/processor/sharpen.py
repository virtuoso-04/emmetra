import numpy as np
from scipy.ndimage import gaussian_filter # type: ignore

def sharpen(rgb_image, amount=1.5, sigma=1):
    # Apply Gaussian filter to blur the image
    blurred = gaussian_filter(rgb_image, sigma=sigma)
    
    # Unsharp masking formula: Original + Amount * (Original - Blurred)
    sharpened = rgb_image + amount * (rgb_image - blurred)
    return np.clip(sharpened, 0, 4095).astype(np.uint16)
