import numpy as np
import imageio as img
import matplotlib.pyplot as plt

image_path = "img.jpeg"
image = img.imread(image_path)


red_channel = np.zeros_like(image)
green_channel = np.zeros_like(image)
blue_channel = np.zeros_like(image)


red_channel[:, :, 0] = image[:, :, 0]  # Only red channel
green_channel[:, :, 1] = image[:, :, 1]  # Only green channel
blue_channel[:, :, 2] = image[:, :, 2]  # Only blue channel

# Titles and images for display
titles = ["Original Image", "Red Channel", "Green Channel", "Blue Channel"]
images = [image, red_channel, green_channel, blue_channel]

plt.figure(figsize=(10, 10))
for idx, (title, img_data) in enumerate(zip(titles, images)):
    plt.subplot(4, 1, idx + 1)
    plt.title(title)
    plt.imshow(img_data)
    plt.axis('off')

plt.tight_layout()
plt.show()
