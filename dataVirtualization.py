#                                  Data virtualization
# Task1: Load dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# load the dataset
df = pd.read_csv("vgsales.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.columns)

# Task2: times series/trend analysis
# missing Year in dataset: clean that first
df = df.dropna(subset=["Year"])
df["Year"] = df["Year"].astype(int)
df = df[(df["Year"] >= 2006) & (df["Year"] <= 2016)]
# group by year: sum the global sales for each year
yearSales = df.groupby("Year")["Global_Sales"].sum()
print("Sales Year: ",yearSales)
# line plot: year vs globalSales trend
plt.figure(figsize=(10,6))
plt.plot(yearSales.index, yearSales.values, color="steelblue", marker="o", linewidth=2)
plt.title("Global Video Game Sales Trend (2006-2016)", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Global Sales",fontsize=12 )
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# Task3: Data distribution analysis
# Box plot: Genre vs global Sales
plt.figure(figsize=(12,6))
sns.boxplot(data=df, x="Genre", y="Global_Sales", hue="Genre", palette="Set2", legend=False)
plt.title("Global Sales Distribution of Video Game by Genre", fontsize=14, fontweight="bold")
plt.xlabel("Genre", fontsize=12)
plt.ylabel("Global Sales", fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0,5)
plt.tight_layout()
plt.show()

# Task4: non-geographic visualization
# Bar chart:total global sales by genre
genreSales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(12,6))
plt.bar(genreSales.index, genreSales.values, color="mediumseagreen")
plt.title("Total Global Sales by Genre", fontsize=14, fontweight="bold")
plt.xlabel("Genre", fontsize=12)
plt.ylabel("Total Global Sales", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
