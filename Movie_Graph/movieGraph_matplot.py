import pandas as pd
from matplotlib import pyplot as plt
from adjustText import adjust_text 

df_movies = pd.read_csv(r"C:\Users\hidek\Downloads\Resume Coding Projects\Machine Learning\datasets\movies.csv")


# Data frame with the top 25 highest grossing movies
df_mo_highest = df_movies.nlargest(25, "gross")

# Gross of the top 25 movies (In billions)
df_gross = df_mo_highest["gross"] / 1e9

# Budget of the top 25 movies (In millions)
df_budget = df_mo_highest["budget"] / 1e6


# Creates a scatter plot of Gross vs Budget
plt.scatter(df_budget, df_gross, zorder=3)

plt.axis((50, df_budget.max() + 20,
          1.0, 3.0))

texts = []
for i, row in df_mo_highest.iterrows():
    texts.append(plt.text(row["budget"] / 1e6, row["gross"] / 1e9, row["name"], fontsize=7))

adjust_text(texts, arrowprops=dict(arrowstyle="-", color="gray", lw=0.5))

plt.grid(True, zorder=0)
plt.title("Gross vs Budget (top 25 highest grossing movies)")
plt.xlabel("Budget (In Millions)")
plt.ylabel("Gross (In BIllions)")
plt.show()

while not True:

    for i, row in df_movies.iterrows():
        if row["length (total)"] == df_movies["length (total)"].max():
            None