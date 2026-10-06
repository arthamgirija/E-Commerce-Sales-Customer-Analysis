import pandas as pd
df=pd.read_csv("ecommerce_sales.csv")
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
df["order_date"]=pd.to_datetime(df["order_date"])
print(df.dtypes)
df=df.drop_duplicates()
print(df.duplicated().sum())
print(df[["discount","rating"]].mean())
df["discount"]=df["discount"].fillna(df["discount"].mean())
df["rating"] = df["rating"].fillna(df["rating"].mean())
print(df.isnull().sum())
#q10
df["revenue"]=df["unit_price"]*df["quantity"]
print(df[["quantity", "unit_price", "revenue"]].head())

df["discounted_revenue"]=df["revenue"]*(1-df["discount"]/100)
print(df[["revenue","discount","discounted_revenue"]].head())
#q11
df.groupby("category").agg(
    total_revenue=("revenue", "sum"),
    average_rating=("rating", "mean")
)
df["month"]=df["order_date"].dt.month
print(df[["order_date", "month"]].head())
monthly_revenue=df.groupby("month")["revenue"].sum()
print(monthly_revenue)
import numpy as np
print("Mean:", np.mean(df["revenue"]))
print("Median:", np.median(df["revenue"]))
print("Minimum:", np.min(df["revenue"]))
print("Maximum:", np.max(df["revenue"]))
print("Standard Deviation:", np.std(df["revenue"]))
top_products=df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(10)
print(top_products)
import matplotlib.pyplot as plt
top_products.plot(x="product",y="revenue",kind="bar")
plt.title("Top 10 products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("visualizations/top_products.png")
plt.show()
monthly_revenue.plot(kind="line",grid=True,marker="o")
plt.title("monthly revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("visualizations/monthly_revenue.png")
plt.show()

