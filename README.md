#  U.S. Consumer Spending and Inflation Analysis

This project explores the relationship between **consumer spending**, **inflation**, and **disposable income** using publicly available U.S. economic data. The goal is to build a reproducible data pipeline, clean and merge multiple datasets, and draw insightful economic interpretations through visual analysis.

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

---

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

---

##  Next Steps
- Compute savings rate = (DSPI - Real PCE) / DSPI
- Visualize inflation trends via CPI vs PCEPI
- Add CPI/PCE by category (e.g. food, housing)

---

##  Getting Started
1. Clone this repo
2. Set up a Python environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
---

##  Author
Nguyen Do  
Analyzing macroeconomic trends through Python, pandas, and visual storytelling.

