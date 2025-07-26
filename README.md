# Superstore Sales Analysis - End-to-End Project

**Data Analytics Project** using Python, Jupyter Notebook, Seaborn, Plotly, Matplotlib, Power BI, and Git.

---

## Project Overview

This project presents a comprehensive analysis of the **Superstore Sales dataset**, offering actionable business insights through:

- Exploratory Data Analysis (EDA) in Python
- Data visualization using both code and dashboard tools
- Interactive dashboard using Power BI

The project simulates a real-world analytics pipeline: from **data cleaning** to **insight generation** to **dashboard storytelling**.

---

## Tools & Technologies

| Category            | Tools & Libraries                              |
|---------------------|----------------------------------------------- |
| Language            | Python                                         |
| Data Analysis       | Pandas, NumPy                                  |
| Visualization       | Seaborn, Matplotlib, Plotly                    |
| Dashboard           | Power BI                                       |
| Notebook            | Jupyter Notebook                               |
| IDE                 | VS Code                                        |
| Environment Mgmt    | virtualenv, pipreqs                            |
| Version Control     | Git, GitHub                                    |

---

##  Data Cleaning & Preparation

- Removed missing values and fixed inconsistent data types
- Checked for similar words using fuzzywuzzy
- Parsed date columns and created derived metrics
- Saved cleaned dataset as `.csv` for reuse in Power BI

---

## Exploratory Data Analysis (EDA)

Performed in Jupyter using Seaborn, Matplotlib, and Plotly:

- 📌 Sales by Category/Sub-Category
- 🧑‍💼 Top Customers by Total Spend
- 🌍 Sales Distribution by State and Region
- 🚚 Shipping Mode impact on performance
- 📅 Time-Series Analysis of Sales Trends

> 🖼️ Visuals include interactive bar charts, line plots, and category-wise plots.

📈 Monthly Sales Trend Analysis (2015–2018)
This line chart illustrates the monthly sales trend over the period from January 2015 to December 2018, based on aggregated transactional data.

![Monthly Sales Plot](images/monthly_sales.png)

**Basic Description**:
The x-axis represents the Year-Month (YYYY-MM format), while the y-axis shows Total Sales in monetary units.

Each point on the line corresponds to the total sales for a given month.

The data shows seasonal fluctuations and growth patterns over the four-year period.

**Key Observations**:

Sales Growth:
There is a gradual upward trend in total monthly sales, especially noticeable in late 2017 and throughout 2018.

Peak Months:

Dec 2018 shows the highest sales peak, crossing 120,000 units. Other visible spikes occurred in mid-2015, early 2016, and late 2017.

Volatility:
The chart reveals significant month-to-month variation, indicating:

Promotions?

Seasonal demand?

Market dynamics or external factors?

**Insights & Recommendations**:
Seasonal Campaigns: Analyze months with consistent spikes and plan campaigns accordingly.

Inventory Planning: Ensure high-demand months (e.g., Q4) are stocked adequately.

Further Analysis: Cross-analyze with customer segments, product categories, or regions to pinpoint growth drivers.

**Sales by Product Category:**
This bar plot shows the total sales distribution across the three main product categories:
This visualization was created using Seaborn's barplot for clear comparison of category-level performance.

![Sales by Category](images/sales_by_category.png)







---

## Power BI Dashboard

Using the cleaned dataset, I created an interactive Power BI dashboard including:

- ✅ Regional and state-wise sales insights
- ✅ Top-performing categories and products
- ✅ Filters for Order Date and Category
- ✅ KPI Cards for Total Sales, Sales YOY Growth, Total Orders, Distinct Customers and Avg. Order Value (**Using DAX**)

📁 File: `powerbi/superstore_analysis.pbix`

---



