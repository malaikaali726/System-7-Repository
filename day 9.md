Measures of Central Tendency and Spread
1. Mean

The mean is the average of all values in a dataset. You find it by adding all the values and dividing by how many values there are.

Formula: Mean = Sum of all values ÷ Total number of values

Example: For the dataset 10, 20, 30, 40, 50:

Sum = 10 + 20 + 30 + 40 + 50 = 150
Count = 5
Mean = 150 ÷ 5 = 30

Uses: Average marks of students, average salary of employees, average house prices, and understanding the central value of numerical data.

Important: The mean is sensitive to outliers. Very large or very small values can pull it significantly.

2. Median

The median is the middle value when all values are arranged in order, from smallest to largest or largest to smallest. It splits the dataset into two equal halves.

Odd number of values: For 10, 20, 30, 40, 50, there are five values, so the middle one is 30.

Even number of values: For 10, 20, 30, 40, 50, 60, the two middle values are 30 and 40. The median is their average: (30 + 40) ÷ 2 = 35.

Uses: Typical house prices in a city, salaries when a few are extremely high, and any numerical data containing outliers.

Important: The median is less affected by outliers than the mean.

3. Mode

The mode is the value that appears most often in a dataset. A dataset can have one mode, several modes, or none.

One mode: In 10, 20, 20, 30, 40, the mode is 20, since it appears twice.
Two modes (bimodal): In 10, 10, 20, 30, 30, 40, the modes are 10 and 30.
No mode: In 10, 20, 30, 40, every value appears once, so there is no mode.

Uses: Most purchased product, most popular clothing size, and the most common category in categorical data such as city names or colors.

Important: Unlike the mean and median, the mode works with categorical data.

4. Variance

Variance measures how far the values in a dataset spread out from the mean. Low variance means values cluster near the mean, while high variance means they are more spread out.

Formula (population):

σ² = Σ(xᵢ − μ)² ÷ N

where σ² is the variance, xᵢ is each value, μ is the mean, and N is the number of values.

Example: For the dataset 2, 4, 6, 8, 10:

Mean: (2 + 4 + 6 + 8 + 10) ÷ 5 = 6
Differences from the mean: −4, −2, 0, 2, 4
Squared differences: 16, 4, 0, 4, 16
Sum of squared differences: 40
Divide by N: 40 ÷ 5 = 8

Population variance = 8

Sample variance: When your data is a sample from a larger population, divide by N − 1 instead:

40 ÷ (5 − 1) = 10

Uses: Measuring spread in data, understanding variation in house prices, analyzing financial returns, and comparing variability between datasets.

Important: Variance is in squared units. If the values are in square feet, the variance is in square feet squared.

5. Standard Deviation

Standard deviation describes how much values typically vary around the mean. It is the square root of the variance.

Formula (population):

σ = √(Σ(xᢤ − μ)² ÷ N)

Example: For the same dataset, the population variance is 8, so:

Standard deviation = √8 ≈ 2.83

For a sample, the variance is 10, so the sample standard deviation is √10 ≈ 3.16

Uses: Understanding how spread out data is, measuring variation in house prices, analyzing student marks, detecting unusual observations, and supporting feature scaling in machine learning.

Important: Standard deviation is in the same units as the original data, which makes it easier to interpret than variance.
