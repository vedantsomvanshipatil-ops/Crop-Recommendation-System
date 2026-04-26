# Crop-Recommendation-System
# 🌾 Crop Recommendation System

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat-square&logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-Boosting-red?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-ff4b4b?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> A machine learning system that recommends the most suitable crop to grow based on soil NPK values and climatic conditions — helping farmers make smarter, data-driven agricultural decisions.

---

## 📌 Project Overview

Agriculture is one of the most important sectors of the Indian economy, yet many farmers suffer losses due to planting crops that are not suited to their soil or climate. This project addresses that problem by building an intelligent **Crop Recommendation System** using machine learning.

By analyzing key soil parameters — **Nitrogen (N)**, **Phosphorus (P)**, and **Potassium (K)** — along with environmental factors like **temperature**, **humidity**, **pH**, and **rainfall**, the system predicts the most optimal crop to cultivate with high accuracy.

### ✨ Features

- 🔍 **Multi-Model Comparison** — Trains and evaluates 5 ML models side by side (Random Forest, XGBoost, Naive Bayes, SVM, Decision Tree)
- 📊 **Exploratory Data Analysis** — Visualizes feature distributions, correlations, and crop class balance
- 🧪 **Automated Preprocessing** — Feature scaling, label encoding, and stratified train/test splitting
- 🏆 **Best Model Auto-Selection** — Automatically saves the highest-accuracy model
- 🌐 **Interactive Web App** — Clean Streamlit UI with sliders for real-time crop prediction
- 📈 **Top-5 Predictions** — Displays the top 5 recommended crops with confidence percentages
- 💾 **Exportable Model** — Saved via pickle for easy deployment or integration

---

## 🗂️ Dataset

- **Source:** [Kaggle — Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
- **Size:** 2,200 samples | 7 input features | 22 crop classes
- **Missing values:** None

| Feature | Description | Unit |
|---|---|---|
| N | Nitrogen content in soil | kg/ha |
| P | Phosphorus content in soil | kg/ha |
| K | Potassium content in soil | kg/ha |
| temperature | Average temperature | °C |
| humidity | Relative humidity | % |
| ph | Soil pH value | 0–14 |
| rainfall | Average annual rainfall | mm |

---

## ⚙️ Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.8+ |
| ML Models | Scikit-learn, XGBoost |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web App | Streamlit |
| Model Saving | Pickle |

---

## 📊 Model Accuracy Results

All five models were evaluated using an 80/20 train-test split with stratified sampling and 5-fold cross-validation.

| Model | Train Accuracy | Test Accuracy | CV Accuracy |
|---|---|---|---|
| 🥇 Naive Bayes | 99.6% | **99.5%** | 99.5% |
| 🥈 Random Forest | 100% | **99.3%** | 99.3% |
| 🥉 XGBoost | 100% | **99.1%** | 99.2% |
| Decision Tree | 100% | **98.6%** | 98.5% |
| SVM | 98.1% | **97.5%** | 97.6% |

### 🔑 Key Observations

- All models exceed **97% accuracy**, indicating strong feature-label correlations in the dataset.
- **Naive Bayes** achieves the highest test accuracy due to the near-Gaussian distribution of soil features.
- **Random Forest & XGBoost** are the most robust choices — high accuracy with minimal overfitting risk.
- **NPK values and pH** are the top contributing features according to Random Forest feature importance.
- 5-fold cross-validation confirms that no model is significantly overfitting the training data.

### 📋 Classification Metrics (Best Model — Naive Bayes)

| Metric | Score |
|---|---|
| Accuracy | 99.5% |
| Precision (Macro) | 99.4% |
| Recall (Macro) | 99.5% |
| F1-Score (Macro) | 99.4% |

---

## 🔮 Future Scope

This project lays a strong foundation that can be extended in several directions:

### 📡 Data & Input Enhancements
- [ ] Integrate **real-time soil sensor data** via IoT devices for live recommendations
- [ ] Connect to a **weather API** (e.g., OpenWeatherMap) to auto-fill temperature, humidity, and rainfall
- [ ] Expand the dataset with more regional crop varieties and soil types from India

### 🤖 Model Improvements
- [ ] Experiment with **deep learning models** (e.g., neural networks) for comparison
- [ ] Add **SHAP (SHapley Additive exPlanations)** for model interpretability
- [ ] Implement **hyperparameter tuning** with GridSearchCV or Optuna for further accuracy gains
- [ ] Build an **ensemble/stacking model** combining top performers

### 📱 Deployment & Accessibility
- [ ] Deploy the Streamlit app to **Streamlit Cloud** or **Heroku** for public access
- [ ] Build a **mobile-friendly version** using Flutter or React Native
- [ ] Create a **REST API** using FastAPI so third-party apps can query predictions
- [ ] Add **multilingual support** (Hindi, Marathi, Telugu) for accessibility in rural India

### 📊 Analytics & Reporting
- [ ] Add a **crop calendar** feature suggesting the best planting seasons
- [ ] Include **fertilizer recommendation** as a companion module
- [ ] Generate downloadable **soil health reports** as PDFs

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m "Add: your feature description"`
4. **Push** to the branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

Please make sure your code follows PEP8 style guidelines and includes comments where necessary. For major changes, open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

**VEDANT SOMVANSHI**
B.E. Computer Engineering | 2026
📧 vedantsomvanshipatil@gmamil.com
🔗 [LinkedIn](www.linkedin.com/in/vedanth-somwanshi-2ba87a315) | [GitHub]((https://github.com/vedantsomvanshipatil))

---

*If you found this project helpful, please consider giving it a ⭐ on GitHub!*
