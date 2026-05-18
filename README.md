# Python-image-mirror-reflection

Image Processing Toolkit
A collection of custom image‑processing functions built using Python, NumPy, and PIL.

Overview
This project contains three image‑processing tools I originally wrote almost 6 years ago by the time no AI. Today is May 18, 2026. I am using AI to help me add notes to give a descrition about my script.
Each function manipulates images at the pixel‑array level, using NumPy to reshape, slice, reverse, and reconstruct images manually.

The toolkit includes:
Grayscale Reflection Tool:mirror effects on grayscale images
Thresholding Tool:convert grayscale images to binary black/white
RGB Reflection Tool:mirror effects on full‑color images

These functions demonstrate foundational image‑processing logic without relying on high‑level libraries.

Technologies Used
  Python
  NumPy
  Pillow (PIL)

Features
1. Grayscale Reflection (reflection_change())
Creates vertical or horizontal mirror effects on grayscale images.

User Inputs
Percentage (-50 to 50)  
Controls how much of the image is reflected.

Positive → reflect lower/right portion
Negative → reflect upper/left portion
Zero → no reflection

Direction
v → vertical reflection
h → horizontal reflection

Image Path  
Full path to the input image.

How It Works
Code
Input Image
      ▼
Convert to grayscale → NumPy array
      ▼
Compute reflection slice based on percentage
      ▼
Reverse slice (mirror effect)
      ▼
Merge slice back into original array
      ▼
Reconstruct final image → Show result
      └──► Optional: Save as reflection.jpg

2. Thresholding Tool (change_threshold())
Converts a grayscale image into a binary black‑and‑white image using a threshold between 0 and 255.

User Inputs
Threshold (0–255)
Pixels ≤ threshold → black
Pixels > threshold → white

Image Path
How It Works

Code
Input Image
      ▼
Convert to grayscale → NumPy array
      ▼
For each pixel:
    if pixel ≤ threshold → 0 (black)
    else → 255 (white)
      ▼
Reconstruct binary image → Show result
      └──► Optional: Save as threshold.jpg
Threshold Meaning
0 → all white
255 → all black
Low threshold → more white
High threshold → more black

3. RGB Reflection Tool (reflection_rgb())
Creates vertical or horizontal mirror effects on full‑color RGB images.
This is the most advanced function in the toolkit — it performs reflection on 3‑channel pixel arrays.

User Inputs
Percentage (-50 to 50)  
Controls reflection intensity.

Direction (v / h)  
Vertical or horizontal reflection.

Image Path

How It Works
Code
Input RGB Image
      ▼
Convert to NumPy array (H × W × 3)
      ▼
Compute reflection slice based on percentage
      ▼
Reverse slice (mirror effect)
      ▼
Merge slice back into original RGB array
      ▼
Reconstruct final RGB image → Show result
      └──► Optional: Save as reflectionRGB.jpg
Reflection Logic
Vertical reflection  
Slice rows → reverse → merge → reshape → RGB image

Horizontal reflection  
Slice columns → reverse → merge → reshape → RGB image

Output
A full‑color mirrored image saved as:

reflection.jpg

Grayscale Reflection:  
Example (-40,v)
A lotus image with a 20% vertical mirrored reflection.
Thresholding:  
Example (128)
A high‑contrast black‑and‑white silhouette using threshold 50.
RGB Reflection:
Excample (-40,V)
A pink lotus reflected vertically in full color.



🎯 Purpose of This Project
This project showcases early image‑processing techniques implemented manually:
Pixel‑level manipulation
Array slicing and reversing
Thresholding logic
RGB and grayscale handling
User‑interactive command‑line tools
It highlights algorithmic thinking and foundational understanding of how images are represented as numerical arrays.





