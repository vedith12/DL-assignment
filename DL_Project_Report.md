# Dog Breed Classification - Project Report

## Project Overview
The objective of this project is to build and evaluate robust deep learning models capable of classifying dog breeds using the Stanford Dogs Dataset (which contains 120 distinct classes). The project systematically tests the limits of various neural network architectures, ranging from basic perceptrons and Multi-Layer Perceptrons (MLPs) to Custom Convolutional Neural Networks (CNNs) and state-of-the-art pretrained architectures utilizing transfer learning, attention mechanisms, and ensemble methods.

## Technologies and Tools Used
*   **Programming Language:** Python
*   **Deep Learning Framework:** TensorFlow and Keras
*   **Libraries:** NumPy, Matplotlib (for visualization), scikit-learn (for baseline algorithms)
*   **Pre-trained Models:** VGG16, ResNet50, MobileNetV2, EfficientNetB0
*   **Environment:** Google Colab / Local IDE

## System Architecture
The overall architecture revolves around an iterative progression through various model paradigms to tackle the non-linear, high-dimensional problem of image classification:
1.  **Data Ingestion & Preprocessing:** Resizing high-definition inputs to fixed dimensions (64x64, 128x128, 224x224), normalizing pixel ranges to `[0, 1]`, and caching the structures.
2.  **Basic Feedforward Pipeline:** Converting image arrays to flattened vectors to establish baseline weights using basic dense layers or perceptrons.
3.  **Convolutional & Regularization Pipeline:** Implementing custom extraction modules utilizing Convolutional Layers, Max-Pooling, Dropout, and L2 constraints to govern overfitting.
4.  **Transfer Learning Pipeline:** Feeding preprocessed images to pre-trained architectures (acting as complex feature extractors) stripped of their top classification layers.
5.  **Attention and Ensemble Architecture:**
    *   **Feature Extraction:** Generating feature maps via EfficientNetB0 and MobileNetV2.
    *   **Attention Mechanism:** Applying weights to regional spatial properties to prioritize distinguishing characteristics (e.g., ears, fur patterns).
    *   **Classification Head:** Global Average Pooling condensed features fed to Softmax Dense aggregators.
    *   **Ensemble:** Averaging the independent probability distributions of the standalone fine-tuned models for stable classification.

## Methodology

### Baseline Binary Classification and Perceptron
Initial experiments were conducted on a subset binary classification task using the McCulloch-Pitts (MP) Perceptron and a standard `scikit-learn` Perceptron. To process inputs, images were flattened to dense 1D arrays. The strict linear limitations inherent to basic perceptrons failed to achieve separability, predicting zeroes universally.

### MLP Training
A vanilla Multi-Layer Perceptron (MLP) was trained employing differing learning rates (e.g., `0.0001`, `0.001`, `0.01`). The simplistic spatial-unaware flattening of pixels predictably struggled. The lower learning rates yielded slow and graduate loss convergence, but the models exhibited significant fluctuation in validation loss and extreme underfitting due to their inability to encode explicit 2D spatial relationships.

### Optimisers Used
To examine converging dynamics, identical topological networks were trained sequentially utilizing different gradient descent engines, inclusive of standard Stochastic Gradient Descent (SGD), Momentum, RMSProp, and Adam. Advanced optimizers like Adam were vital for smoothing the loss curves dynamically compared to constant learning-rate environments.

### Regularization Techniques
Given standard networks' tendencies to memorize small training samples, three active regularization techniques were analyzed:
*   **L2 Regularization (Weight Decay):** Penalizing excessively high neuron weights directly in the loss penalty.
*   **Dropout:** Randomly deactivating a specific ratio of neurons during each batch to force diverse feature mapping.
*   **Early Stopping:** Abstracting validation-loss monitors to cease training when generalization peaks and overfitting initializes.

### CNN Training and Augmentation
A Custom Convolutional Neural Network (CNN) leveraged parameter-sharing and spatial convolutions. A preliminary data augmentation pipeline (Random Flips, Rotations) was established beforehand. This approach massively slowed down initial epoch overfitting and captured spatial texture and shape distributions.

### Pretrained Models
Scaling upwards, the inputs were scaled to `128x128` and pushed across state-of-the-art imagenet-weighted topologies:
*   **VGG16:** Converged modestly with roughly 30% accuracy, acting as primarily a heavy-weight structural validation.
*   **MobileNetV2:** Provided excellent tradeoffs, computing significantly faster epochs while capturing highly accurate parameters (~77.3% Validation Accuracy).
*   **ResNet50:** Explored residual structural leaps preventing vanishing gradients, leaping to an impressive ~90.1% generalization.

### Autoencoder 
An unsupervised exploratory Autoencoder setup was modeled to compress incoming shapes into condensed vectors, subsequently up-sampling them to original scales. Examining the decoded outputs verified the model's fundamental abstract learning characteristics.

### Attention Mechanisms and Ensemble Learning 
For the apex of the methodology, a medium complexity subset of 25 classes (scaled to `224x224`) was trained across an ensemble consisting of `EfficientNetB0` and `MobileNetV2`:
*   **Attention Mechanisms:** The systems were supplemented with attention constraints specifically focusing calculations on critical, distinct facial properties instead of background noise.
*   **Fine-Tuning:** The deeper, abstractly rich layers of the pretrained bases were formally "unfrozen" to allow tight tuning specifically adapted per-dog-breed, rather than generic objects.
*   **Ensemble Evaluation:** Predictions from both fine-tuned architectures were averaged for the final predictions, preventing reliance on a single structural weakness. 

## Screenshots
*(Note: Please insert the relevant notebook graph snapshots corresponding to the following placeholders.)*

*   **Training & Validation Loss Convergence Curves** (Include MLP / Learning Rate / ResNet convergence)
*   **Output Accuracy Metrics over Iterations**
*   **Visualization of Sample Images / Autoencoder Reconstructions**

## Results
*   **Flattened MLP Baseline:** Barely better than random chance (~2.8% Accuracy).
*   **Single CNN Array:** Steady, albeit modest spatial improvement (~13.2% Accuracy).
*   **VGG16 Base:** ~30.4% Validation Accuracy.
*   **MobileNetV2 Base:** ~77.3% Validation Accuracy.
*   **ResNet50 Base:** ~90.1% Validation Accuracy.
*   **Dual Attention Ensemble (MobileNetV2 + EfficientNetB0):** Reached a highly confident **91.2% Validation Accuracy** using a medium subset mapping, successfully combating intense visual similarities between related dog breeds.

## Learning Outcomes
1.  **Architecture Matters:** High-dimensional image tracking with mere spatial un-aware flattening (MLPs) is strictly inefficient. Deep hierarchical feature mapping via convolutions is explicitly mandated.
2.  **Regularization is Key:** Left unchecked, advanced models with massive parameters will aggressively overfit dataset boundaries. Data Augmentations and Dropout are indispensable.
3.  **The Power of Transfer Learning:** Adapting preexisting networks heavily cuts down the requirement for staggering datasets and computationally intensive resources, while bypassing the 'cold-start' optimization issue.
4.  **Ensembles and Attention Multiply Stability:** Combining multiple different architectural approaches allows weaknesses in one framework to be masked by successes in the other. Mapped attention dramatically cuts down confusion stemming from variable background environments.

## Conclusion
This progressive experimentation conclusively proves the difficulty of multi-class high-resolution image predictions. The dataset transitioned from rendering simplistic perceptrons mathematically obsolete entirely, to challenging standalone intermediate CNNs. Through methodical upgrades via Regularization, Transfer Learning, Unfreezing strategies, and ultimate Attention-driven Ensembles, the architecture adapted seamlessly mapping complex textual and physical traits, reaching robust industrial-level accuracy marks exceeding 91%.
