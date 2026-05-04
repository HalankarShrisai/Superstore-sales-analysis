# Superstore-sales-analysis
End-to-end EDA on retail sales data using Python, Pandas and Matplotlib
# 🛒 Superstore Sales Analysis

An end-to-end exploratory data analysis (EDA) project on the Sample Superstore retail dataset.  
Built to practice real-world data analyst skills — cleaning, querying, visualising, and reporting.

---

## 📌 Business Questions Answered

| # | Question | Tool Used |
|---|----------|-----------|
| 1 | Which region generates the highest sales? | `groupby` + `sort_values` |
| 2 | Which product category is least profitable? | `groupby` + `sum` |
| 3 | Which sub-categories have negative profit and should be discontinued? | Boolean filtering |
| 4 | What is the average profit margin by customer segment? | Derived column + `mean` |
| 5 | Which 5 states are losing the most money? | `nsmallest` |

---

## 📊 Visualisations

| Chart | Type | Insight |
|-------|------|---------|
| Sales by Region | Horizontal Bar | West leads; South lags |
| Monthly Sales Trend | Line + Fill | Clear year-end spikes (Q4) |
| Sales by Category | Pie | Technology dominates at ~37% |

Charts exported as `superstore_charts.png`.

---

## 🗂️ Project Structure

```
superstore-sales-analysis/
│
├── Superstore.csv              # Raw dataset
├── superstore_analysis.py      # Main analysis script
├── superstore_charts.png       # Output charts
├── superstore_summary.xlsx     # Formatted Excel report
└── README.md
```

---

## 🔧 Tech Stack

- **Python 3.12**
- **Pandas** — data loading, cleaning, aggregation
- **Matplotlib** — visualisations
- **OpenPyXL** — Excel export with conditional formatting

---

## ▶️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/superstore-sales-analysis.git
cd superstore-sales-analysis

# 2. Install dependencies
pip install pandas matplotlib openpyxl

# 3. Run the analysis
python superstore_analysis.py

git clone https://github.com/HalankarShrisai/superstore-sales-analysis.git
```

---

## 💡 Key Findings

- **West region** has the highest total sales (~$725K), followed by East
- **Furniture** is the least profitable category; **Tables** and **Bookcases** operate at a net loss
- **Technology** has the best profit margins despite mid-range sales volume
- **Texas, Ohio, and Pennsylvania** are the top 3 loss-making states — driven by heavy discounting
- Sales spike significantly in **Q4 (Oct–Dec)** every year, suggesting seasonal demand

---

## 👤 Author

**Shrisai Halankar**  
B.Tech — Electronics & Computer Science, VIT Mumbai (2026)  
Aspiring Data Analyst  

[![LinkedIn](https://www.linkedin.com/in/shrisai-halankar-297a18299/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/HalankarShrisai)

