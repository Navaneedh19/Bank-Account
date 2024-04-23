# Line Plot
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10000, 12000, 11000, 13000, 14000]
plt.plot(months, sales, marker='o', linestyle='-', color = 'green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.show()


# # Scatter Plot
# import matplotlib.pyplot as plt
# sales = [10000, 12000, 11000, 13000, 14000]
# ad_expenses = [5000, 6000, 5500, 7000, 7500]
# plt.scatter(ad_expenses, sales, color='blue', alpha=0.5)
# plt.title('Sales vs Advertising Expenses')
# plt.xlabel('Advertising Expenses ($)')
# plt.ylabel('Sales ($)')
# plt.grid(True)
# plt.show()


# # Histogram
# import matplotlib.pyplot as plt
# sales = [10000, 12000, 11000, 13000, 14000, 12500, 12200, 11500, 12800, 13500]
# plt.hist(sales,  color='green', edgecolor='red')
# plt.title('Sales Distribution')
# plt.xlabel('Sales ($)')
# plt.ylabel('Frequency')
# # plt.grid(True)
# plt.show()
