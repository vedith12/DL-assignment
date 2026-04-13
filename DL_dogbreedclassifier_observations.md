# Deep Learning Dog Breed Classifier: Key Observations

## Initial Data Loading & Preprocessing
* **Loading the Dataset:** The Stanford Dogs dataset was successfully mounted from Google Drive and unzipped, revealing a massive directory of thousands of images.
* **Metadata Extraction:** When reading the files into a TensorFlow dataset, the system correctly identified that there are 20,580 images distributed across 120 unique dog breed classes.
* **Establishing a Baseline Model:** After splitting the raw data (80% training, 20% testing), an initial sequential Convolutional Neural Network (CNN) was built from scratch and trained for 5 epochs. The plotted training history showed the loss steadily decreasing and accuracy improving, although signs of overfitting were clear as the training accuracy rapidly outpaced the validation accuracy.

## Testing Early DL Concepts (MP Neuron & Perceptron)
* **Breaking Down the Image (Flattening):** To test the simplest historical neural network models, the 2D color images had to be flattened into massive 1D vectors for the models to process them since perceptrons don't understand 2D spatial layouts. The $64 \times 64$ images with 3 RGB channels became arrays with a shape of `(6400, 12288)`.
* **Binary Transformations:** The McCulloch-Pitts (MP) Perceptron is strictly binary. To accommodate this, the pixel intensities were mapped to pure `0`s and `1`s using a threshold. 
* **Perceptron Failures:** Testing both the strict MP Perceptron and a basic weighted Perceptron model on the flattened dataset yielded terrible results—the models just predicted `0` across the board, demonstrating their inability to comprehend complex spatial image data.

## Diagnosing Dataset Imbalance
* **Target Count Investigation:** An investigation into the target variables revealed why the simple perceptron models defaulted to an array of zeros. In the binary test, there were only 54 positive samples and 6,346 negative samples. Because the dataset was highly imbalanced, the simplistic models learned to just predict the dominant class (0) every time to artificially pad their accuracy metrics.

## Hyperparameter Tuning
* **Experimenting with Learning Rates:** By looping through a list of potential learning rates (like `0.0001` and `0.001`), the plotted charts demonstrated how aggressively high learning rates cause the training loss to spike and become unstable, while the lower, optimal learning rates showed a smoother, more reliable convergence. 
* **Comparing Optimizers:** The model was tested against various optimizers (such as standard SGD and more adaptive ones). The visualizations proved that leveraging adaptive optimizers allowed the network to learn and converge significantly faster than standard Stochastic Gradient Descent.

## Implementation of Overfitting Prevention Strategies
* **Scaling Down for Rapid Testing:** A miniature dataset subset of 1000 images and 10 classes was created. This smart strategy allowed for the rapid execution of experiments without waiting hours for the full dataset to train.
* **Applying Regularization:** Three distinct strategies were tested independently: L2 Regularization, Dropout layers, and Early Stopping mechanisms. 
* **Early Stopping Success:** The Early Stopping mechanism successfully halted execution right when the validation loss started to plateau, saving computing time and preventing the model from memorizing the noise in the training set.
* **Data Augmentation:** Scaling back to a medium dataset (2500 files), real-time data augmentation (flipping, rotating) was introduced. While the initial training accuracy took a momentary dip, the overall generalizability improved significantly, closing the gap between training and validation accuracy curves. 

## Advancing to Transfer Learning 
* **Importing Pre-trained Architectures:** State-of-the-art model architectures like `VGG16`, `ResNet`, and `MobileNet` were pulled into the notebook, along with their completely pre-trained weights.
* **ResNet Superiority:** Because these models already "know" how to identify basic geometric shapes and edges, the `ResNet` model began its very first training epoch with a massively higher starting accuracy compared to our scratch-built CNN. 

## Single Image Inference
* **End-to-End Prediction:** Fetching a random sample image from the test set, the chosen model required about 5 seconds to run the inference step. It successfully mapped the output tensors back directly to a readable string, displaying the predicted dog breed accurately next to the plotted image.
## Detailed Observations (Weeks 6, 7, & 8)

### Week 6: Building a Real CNN
* **Scaling to more Classes:** We moved up to a "medium" dataset with 25 dog breeds and 2500 images.
* **CNN Architecture:** Instead of just flat layers, we used `Conv2D` and `MaxPooling2D`. This helps the model see spatial features like ears or patterns.
* **Data Augmentation:** We added random flipping and zooming to the images.
* **Performance:** I got about **13.2% accuracy** in just 5 epochs. It's a low start, but it shows more potential than the previous flat models.

### Week 7: Transfer Learning (Pre-trained Models)
* **VGG16:** Using a pre-trained VGG16 model with 25 classes, I got around **30.3% accuracy**. It's much better than my scratch-built CNN!
* **ResNet50:** This was the best! After I fixed the image size to 224x224 and added the proper `preprocess_input` line, the accuracy jumped to **90.0%**. It shows how important it is to use the same setup the model was originally trained on.
* **MobileNetV2:** This model gave me about **77.2% accuracy**. It's not as good as ResNet, but it's very fast and would be good for a mobile phone app.

### Week 8: Advanced Visualisation
* **Feature Maps:** I plotted the filters from the first layer. I can see the neural network is looking for basic things like edges, colors, and textures of the dog's fur.
* **Heatmaps (Grad-CAM):** We created a heatmap to overlay on our test images. It confirmed that the model is actually looking at the dog's face and body to make its choice, which is really cool to see.

### Regularization Summary
*   **Dropout:** I added dropout layers of 0.5 to stop the model from memorizing the data. The accuracy was about **16.5%**. It's stable but slow. 
*   **Early Stopping:** This stopped the training at Epoch 7 because the validation loss wasn't improving. It saved time and gave me about **24.5% accuracy**, which is my best result for the simple models.

### Autoencoders
* **Compression and Reconstruction:** This model is different because it doesn't predict a breed. Instead, it tries to rebuild the image it was given. 
* **The "Latent" Bottleneck:** It compresses the $64 \times 64$ image into a smaller representation (Encoder) and then blows it back up (Decoder). 
* **Performance:** I noticed the "Reconstructed" image looks a bit blurry compared to the "Original," but the colors and shapes are almost the same. It's cool how the model can learn to redraw a dog after seeing it!

