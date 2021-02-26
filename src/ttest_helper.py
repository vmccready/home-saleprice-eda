import numpy as np
from scipy import stats
from itertools import combinations

c = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
     '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
     '#bcbd22', '#17becf']
colors = c + c

use_codes = np.load('./data/use_codes.npy', allow_pickle='TRUE').item()

def plotter(fig, ax, data, column, index):
    axes = ax.flatten()
    for i, col in enumerate(index):
        data[data[column] == col].hist(
            'price/sqft',
            bins=50,
            density=True,
            color=colors[i],
            ax=axes[i])

        axes[i].set_title("{}".format(col))

def perform_ttest(index, data, column, alpha):
    ttests = []
    for i1, i2 in combinations(index, 2):
        s, p = stats.ttest_ind(
            data[data[column] == i1]['price/sqft'],
            data[data[column] == i2]['price/sqft'])
        ttests.append((i1, i2, s, p))
    print(f'Statistical significance in price/sqft between {column}')
    confidence = (1-alpha)*100
    for i1, i2, s, p in ttests:
        if p<alpha:
            print('{} and {} are different with {}% confidence: P value of {:.4f}'.format(i1,i2,confidence,p))
        else:
            print('{} and {}: P value of {:.4f}'.format(i1,i2,p))