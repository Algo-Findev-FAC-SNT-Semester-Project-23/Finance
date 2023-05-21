
# Assignment 1

A brief description of what this project does and who it's for

The provided code is a Python implementation of a simple moving average (SMA) and exponential moving average (EMA) indicator for analyzing the historical stock data of a NIFTY 50 stock. Here's a brief explanation of what each step does:

## Step 1: Importing the necessary libraries
This step imports the required libraries, namely pandas for data manipulation and matplotlib for data visualization.

## Step 2: Loading the stock data
The code loads the historical stock data from a CSV file into a pandas DataFrame. The 'Date' column is converted to the appropriate date format for easier manipulation.

## Step 3: Calculating the Simple Moving Average (SMA)
The SMA is a commonly used technical indicator that smooths out price data over a specified period. In this code, a 20-day SMA is calculated by taking the average of the closing prices over a rolling window of 20 days. The resulting SMA values are stored in the 'SMA' column of the DataFrame.

## Step 4: Calculating the Exponential Moving Average (EMA)
The EMA is another popular technical indicator that gives more weight to recent price data. In this code, a 20-day EMA is calculated using the exponentially weighted moving average formula. The 'ewm' function from pandas is used to calculate the EMA, and the resulting EMA values are stored in the 'EMA' column of the DataFrame.

## Step 5: Visualizing the stock data and moving averages
The code uses the matplotlib library to create a plot that shows the stock's closing prices along with the SMA and EMA. The plot provides a visual representation of how the moving averages change over time, allowing for easier analysis of trends and potential trading signals.

By running this code with the appropriate stock data, you will obtain a plot that displays the stock prices, the SMA curve, and the EMA curve. This can help in understanding the stock's price movements and identifying potential buy or sell signals based on the interactions between the stock price and the moving averages.

