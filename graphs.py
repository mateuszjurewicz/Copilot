"""
Create a bar chart to compare GPT-3 (175 Billion) and Codex (12 Billion)
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    Main function
    """
    # Get the data
    gpt_data, codex_data = generate_data()

    # Create the plot
    fig, ax = plt.subplots()
    ax.bar(gpt_data[:, 0], gpt_data[:, 1], color='#5DADE2', label='GPT-3')
    ax.bar(codex_data[:, 0], codex_data[:, 1], color='#F4D03F', label='Codex')
    ax.set_xlabel('Number of tokens')
    ax.set_ylabel('Number of sentences')
    ax.set_title('Number of sentences per number of tokens')
    ax.legend()
    plt.show()


def generate_data():
    """
    Generate some data
    """
    gpt_data = np.random.randint(0, 100, size=(1, 10))
    codex_data = np.random.randint(0, 100, size=(1, 10))
    return gpt_data, codex_data


def generate_pie_chart_data():
    """
    Generate some data
    """
    gpt_data = np.random.randint(0, 100, size=(1, 2))
    codex_data = np.random.randint(0, 100, size=(1, 2))
    return gpt_data, codex_data


def create_pie_chart():
    """
    Create a pie chart
    """
    # Get the data
    gpt_data, codex_data = generate_pie_chart_data()

    # Create the plot
    fig, ax = plt.subplots()
    ax.pie(gpt_data[0], labels=['GPT-3', 'Codex'], autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')
    plt.show()


if __name__ == "__main__":
    # main()
    create_pie_chart()
