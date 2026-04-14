# Dog Breed Classification using Deep Learning

This repository holds the central Jupyter Notebook and evaluation graphs for a comprehensive deep learning application aimed at classifying fine-grained image data: the diverse cross-sections of dog breeds. By progressing sequentially from simple neural network baselines to robust pre-trained mechanisms, this project showcases empirical state-of-the-art methods resolving intense visual similarities present across different dog breeds.

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

## Repository Contents
*   **`DL_dogbreedclassifier_latest.ipynb`** : The central executed Jupyter Notebook establishing dataset pipelines (Augmentation), layer generation, optimizer exploration, and prediction validation.
*   **`Graphs/`** *(or root images)*: High-fidelity convergence curves (comparative accuracy and loss matrices) plotting the validation capabilities across architectures.

## Usage

### Exploring the Notebook
You can view the main `DL_dogbreedclassifier_latest.ipynb` directly through GitHub or open it in your preferred environment (like Google Colab or Jupyter Lab). The notebook is cleanly separated into modules demonstrating data processing all the way to ensemble prediction.

### Viewing the Results
The convergence graphs (Accuracy/Loss curves) provided alongside the notebook illustrate the exact points at which traditional CNNs plateaued while Transfer Learning and Attention-based Ensemble models learned successfully and generalized robustly.

---
*Authored for advanced Deep Learning empirical vision benchmarking.*
