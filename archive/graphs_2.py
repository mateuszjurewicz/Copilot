"""
Create a bar chart to compare GPT-3 (175 billion) and Codex (12 billion).
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Generate data and plot it.
    :return:
    """
    # Create data
    x = np.arange(2)
    y = [175, 12]
    # Create plot
    plt.bar(x, y)
    plt.xticks(x, ('GPT-3', 'Codex'))
    plt.ylabel('Number of tokens')
    plt.title('Number of tokens in GPT-3 and Codex')
    plt.show()


def generate_pie_chart_data():
    """
    Generate data for a pie chart.
    :return:
    """
    # Create data
    labels = 'GPT-3', 'Codex'
    sizes = [175, 12]
    # Create plot
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    generate_pie_chart_data()