import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

# Sample data
years = np.arange(2010, 2023)
countries = ['USA', 'China', 'Japan', 'Germany', 'India']
gdp = np.array([
    [14964.4, 15542.6, 16197.0, 16784.2, 17427.6, 18120.7, 18857.0, 19542.3, 20242.5, 20928.8, 21664.8, 22415.2, 23191.9],
    [6104.3, 7551.4, 9240.3, 10587.4, 12038.2, 13608.2, 15308.8, 17098.7, 18897.5, 20732.3, 22567.4, 24450.3, 26389.2],
    [5960.5, 5704.5, 6203.2, 6206.9, 5154.2, 4603.4, 4860.2, 4383.1, 4895.4, 4850.6, 5374.2, 5520.4, 5080.2],
    [3339.5, 3416.8, 3581.6, 3693.2, 3840.2, 3978.9, 4113.9, 4259.3, 4399.5, 4524.9, 4658.9, 4793.4, 4932.3],
    [1679.0, 1874.8, 2064.7, 2263.8, 2469.3, 2684.3, 2907.4, 3139.8, 3379.9, 3627.9, 3884.7, 4149.4, 4422.2]
])

# Normalize the data
gdp_norm = gdp / np.max(gdp)

# Create a video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('gdp.mp4', fourcc, 1, (800, 600))

# Create a bar chart for each year
for i, year in enumerate(years):
    plt.bar(countries, gdp_norm[:, i])
    plt.title(f'GDP per country in {year}')
    plt.xlabel('Country')
    plt.ylabel('Normalized GDP')
    plt.ylim([0, 1])
    plt.savefig(f'{year}.png')
    plt.clf()

    # Add the bar chart to the video
    img = cv2.imread(f'{year}.png')
    img = cv2.resize(img, (800, 600))
    video.write(img)

    # Remove the image file
    os.remove(f'{year}.png')

# Release the video
video.release()
