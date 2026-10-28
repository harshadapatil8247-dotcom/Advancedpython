import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

print(df.head())
print(df.info())

print("Average Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

print(df[df["Marks"] > 75])

plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.show()

plt.hist(df["Marks"], bins=5)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Student Marks")
plt.show()

plt.scatter(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")

plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
