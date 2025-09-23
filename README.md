# Inflation Rate Prediction Using LSTM Neural Networks
This project uses **historical global inflation data** to build a predictive model for inflation rates using **Recurrent Neural Networks (LSTM)**.  
The model leverages multi-country inflation sequences and incorporates additional features such as the previous year’s inflation and country codes for improved forecasting accuracy.

---

## Features  

- **Data Preprocessing**  
  - Interpolation of missing values  
  - Outlier handling and smoothing  
  - Scaling for stable training  

- **Categorical Encoding**  
  - Country identifiers encoded for model compatibility  

- **Sequence Generation**  
  - Time-series windows created for forecasting  

- **Deep Learning Model**  
  - Stacked LSTM layers with dropout  
  - Early stopping to prevent overfitting  

- **Performance Evaluation**  
  - Metrics: **MAE** and **RMSE**  
  - Visual comparison of actual vs predicted inflation rates  

---

##  Requirements  

- Python 3.x  
- pandas  
- numpy  
- scikit-learn  
- keras (with TensorFlow backend)  
- matplotlib  
