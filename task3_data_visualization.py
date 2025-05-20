import matplotlib.pyplot as plt

categories = ['A', 'B', 'C']
values = [10, 24, 36]

plt.bar(categories, values, color='skyblue')
plt.title('Sample Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()
