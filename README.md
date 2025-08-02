# **Image Pixel Sum Analysis with Searching & Sorting**

### **Overview**
This project processes **grayscale images**, calculates the **sum of pixel values for each image**, and applies **searching and sorting algorithms** to analyze the data.  
It demonstrates the implementation of **Linear Search**, **Binary Search**, and **Bubble Sort** in a real-world context using image processing.

---

## **Features**
✔ Reads multiple **grayscale images**  
✔ Calculates **total pixel intensity sum** for each image  
✔ Implements **Linear Search** to find a specific pixel sum  
✔ Sorts the list of pixel sums using **Bubble Sort**  
✔ Uses **Binary Search** for efficient searching after sorting  
✔ Displays **comparisons count** for each search algorithm  

---

## **Workflow**
1. **Image Reading:** Loads a set of images in grayscale mode.
2. **Pixel Sum Calculation:** Computes the sum of all pixel values for each image.
3. **Linear Search:** Searches for a target pixel sum in the unsorted list.
4. **Bubble Sort:** Sorts the pixel sums in ascending order.
5. **Binary Search:** Searches for a target pixel sum in the sorted list.

---

## **Example Output**
- **Pixel sums:**  
[(40310491, 1), (29600692, 2), (32894567, 3), ...]
- **Linear Search Result:**  
`(Linear Search) Found in image 1, total comparisons 1`
- **Sorted Pixel Sums:**  
[(29600692, 2), (32894567, 3), (40310491, 1), ...]

- **Binary Search Result:**  
`(Binary Search) Found in image 2, total comparisons 3`

---

## **Applications**
- Understanding **basic image processing concepts**
- Demonstrating **searching & sorting algorithms** on real data
- Comparing **efficiency** of linear vs. binary search

---

## **Requirements**
- Python 3.x
- Libraries:
- `opencv-python`
- `numpy`

---

## **Why This Project?**
✅ Combines **image processing** with **data structure concepts**  
✅ Provides a **hands-on example** for algorithm analysis  
✅ Useful for **students learning computer vision & algorithms**

---

## **Future Enhancements**
- Replace **Bubble Sort** with more efficient algorithms (e.g., Quick Sort, Merge Sort)
- Add **visualizations** for pixel sum distribution
- Support **different image formats and color modes**

---
