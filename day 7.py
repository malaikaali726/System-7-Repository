# Day 7: CSV analysis with Pandas, Matplotlib, Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("students.csv")
print("First 5 rows:\n", df.head())
print("\nShape:", df.shape)

# Summary statistics
print("\nSummary statistics:\n", df.describe())
print("\nAverage marks per subject:\n", df[["math", "english", "science"]].mean())

# Add overall average column
df["average"] = df[["math", "english", "science"]].mean(axis=1).round(2)
print("\nTop 3 students:\n", df.sort_values("average", ascending=False).head(3))

# Chart 1: Bar chart of average marks by city (Matplotlib)
city_avg = df.groupby("city")["average"].mean()
plt.figure(figsize=(7, 4))
city_avg.plot(kind="bar", color="steelblue")
plt.title("Average Marks by City")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_city_average.png")
plt.show()

# Chart 2: Histogram of math marks (Matplotlib)
plt.figure(figsize=(7, 4))
plt.hist(df["math"], bins=5, color="orange", edgecolor="black")
plt.title("Distribution of Math Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("chart_math_hist.png")
plt.show()

# Chart 3: Heatmap of correlations (Seaborn)
plt.figure(figsize=(7, 5))
sns.heatmap(df[["math", "english", "science", "attendance"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Between Scores and Attendance")
plt.tight_layout()
plt.savefig("chart_correlation.png")
plt.show()

# Chart 4: Scatter plot attendance vs average (Seaborn)
plt.figure(figsize=(7, 4))
sns.scatterplot(data=df, x="attendance", y="average", hue="course", s=100)
plt.title("Attendance vs Average Marks")
plt.tight_layout()
plt.savefig("chart_attendance_scatter.png")
plt.show()

print("\nCharts saved successfully.")