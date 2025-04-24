# U.S. Consumer Spending & Inflation Trends (2025)

# Overview

This project explores how U.S. consumer spending has evolved over time, focusing on its relationship with inflation across various categories like food, housing, and energy.

It uses the FRED API to fetch economic indicators and builds a reproducible pipeline for data retrieval, transformation, and future analysis.

---

## Tools Used

- Python 3.12 (Anaconda)
- Requests
- Pandas
- FRED API
- Dotenv
- VS Code + GitHub

---

## Data Sources

- **FRED (Federal Reserve Economic Data)** via API
  - [`PCE`](https://fred.stlouisfed.org/series/PCE): Personal Consumption Expenditures
  - `CPIAUCSL`: CPI (All Urban Consumers)
  - `CPIENGSL`: CPI – Energy
  - `CPIFABSL`: CPI – Food & Beverages
  - `CPIHOSSL`: CPI – Housing
  - `PCEPILFE`: PCE Excluding Food & Energy

---


---

## 🛠️ How to Use

### 1. Add your API Key

Create a `.env` file in the root folder with:
FRED_API_KEY=your_actual_key_here


### 2. Run the Data Fetch Script

```bash
python scripts/fetch_fred_data.py

---
Author
Nguyen Do 