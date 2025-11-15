import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import ElasticNet, LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

iris = load_iris()

# Create a DataFrame for easier exploration
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df["sepal area (cm^2)"] = df["sepal length (cm)"] * df["sepal width (cm)"]

feature_names = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal width (cm)",
    # NEW FEATURE:
    "sepal area (cm^2)",
]
target_name = "petal length (cm)"

X = df[feature_names]
y = df[target_name]

# Display basic information
print(f"Dataset shape: {df.shape}")
print(f"Number of samples: {df.shape[0]}")
print(f"Number of features: {df.shape[1] - 1}\n")

# Display the first few rows
print("First 5 rows:")
print(df.head())


# Display statistical summary
print("Statistical Summary:")
print(df.describe())


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=100, random_state=42),
    "KNN Regressor": KNeighborsRegressor(n_neighbors=5),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Support Vector Regressor": SVR(kernel="rbf"),
    "Elastic Net": ElasticNet(),
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    results[name] = {"MSE": mse, "RMSE": rmse, "R²": r2}

for name, metrics in results.items():
    print(
        f"{name:<25}: MSE = {metrics['MSE']:8.4f}, RMSE = {metrics['RMSE']:8.4f}, R² = {metrics['R²']:8.4f}"
    )


# Petal length predictor
sepal_length = 5.84333
sepal_width = 3.057333
petal_width = 1.199333
sepal_area = sepal_length * sepal_width

my_data = {
    "sepal length (cm)": sepal_length,
    "sepal width (cm)": sepal_width,
    "petal width (cm)": petal_width,
    "sepal area (cm^2)": sepal_area,
}

my_iris = pd.DataFrame([my_data])

lr_model = models["Linear Regression"]
rf_model = models["Random Forest"]
xgb_model = models["XGBoost"]
knn_model = models["KNN Regressor"]
gb_model = models["Gradient Boosting"]
dt_model = models["Decision Tree"]


lr_model_prediction = lr_model.predict(my_iris)[0]
rf_model_prediction = rf_model.predict(my_iris)[0]
xgb_model_prediction = xgb_model.predict(my_iris)[0]
knn_model_prediction = knn_model.predict(my_iris)[0]
gb_model_prediction = gb_model.predict(my_iris)[0]
dt_model_prediction = dt_model.predict(my_iris)[0]

print()
print("=" * 50)
print("PETAL LENGTH PREDICTION")
print("=" * 50)
my_data_items = my_data.items()

for my_data_item in my_data_items:
    print(f"{my_data_item[0]}: {my_data_item[1]}")

print("-" * 50)

for model_item in models.items():
    model_name = model_item[0]
    model_prediction = models[model_name].predict(my_iris)[0]
    print(f"{model_name}: {model_prediction:.4f} cm")

print("-" * 50)
