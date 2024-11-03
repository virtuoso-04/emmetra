from scipy.ndimage import gaussian_filter # type: ignore

def denoise(rgb_image, sigma=1):
    # Apply Gaussian filter to each color channel
    denoised_image = rgb_image.copy()
    denoised_image[:, :, 0] = gaussian_filter(rgb_image[:, :, 0], sigma=sigma)
    denoised_image[:, :, 1] = gaussian_filter(rgb_image[:, :, 1], sigma=sigma)
    denoised_image[:, :, 2] = gaussian_filter(rgb_image[:, :, 2], sigma=sigma)
    return denoised_image
