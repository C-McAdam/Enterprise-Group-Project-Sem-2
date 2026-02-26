# Very basic Linear Regression + Logistic Regression
# Dataset: Student_Performance_2026_Updated.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression

# -----------------------------------------------------
# 1. LOAD DATA
# -----------------------------------------------------

df=pd.read_csv("Student_Performance_2026_Updated.csv")

# ====================
# LINEAR REGRESSION (Line)
# Predict current_sem_CGPA from total_study_hours
# ====================
X = df[["total_study_hours"]]       # Needs to be a 2D table (one column)
y = df["current_sem_CGPA"]          # Target (Numbers)

lin=LinearRegression()
lin.fit(X,y)

# Make a smooth line for the graph
x_line=np.linspace(X["total_study_hours"].min(),X["total_study_hours"].max(),100).reshape(-1,1)
y_line=lin.predict(x_line)

plt.figure()
plt.scatter(X["total_study_hours"],y)
plt.plot(x_line,y_line)
plt.xlabel("total_study_hours")
plt.ylabel("current_sem_CGPA")
plt.title("Very Basic Linear Regression")
plt.show()

print("LINEAR REGRESSION EQUATION:")
print(f"Current Sem_CGPA = {lin.coef_[0]:.2f} * Total Study Hours + {lin.intercept_:.2f}")

# ====================
# LOGISTIC REGRESSION (S-curve)
# Predict Pass/Fail from total_study_hours
# Pass if current_sem_CGPA >= 7.0
# ====================
df["Pass"] = (df["current_sem_CGPA"] >= 8.0).astype(int)

X2 = df[["total_study_hours"]] 
y2 = df["Pass"]    


log = LogisticRegression()
log.fit(X2, y2)

# Smooth S-curve for graph (probabilities)
x_curve = np.linspace(X2["total_study_hours"].min(), X2["total_study_hours"].max(), 100).reshape(-1,1)
p_pass = log.predict_proba(x_curve)[:, 1]   # probability of class "1" (Pass)

plt.figure()
plt.scatter(X2["total_study_hours"],y2)
plt.plot(x_curve,p_pass)
plt.xlabel("total_study_hours")
plt.ylabel("Probability of Passing")
plt.title("Very Basic Logistic Regression")
plt.show()

# print("\nLOGISTIC REGRESSION NUMBERS:")
# print(f"Coefficient = {log.coef_[0][0]:2f}")
# print(f"Intercept = {log.intercept_[0]:.2f}")



