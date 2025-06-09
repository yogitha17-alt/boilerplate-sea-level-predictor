import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    y = df["CSIRO Adjusted Sea Level"]
    x = df["Year"]

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    res = linregress(x, y)
    x_fit1 = pd.Series([i for i in range(1880, 2051)])
    y_fit1 = res.slope * x_fit1 + res.intercept
    plt.plot(x_fit1, y_fit1, 'red')
    # Create second line of best fit

    new_df = df[df['Year'] >= 2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    res2 = linregress(new_x, new_y)
    x_fit2 = pd.Series([i for i in range(2000, 2051)])
    y_fit2 = res2.slope * x_fit2 + res2.intercept
    plt.plot(x_fit2, y_fit2, 'green')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()