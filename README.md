# Facial Emotion Recognition with CNN

This project focuses on building a Convolutional Neural Network (CNN) from scratch using only NumPy to classify facial emotions. The goal is to deeply understand the mechanics of CNNs by implementing the full image processing and training pipeline manually, without relying on high-level deep learning libraries like TensorFlow or PyTorch.

## 🔍 Objective

- Perform facial emotion recognition on grayscale and color images.
- **Implement Convolutional Neural Networks (CNNs) entirely from scratch using only NumPy.**
- Experiment with multiple CNN architectures:
  - Single kernel CNN
  - Multi-kernel CNN
  - Multi-layer CNN
- Evaluate model performance using metrics like accuracy and the confusion matrix.

## 🗃 Dataset

- **Source**: [Emotion Recognition Dataset on Kaggle](https://www.kaggle.com/datasets/sujaykapadnis/emotion-recognition-dataset)
- **Classes Used**: Angry, Happy, Neutral, Sad, Surprise
- **Preprocessing**:
  - Resized to 48×48 pixels
  - Stored in both grayscale and color formats
  - Limited to 1000 images per class

## 🧱 Project Structure

```
Facial-Emotion-Recognition-with-CNN/
│
├── downloader.py          # Kaggle dataset downloader and extractor
├── image_processor.py     # Preprocess raw data into grayscale and RGB image sets
├── file_system.py         # Utility to read directories and files
├── raw_data/              # Extracted original dataset
├── dataset/
│   ├── gray_data/         # Grayscale processed images
│   └── color_data/        # Color processed images
└── README.md              # Project overview and instructions
```

## 🚀 Getting Started

1. **Install requirements** (Kaggle API must be configured):
```bash
pip install kaggle pillow tqdm
```

2. **Download and Extract Dataset**:
```bash
python downloader.py --dataset sujaykapadnis/emotion-recognition-dataset
```

3. **Preprocess Images**:
```bash
python image_processor.py
```

## 📌 Next Steps

- Implement CNN architectures using NumPy
- Build a training and evaluation pipeline
- Visualize results and compare performance

## 📄 License

This project is for educational purposes and includes no proprietary datasets or pre-trained models.
