import numpy as np

def white_balance(rgb_image):
    # Gray world assumption for white balance
    mean_r = np.mean(rgb_image[:, :, 0])
    mean_g = np.mean(rgb_image[:, :, 1])
    mean_b = np.mean(rgb_image[:, :, 2])
    
    avg_gray = (mean_r + mean_g + mean_b) / 3
    scale_r = avg_gray / mean_r
    scale_g = avg_gray / mean_g
    scale_b = avg_gray / mean_b

    # Apply scaling factors to each channel
    rgb_image[:, :, 0] = np.clip(rgb_image[:, :, 0] * scale_r, 0, 4095)
    rgb_image[:, :, 1] = np.clip(rgb_image[:, :, 1] * scale_g, 0, 4095)
    rgb_image[:, :, 2] = np.clip(rgb_image[:, :, 2] * scale_b, 0, 4095)
    
    return rgb_image.astype(np.uint16)
