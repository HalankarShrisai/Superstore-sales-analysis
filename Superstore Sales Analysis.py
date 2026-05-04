import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Superstore.csv', encoding='latin-1')

print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Category'] = df['Category'].astype('category')
df['Region'] = df['Region'].astype('category')
# Q1: Sales by region
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

# Q2: Profit by category
print(df.groupby('Category')['Profit'].sum().sort_values())

# Q3: Sub-categories with negative profit (discontinue these)
sub = df.groupby('Sub-Category')[['Sales','Profit']].sum()
print(sub[sub['Profit'] < 0])

# Q4: Profit margin by segment
df['Margin'] = df['Profit'] / df['Sales']
print(df.groupby('Segment')['Margin'].mean().round(3))

# Q5: Top 5 loss-making states
print(df.groupby('State')['Profit'].sum().nsmallest(5))
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Chart 1: Bar — Sales by Region
region_sales = df.groupby('Region')['Sales'].sum().sort_values()
axes[0].barh(region_sales.index, region_sales.values, color='steelblue')
axes[0].set_title('Sales by Region')
axes[0].set_xlabel('Total Sales ($)')

# Chart 2: Line — Monthly Sales Trend
monthly = df.resample('ME', on='Order Date')['Sales'].sum()
axes[1].plot(monthly.index, monthly.values, color='darkorange', linewidth=2)
axes[1].set_title('Monthly Sales Trend')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Sales ($)')
axes[1].tick_params(axis='x', rotation=45)

# Chart 3: Pie — Sales by Category
cat_sales = df.groupby('Category')['Sales'].sum()
axes[2].pie(cat_sales.values, labels=cat_sales.index,
            autopct='%1.1f%%', startangle=90,
            colors=['#4C72B0','#DD8452','#55A868'])
axes[2].set_title('Sales by Category')

plt.tight_layout()
plt.savefig('superstore_charts.png', dpi=150)
plt.show()
summary = df.groupby(['Region', 'Category']).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Avg_Margin=('Margin', 'mean')
).round(2).reset_index()

summary.to_excel('superstore_summary.xlsx', index=False)
print("Saved!")