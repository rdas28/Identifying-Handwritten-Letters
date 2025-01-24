Handwritten Character Recognition with Semi-Supervised Learning and GUI

This project presents a Convolutional Neural Network (CNN) model for recognizing handwritten characters, implemented with a semi-supervised learning approach. The model leverages both labeled and unlabeled data to improve accuracy through pseudo-labeling, allowing it to generalize more effectively to new inputs. We employ a confidence-based filtering technique to select high-quality pseudo-labels, enhancing the training process and overall performance.

Features

1.Semi-Supervised Learning: Uses pseudo-labeling on unlabeled data to boost the model’s accuracy and make the most of available data.

2.Confidence Filtering: Applies a confidence threshold to ensure only high-confidence predictions are used, reducing noise in the pseudo-labeled dataset.

3.Alternative Algorithm Exploration: The code structure allows for easy experimentation with alternative algorithms, and future work may explore Vision Transformers, RNNs, and more.

4.Real-Time GUI: A user-friendly graphical interface enables real-time character input, enhancing the user experience and providing immediate feedback on model predictions.

Getting Started

To train and test the model, the MNIST dataset can be downloaded from Kaggle, providing a straightforward way to experiment with handwritten digit recognition. The code is modular, allowing easy adaptation for other character datasets as well.

Future Work

Real-Time Application Enhancements: Researching further methods to improve real-time character recognition, including real-time data augmentation and preprocessing.
Alternative Architectures: Experimenting with advanced architectures like Vision Transformers and LSTM-based models to explore improvements over CNN.
Deployment on Edge Devices: Investigating model compression and optimization for edge devices to support mobile and low-power applications.
This repository is ideal for those interested in semi-supervised learning, computer vision, and interactive machine learning applications. It combines a robust deep learning approach with an interactive GUI, providing a comprehensive solution for handwritten character recognition tasks.
