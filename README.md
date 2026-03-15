# Movie Data Analysis

Exploratory data analysis of movie datasets covering box office performance, ratings, genre trends, and inflation-adjusted ROI. Built as a personal project to practice data cleaning, merging datasets, and visualization with Python.

## What's Covered

- Data cleaning and null handling across multiple datasets
- Merging movie metadata with ratings and financial data
- Inflation adjustment of historical box office revenue using CPI data
- ROI calculation (budget vs. revenue)
- Interactive visualizations with Plotly
- Static plots with Matplotlib

## Datasets

| File | Description |
|------|-------------|
| `movies.csv` | Core movie metadata (title, genre, year, budget, revenue) |
| `movieratings.xlsx` | Audience and critic ratings |
| `US CPI.csv` | US Consumer Price Index for inflation adjustment |
| `food_price_inflation.csv` | Supplementary inflation data |

## Project Structure

```
movie-data-analysis/
├── Movie_Graph/
│   ├── movies.ipynb              # Main analysis notebook (Plotly)
│   └── movieGraph_matplot.py     # Matplotlib version of key charts
├── movies.html                   # Exported interactive Plotly chart
├── movies.csv
├── movieratings.xlsx
├── US CPI.csv
└── food_price_inflation.csv
```

## Requirements

```
pandas
numpy
matplotlib
plotly
openpyxl
```

Install with:
```bash
pip install pandas numpy matplotlib plotly openpyxl
```

## Usage

Open the notebook in Jupyter:

```bash
jupyter notebook Movie_Graph/movies.ipynb
```

Or run the matplotlib script directly:

```bash
python Movie_Graph/movieGraph_matplot.py
```

---

*Hidekel Irizarry | Mechanical Engineering @ UCF*
