import numpy as np
def gamma_correction(rgb_image, gamma=2.2):
    # Normalize and apply gamma correction
    normalized = rgb_image / 4095.0  # Normalizing 12-bit data
    gamma_corrected = np.power(normalized, 1 / gamma) * 255
    return np.clip(gamma_corrected, 0, 255).astype(np.uint8)
