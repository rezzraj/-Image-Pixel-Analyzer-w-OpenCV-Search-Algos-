import cv2
import numpy as np

images1 = []
pixel_sums = []

# Reading grayscale images and calculating pixel sums
for i in range(1, 11):
    img = cv2.imread(f'images/img{i}.jpeg', cv2.IMREAD_GRAYSCALE)
    images1.append(img)
    height, width = img.shape
    pixel_sum = np.int64(0)
    for row in range(height):
        for col in range(width):
            pixel_sum += img[row, col]
    pixel_sums.append((int(pixel_sum), i))  # (sum, image_number)

print('Pixel sums:', pixel_sums)

def linear_search(target):
    comparisons = 0
    for value, image_num in pixel_sums:
        comparisons += 1
        if value == target:
            return f'(Linear Search) Found in image {image_num}, total comparisons {comparisons}'
    return 'Target not found', comparisons

print(linear_search(40310491))

def bubble_sort(pixels):
    n = len(pixels)
    for i in range(n):
        for j in range(0, n-i-1):
            if pixels[j][0] > pixels[j+1][0]:
                pixels[j], pixels[j+1] = pixels[j+1], pixels[j]
    return pixels

sorted_pixels = bubble_sort(pixel_sums.copy())
print('Sorted pixel sums:', sorted_pixels)

def binary_search(target):
    left = 0
    right = len(sorted_pixels) - 1
    comparisons = 0

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        mid_value, image_num = sorted_pixels[mid]
        if mid_value == target:
            return f'(Binary Search) Found in image {image_num}, total comparisons {comparisons}'
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return 'Target not found', comparisons

print(binary_search(29600692))
