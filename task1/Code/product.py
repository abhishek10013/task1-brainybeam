import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('product_stock.csv')

# Extract the 'Product' and 'Stock' columns
products = data['Product']
stocks = data['Stock']

# Create the pie chart
plt.figure(figsize=(8,8))  # Size of the figure
plt.pie(stocks, labels=products, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that the pie is drawn as a circle.
plt.axis('equal')

# Add a title
plt.title('Product Stock Distribution')

# Display the chart
plt.show()
