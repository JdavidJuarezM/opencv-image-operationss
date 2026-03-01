<div align="center">

# 🖼️ OpenCV Image Operations

**A computer vision script demonstrating arithmetic and bitwise image transformations**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](#)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](#)

*A Python-based utility that utilizes OpenCV to perform fundamental mathematical and logical operations on image matrices, generating comprehensive visual outputs for each transformation.*

</div>

<br />

## 📑 Table of Contents
- [✨ Key Features](#-key-features)
- [🏗️ Architecture & Structure](#️-architecture--structure)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Execution](#execution)
- [🛠️ Tech Stack](#️-tech-stack)

---

## ✨ Key Features

* **✔️ Arithmetic Operations:** Computes pixel-by-pixel addition (`suma.jpg`), subtraction (`resta.jpg`), multiplication (`multiplicacion.jpg`), and division (`division.jpg`) between two images.
* **✔️ Bitwise (Logical) Operations:** Applies logical gates to image matrices, useful for masking and region extraction. Includes AND (`bitwise_and.jpg`), OR (`bitwise_or.jpg`), XOR (`bitwise_xor.jpg`), and NOT (`bitwise_not.jpg`).
* **✔️ Matrix Manipulation:** Leverages underlying NumPy arrays to properly handle image data blending and clipping without exceeding RGB thresholds (0-255).
* **✔️ Automated Export:** Automatically processes the input images and saves all resulting transformed images into a dedicated `resultados/` directory.

---

## 🏗️ Architecture & Structure

The repository is kept highly focused on the core computer vision mathematical transformations:

```text
opencv-image-operationss/
├── operaciones_imagenes.py      # Main script containing all arithmetic and bitwise logic
├── original.jpg                 # Input image 1
├── original2.jpg                # Input image 2
├── resultados/                  # Automatically generated outputs
│   ├── suma.jpg                 # Blended addition result
│   ├── resta.jpg                # Subtracted image result
│   ├── multiplicacion.jpg       # Multiplied matrix result
│   ├── division.jpg             # Divided matrix result
│   ├── bitwise_and.jpg          # Logical AND intersection
│   ├── bitwise_or.jpg           # Logical OR union
│   ├── bitwise_xor.jpg          # Logical XOR
│   ├── bitwise_not_1.jpg        # Logical NOT (Inverted Image 1)
│   └── bitwise_not_2.jpg        # Logical NOT (Inverted Image 2)
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

To run this project, ensure you have Python installed on your local machine along with the required computer vision and matrix calculation libraries:

* **Python:** Version 3.x
* **OpenCV:** For image processing (`cv2`)
* **NumPy:** For advanced array and matrix operations (`numpy`)

You can install the required dependencies using pip:
```bash
pip install opencv-python numpy
```

### Execution

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd opencv-image-operationss
   ```
3. Run the Python script:
   ```bash
   python operaciones_imagenes.py
   ```
4. The script will read `original.jpg` and `original2.jpg`, process them using various mathematical operations, and save the resulting images inside the `resultados/` folder.

---

## 🛠️ Tech Stack

* **Python** - Core programming language
* **OpenCV (`cv2`)** - Computer Vision and image array manipulation
* **NumPy (`np`)** - Under-the-hood matrix mathematics and type handling

<br />

<div align="center">
  <i>Developed with ☕ to explore Matrix Mathematics in Computer Vision.</i>
</div>
