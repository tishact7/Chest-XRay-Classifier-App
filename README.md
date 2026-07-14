[Chest_XRay_Classifier_App_README.md](https://github.com/user-attachments/files/30021238/Chest_XRay_Classifier_App_README.md)

# Chest X-Ray Pathology Classifier — Streamlit Application

A production-ready web application for AI-assisted chest X-ray pathology detection, built with PyTorch and Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chest-xray-classifier-app-tc.streamlit.app)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Overview

This application enables users to upload a chest X-ray image and receive instant AI-powered predictions for 14 common thoracic pathologies. The underlying model is a DenseNet-121 trained via transfer learning on the NIH ChestX-ray14 dataset.

| Pathology | Description |
|-----------|-------------|
| Atelectasis | Collapsed lung tissue |
| Cardiomegaly | Enlarged heart |
| Consolidation | Fluid-filled lung tissue |
| Edema | Fluid accumulation |
| Effusion | Fluid around lungs |
| Emphysema | Damaged air sacs |
| Fibrosis | Scarred lung tissue |
| Hernia | Diaphragmatic hernia |
| Infiltration | Substance accumulation |
| Mass | Abnormal growth |
| Nodule | Small abnormal growth |
| Pleural Thickening | Thickened pleura |
| Pneumonia | Lung infection |
| Pneumothorax | Collapsed lung (air leak) |

> **Clinical Disclaimer**: This tool is for educational and research purposes only. It is NOT a substitute for professional medical diagnosis. Always consult a qualified radiologist or physician.

---

## Live Demo

**Access the deployed application:** [chest-xray-classifier-app-tc.streamlit.app](https://chest-xray-classifier-app-tc.streamlit.app)

![App Screenshot](assets/app_screenshot.png)

---

## Project Structure

```
Chest-XRay-Classifier-App/
├── app.py                 # Main Streamlit application
├── model.py               # Model loading and inference logic
├── utils.py               # Image preprocessing utilities
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container configuration
├── .streamlit/
│   └── config.toml        # Streamlit UI configuration
├── assets/
│   ├── app_screenshot.png # Demo screenshot
│   └── sample_xrays/      # Example images for testing
├── models/
│   └── densenet121_chestxray.pth  # Pre-trained weights (not in repo)
└── README.md
```

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Deep Learning | PyTorch, TorchVision |
| Model | DenseNet-121 (Transfer Learning) |
| Image Processing | PIL, OpenCV |
| Visualization | Matplotlib, Plotly |
| Deployment | Streamlit Cloud / Docker |

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/tishact7/Chest-XRay-Classifier-App.git
cd Chest-XRay-Classifier-App
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Model Weights

The pre-trained model weights are hosted via GitHub Releases due to file size constraints. Download the latest release and place the weights file in:

```
models/densenet121_chestxray.pth
```

Alternatively, train your own model using the [classifier training repository](https://github.com/tishact7/Chest-XRay-Classifier).

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`.

---

## Docker Deployment

```bash
# Build the image
docker build -t chest-xray-app .

# Run the container
docker run -p 8501:8501 chest-xray-app
```

---

## Model Performance

The underlying model was trained on the NIH ChestX-ray14 dataset (112,120 images, 30,805 unique patients):

| Metric | Value |
|--------|-------|
| AUC-ROC (Macro) | ~0.82 |
| AUC-ROC (Micro) | ~0.90 |
| Input Size | 224 x 224 px |
| Architecture | DenseNet-121 |
| Classes | 14 (multi-label) |

Full training details and reproducible notebooks are available in the [Chest-XRay-Classifier](https://github.com/tishact7/Chest-XRay-Classifier) repository.

---

## Usage

1. Upload a chest X-ray image (PNG or JPG supported).
2. View the preprocessed image.
3. Review predicted probability scores for all 14 pathologies.
4. Interpret results using the built-in visualization.

### Supported Image Formats

- `.png`, `.jpg`, `.jpeg`

---

## Configuration

Edit `.streamlit/config.toml` to customize the UI:

```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
font = "sans serif"
```

---

## Sample Output

```json
{
  "Atelectasis": 0.87,
  "Cardiomegaly": 0.12,
  "Consolidation": 0.45,
  "Edema": 0.03,
  "Effusion": 0.91,
  "Emphysema": 0.08,
  "Fibrosis": 0.15,
  "Hernia": 0.01,
  "Infiltration": 0.67,
  "Mass": 0.22,
  "Nodule": 0.34,
  "Pleural_Thickening": 0.19,
  "Pneumonia": 0.55,
  "Pneumothorax": 0.04
}
```

---

## Future Enhancements

- [ ] Grad-CAM visualization to highlight model attention regions
- [ ] Batch upload for processing multiple images simultaneously
- [ ] PDF report generation for clinical documentation
- [ ] DICOM metadata display for patient/study information
- [ ] Model comparison toggle (DenseNet, ResNet, EfficientNet)
- [ ] User-adjustable confidence thresholds

---

## Author

**Tisha Chatterjee**

- Researcher at MIT Critical Data and Stanford
-
- [LinkedIn](https://linkedin.com/in/tishachatterjee) | [GitHub](https://github.com/tishact7)

---

## Acknowledgments

- NIH ChestX-ray14 Dataset — National Institutes of Health
- PyTorch and TorchVision — Meta AI Research
- Streamlit — For streamlined ML deployment

---

## Contact

For questions, collaborations, or feedback:

- Open an [Issue](https://github.com/tishact7/Chest-XRay-Classifier-App/issues)
- Connect on [LinkedIn](https://linkedin.com/in/tishachatterjee)

---

> AI in healthcare should augment, not replace, clinical expertise.
