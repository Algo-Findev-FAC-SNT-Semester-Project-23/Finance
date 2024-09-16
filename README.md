First I imported pandas,numpy,matplotlib,and yfinance libraries.
Then I downloaded the data (Stock Prices) of 3 months of Reliance.
Further, I calculated Simple moving average (mean of the closing values during a specific timeperiod), I used mean() of numpy to calculate mean and using rolling method of pandas I fixed time period to 3 months.
Next, I calculated Expotential moving average by using ewm() function of pandas. Span determines the time period of 3 months.
Lastly, I plotted the graph of SMA,EMA,CLOSE (price v/s date) using functions of maatplotlib library.
