# Dog Breed Classification using Deep Learning

This repository holds the code, analytical reports, and visualizations for a comprehensive deep learning application aimed at classifying fine-grained image data: the diverse cross-sections of dog breeds. By progressing sequentially from simple neural network baselines to robust pre-trained mechanisms, this project showcases empirical state-of-the-art methods resolving intense visual similarities present across different dog breeds.

## Dataset
The models are trained and validated against the **Stanford Dogs Dataset**:
*   **Total Images:** 20,580
*   **Categories:** 120 Distinct Dog Breeds
*   **Challenges Provided:** Complex background clusters, intense inter-class optical similarities, diverse camera geometries.
*   *(Note: Subsets of 2,500 images across 25 breeds were dynamically formed locally for hyperparameter tuning phases).*

## Architectures & Methodology Evaluated

This project explores a strict empirical progression evaluating the mathematical properties of varying vision mechanisms:
1.  **Multi-Layer Perceptron (MLP):** Evaluated strictly as a mathematically isolated baseline, measuring raw performance on flattened image arrays devoid of spatial hierarchy awareness.
2.  **Custom CNN:** Monitored the initial leaps in validation capability utilizing convolutional 2D filters and max-pooling strategies alongside raw Dropout environments.
3.  **Transfer Learning Bases:** Shifted calculations sequentially towards Frozen pre-computed matrices.
    *   `VGG16`
    *   `MobileNetV2`
    *   `ResNet50`
4.  **Attention-Ensemble Framework (Proposed Apex):** Leveraged a parallel ensemble executing representations alongside `MobileNetV2` and `EfficientNetB0`. Integrated regional facial Attention mechanisms and systematically 'unfroze' distinct layers to adapt generically pre-trained weights strictly towards fine-grained animal features.

## Benchmark Accuracies
*(Obtained via Categorical Crossentropy over 25-Class Data Split)*
*   **MLP Baseline:** ~2.8%
*   **VGG16 Transfer:** ~30.4%
*   **MobileNetV2 Instance:** ~77.3%
*   **ResNet50 Instance:** ~90.1%
*   **Dual Attention Ensemble:** **91.2%**

## Repository Contents Highlight
*   **`DL_dogbreedclassifier_latest.ipynb`** : The central Jupyter Notebook establishing dataset pipelines (Augmentation), layer generation, optimizer exploration, and prediction validation.
*   **`DL_Academic_Paper.tex` / `.md` / `.docx`** : Generated IEEE-formatted academic publications automatically structured directly extrapolating local convergence reports.
*   **`plot_convergence.py`** : Standardized utility Python script structured to instantly export high-fidelity IEEE publication-ready training and convergence curves (comparative accuracy and loss matrices).
*   **`parse.py` / `extract_pdf.py`** : Utility analysis modules meant for raw PDF string extraction and dense repetitive Jupyter log truncations.

## Usage

### 1. Requirements Installation
Ensure you have the core Deep Learning frameworks and utility graphing modules installed:
```bash
pip install tensorflow docx pypdf matplotlib seaborn
```

### 2. Plotting the Analytics
For rapid visual analysis of your resulting `.fit()` histories, leverage the custom plotting interface:
```bash
python plot_convergence.py
```
*Outputs `convergence_curves_accuracy.png` directly tailored for academic paper imports.*

### 3. Generating the Academic Word Document
If modifying the local markdown variants of the formal write-ups, export a styled Word Document easily:
```bash
python create_paper_docx.py
```
---
*Authored for advanced Deep Learning empirical vision benchmarking.*
