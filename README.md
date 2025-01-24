Handwritten Character Recognition Using Semi-Supervised Learning and a GUI
This project introduces a Convolutional Neural Network (CNN) designed for recognizing handwritten characters, incorporating a semi-supervised learning approach. By utilizing both labeled and unlabeled data through pseudo-labeling, the model achieves improved accuracy and better generalization to new inputs. A confidence-based filtering mechanism ensures the quality of pseudo-labels, enhancing the training process and overall model performance.

Key Features:

Semi-Supervised Learning: Leverages pseudo-labeling on unlabeled data to maximize data utilization and enhance accuracy.

Confidence Filtering: Implements a thresholding mechanism to include only high-confidence predictions as pseudo-labels, minimizing noise in the training process.

Algorithm Flexibility: Provides a modular code structure, facilitating experimentation with alternative approaches like Vision Transformers, RNNs, and other architectures.

Interactive GUI: Features a user-friendly graphical interface for real-time character input, enabling instant feedback on predictions and enhancing usability.

Getting Started
The model can be trained and tested using the MNIST dataset, easily downloadable from Kaggle, to enable quick experimentation with handwritten digit recognition. The code is designed to be adaptable, allowing seamless application to other character datasets.

Future Directions
Enhanced Real-Time Applications: Exploring advanced methods like real-time data augmentation and preprocessing to improve character recognition in real-world settings.
Alternative Architectures: Investigating modern approaches, including Vision Transformers and LSTM-based models, to identify potential improvements over CNNs.
Edge Deployment: Focusing on model optimization and compression to support deployment on edge devices, enabling mobile and low-power use cases.
