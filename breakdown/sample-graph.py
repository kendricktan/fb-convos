import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

blue, = sns.color_palette('muted', 1)

x = np.arange(5)
y = np.random.randint(8, 20, 5)

x_labels = ['one', 'two', 'three', 'four', 'five']

# Create 
fig, ax = plt.subplots()
ax.plot(x, y, color=blue, lw=3)
ax.fill_between(x, 0, y, alpha=.3)
ax.set(xlim=(0, len(x)-1), ylim=(0, None), xticks=x)

# Set label position
ax.set_xticks([1,1.5,2,3,4])

# Set labels text
ax.set_xticklabels(x_labels)

plt.show()
