
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
# df = sns.load_dataset("tips")
try:
    df = sns.load_dataset("tips")
except:
    df = pd.read_csv("ex2/tips.csv")

print("--- 1. Men's bills vs Women's bills ---")
print(df.groupby('sex', observed=True)['total_bill'].describe())

print("\n--- 2. Women's tips vs Men's tips ---")
print(df.groupby('sex', observed=True)['tip'].describe())

print("\n--- 3. Smokers vs Non-smokers tips (Variability and Median) ---")
print(df.groupby('smoker', observed=True)['tip'].agg(['std', 'var', 'median']))

print("\n--- 4. Visitors by day ---")
print(df['day'].value_counts())

print("\n--- 5. Correlation between total_bill and tip ---")
print(df[['total_bill', 'tip']].corr())

print("\n--- 6. Average tip by day ---")
# Order: Thur, Fri, Sat, Sun
days_order = ['Thur', 'Fri', 'Sat', 'Sun']
print(df.groupby('day', observed=True)['tip'].mean().reindex(days_order))

print("\n--- 7. Does larger bill always mean larger tip? ---")
# Check for counterexamples: Bill A > Bill B but Tip A < Tip B
# Just correlation is not enough for "always". Scatter plot visually shows this, but code can check.
# We can check if the rank of tip is identical to rank of total_bill
print("Correlation is high but not 1.0. scatterplot shows spread.")

print("\n--- 8. Tips < 5 dollars ---")
print(f"Percentage < 5: {(df['tip'] < 5).mean() * 100:.2f}%")

print("\n--- 9. Tip around 4 dollars ---")
print(df['tip'].mode())
print(df['tip'].value_counts().head(10))
print(df['tip'].describe())
# Check distribution (histogram-like) around 4
print(f"Tips between 3.5 and 4.5: {((df['tip'] >= 3.5) & (df['tip'] <= 4.5)).mean() * 100:.2f}%")
print(f"Tips between 1.5 and 2.5: {((df['tip'] >= 1.5) & (df['tip'] <= 2.5)).mean() * 100:.2f}%") # often round numbers like 2 or 3

print("\n--- General 1. Class Counts ---")
print(df['sex'].value_counts())
print(df['smoker'].value_counts())

print("\n--- General 2. Correlation ---")
print(df.corr(numeric_only=True))

print("\n--- General 3. Outliers by day ---")
print(df.groupby('day', observed=True)['tip'].describe())
# Outliers are typically > Q3 + 1.5*IQR
for day in days_order:
    day_data = df[df['day'] == day]['tip']
    Q1 = day_data.quantile(0.25)
    Q3 = day_data.quantile(0.75)
    IQR = Q3 - Q1
    outliers = day_data[(day_data < (Q1 - 1.5 * IQR)) | (day_data > (Q3 + 1.5 * IQR))]
    print(f"{day}: {len(outliers)} outliers, max: {day_data.max()}")

