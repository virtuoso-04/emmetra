import cv2
import numpy as np
import os
from hdr import *
# Load images and their log exposure times
def load_images_from_folder(folder):
    images = []
    log_exposure_times = []
    
    for i in range(6):  # Assuming 6 images: sample-00 to sample-05
        filename = f'sample-{i:02d}.png'
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
            # Example exposure times (adjust as needed)
            exposure_time = 1 / (2 ** i)
            log_exposure_times.append(np.log(exposure_time))
    
    return images, np.array(log_exposure_times)

def main():
    # Path to your folder containing HDR images
    folder_path = 'example'
    
    # Load images and log exposure times
    images, log_exposure_times = load_images_from_folder(folder_path)
    
    # Check if images were loaded
    if not images:
        print("No images found in the specified folder.")
        return
    
    # Compute HDR image
    hdr_image = computeHDR(images, log_exposure_times)

    # Save or display the HDR image
    cv2.imwrite('hdr_result.jpg', hdr_image)
    cv2.imshow('HDR Image', hdr_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
