# 🏠 Boston Housing Price Prediction

A Machine Learning project that predicts house prices based on housing features using a **Decision Tree Regressor**.

---

## 📌 Project Overview

This project builds a regression model to predict **Boston housing prices** using selected features from the dataset.

The goal is to analyze how housing characteristics influence property prices and to build an interpretable model.

---

## 🧠 Machine Learning Model

The model used in this project:

- **Decision Tree Regressor**
- Hyperparameter tuning using **GridSearchCV**
- Model evaluation using **R² Score**

---

## 📊 Features Used

| Feature | Description               |
| ------- | ------------------------- |
| RM      | Average number of rooms   |
| LSTAT   | % lower status population |
| PTRATIO | Pupil-teacher ratio       |

---

## ⚙️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Plotly Dash (for dashboard)

---

## 📁 Project Structure

```
project/
│
├── model.pkl
├── dashboard.py
├── visuals.py
├── project.ipynb
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install numpy pandas scikit-learn matplotlib dash plotly
```

### 2️⃣ Run the dashboard

```bash
python dashboard.py
```

### 3️⃣ Open in browser

```
http://127.0.0.1:8050
```

---

## 📈 Model Evaluation

Metrics used:

- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

Example result:

```
R² Score: 0.84
RMSE: 4.6
```

---

## 📊 Visualizations

The project includes:

- Model complexity analysis
- Learning curves
- Feature importance visualization
- Interactive prediction dashboard

---

## 🎥 Demo

Example prediction:

```
Input:
RM = 6
LSTAT = 9
PTRATIO = 17.5

Output:
Predicted Price = $464,562,000
```

## Dashboard Preview

## [dashboard](image.png)

## 👨‍💻 Author

Developed by **Samuel Adel**

Machine Learning Student
