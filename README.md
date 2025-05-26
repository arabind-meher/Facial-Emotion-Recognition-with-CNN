# Facial Emotion Recognition with CNN

This project focuses on building a Convolutional Neural Network (CNN) from scratch using only NumPy to classify facial emotions. The goal is to deeply understand the mechanics of CNNs by implementing the full image processing and training pipeline manually—without relying on high-level deep learning libraries like TensorFlow or PyTorch.

## 🔍 Objective

- Perform facial emotion recognition on grayscale and color images.
- **Implement Convolutional Neural Networks (CNNs) entirely from scratch using only NumPy** – no PyTorch, TensorFlow, or other deep learning frameworks.
- Experiment with multiple CNN architectures:
  - Single kernel CNN
  - Multi-kernel CNN
  - Multi-layer CNN
- Evaluate model performance using metrics like accuracy and confusion matrix.

## 🗃 Dataset

- **Source**: [Emotion Recognition Dataset on Kaggle](https://www.kaggle.com/datasets/sujaykapadnis/emotion-recognition-dataset)
- **Classes Used**: Angry, Happy, Neutral, Sad, Surprise
- **Preprocessing**:
  - Resized to 48×48 pixels (configurable)
  - Stored in both grayscale and color format
  - Limited to 1000 images per class (configurable)

## 🧱 Project Structure

```
Facial-Emotion-Recognition-with-CNN/
│
├── dataset/
│   ├── gray_data/            # Grayscale processed images
│   └── color_data/           # Color processed images
├── download/                 # Downloaded zip files from Kaggle
├── raw_data/                 # Extracted dataset before processing
├── scripts/
│   ├── downloader.py         # Kaggle dataset downloader
│   ├── image_processor.py    # Image preprocessing with resizing, format conversion
│   ├── file_system.py        # Directory and file utilities
├── prepare_dataset.ps1       # Script to automate download and processing
├── README.md
├── requirements.txt
└── .gitignore
```

## 🚀 Getting Started

1. **Install requirements** (Kaggle API must be configured):
```bash
pip install -r requirements.txt
```

2. **Download and Extract Dataset**:
```bash
python scripts/downloader.py --dataset sujaykapadnis/emotion-recognition-dataset
```

3. **Preprocess Images**:
```bash
python scripts/image_processor.py --read-from raw_data/dataset --write-to dataset --size 48 48 --limit 1000
```

4. **Or run everything at once (Windows)**:
```bash
.\prepare_dataset.ps1
```

## 📌 Next Steps

- Implement CNN architectures using NumPy
- Build a training and evaluation pipeline
- Visualize results and compare performance

## 📄 License

This project is for educational purposes and does not include any proprietary datasets or pre-trained models.
