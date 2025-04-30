#  U.S. Consumer Spending and Inflation Analysis

This project explores the relationship between **consumer spending**, **inflation**, and **disposable income** using publicly available U.S. economic data. The goal is to build a reproducible data pipeline, clean and merge multiple datasets, and draw insightful economic interpretations through visual analysis.

---

## Objectives
- Forecast U.S. inflation (CPI YoY %) using time series models
- Compare traditional SARIMA with machine learning-based Random Forest
- Visualize and evaluate model performance with proper metrics

---

##  Data Sources

- **Consumer Price Index (CPI)**  
  Source: FRED ([CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL))

- **Personal Consumption Expenditures (PCE)**  
  Source: FRED ([PCE](https://fred.stlouisfed.org/series/PCE))

- **Disposable Personal Income (DSPI)**  
  Source: FRED ([DSPI](https://fred.stlouisfed.org/series/DSPI))

- **PCE Price Index (PCEPI)**  
  Source: FRED ([PCEPI](https://fred.stlouisfed.org/series/PCEPI))

---

##  Data Cleaning
All raw datasets were loaded, cleaned using `drop_and_save.py`, and saved to the `data/processed` folder. Columns such as `realtime_start` and `realtime_end` were dropped, and rows with missing values were removed.

___

##  Key Analysis

###  Real vs Nominal PCE
- **Real PCE** (inflation-adjusted) was **higher than nominal** during 2010–2016, reflecting strong purchasing power and low inflation.
- After COVID-19 (2020), **Nominal PCE began to outpace Real PCE**, indicating that spending increases were mostly price-driven, not volume-driven.

###  DSPI vs Real PCE
- In the early 2010s, **Real PCE exceeded DSPI**, suggesting consumers spent most or all of their disposable income.
- Post-2016, DSPI consistently outpaced Real PCE, possibly due to higher income levels, increased savings behavior, or economic caution.
- Major spikes in DSPI during 2020–2021 align with **federal stimulus programs**: direct payments, enhanced unemployment, and child tax credits.

###  COVID-19 Annotations
Plots include a **vertical line marking March 2020**, the start of the pandemic’s economic impact, to help interpret sharp dips or spikes in the data.

### The Saving Rates
- The Savings Rate analysis confirms that during the 2010s, consumers spent most of their disposable income, maintaining low savings rates. 
- In contrast, the pandemic period (2020–2021) saw a dramatic surge in savings as government stimulus raised incomes while spending opportunities shrank. 
- As inflation rose post-pandemic, the savings rate declined, reflecting increasing cost pressures on households. 

### Inflation Trends (CPI - PCEPI)
- Although the CPI index is always numerically higher than the PCEPI index due to different weighting methods and base years, both CPI and PCEPI inflation rates track the underlying price movements in the economy. 
- Significant inflation is observed when the year-over-year rates of CPI and PCEPI spike sharply together, such as the notable surge during 2021–2022 following pandemic-related disruptions and fiscal stimulus.

### COVID 19 Economic Effects
- Sharp dip in Real PCE during early 2020 (lockdowns).
- Spikes in DSPI from fiscal stimulus (stimulus checks, enhanced unemployment benefits).
- Elevated inflation starting from mid-2021, coinciding with supply chain disruptions and strong demand recovery.

### CPI Growth vs DSPI Growth Relationship
- Scatter plot and correlation analysis show a very weak negative relationship between CPI growth rates and DSPI growth rates (correlation ≈ -0.10).
- This suggests that changes in consumer prices (inflation) and changes in disposable personal income growth are largely independent.
- Major economic events (like COVID-19 stimulus) can cause large income fluctuations without proportionate changes in inflation rates.

---

## Data Forecasting - Inflation trends

### Models Implemented:

- **SARIMA**: Classical time series model (statsmodels)
  - Grid search over seasonal and non-seasonal parameters
  - Captured trend, but lagged in responding to sharp changes
  - MAE: ~0.42 | RMSE: ~0.55 | MAPE: ~12.5%

- **Random Forest Regressor**: Lag-based ML model (sklearn)
  - Feature engineered using 12 lag variables
  - Tuned via GridSearchCV for optimal parameters
  - MAE: 0.176 | RMSE: 0.044 | MAPE: 6.23%
  - Outperformed SARIMA on all test metrics

### Visuals:
- Line plot: Actual vs SARIMA vs RF forecasts
- Error comparison: Table + Bar chart 

---

##  Author
Nguyen Do  
Nguyen Do — [LinkedIn](https://www.linkedin.com) | Data & Analytics Portfolio  
Currently pursuing advanced analytics in economic trends and financial forecasting.

---

## 📉 Visual Output

### Forecast Comparison:
![Forecast](figures/inflation_model_comparison.png)

### Error Metrics Comparison:
![Metrics](figures/forecast_error_metrics.png)

