#AlgoFindev
The project was carried out under Finance and Analytics Club, IIT Kanpur. The aim was to build effieicnt buy and sell strategies and analyse them on key financial metrics. 

# Structure 
Follwoing was the path followed :
1) Studying Technical Knowledge from Zerodha Varisty.
2) Application of simple algorithms on stock data from Yahoo Finance library.
3) Understanding of models like CAPM, French Farma 3 factor model to understand the working of financial marktets.
4) Utilising concept of Pair Trading Strategies for predicting stock trends. 
5) Utilsing multiple indicators like Bollinger Bands, Donchian Channels and RSI to develop trading strategies and backtest them.

# Implementation
1) **Simple** and **Exponential Moving Average **: As the name suggest these metrics calcualted the direct mean of the closing prices for a stock or give a specified weightage for each day wiht highest gives to the last day.
The logic is that if the EMA of a stock is moving above from the SMA or the EMA of small period is moving above the EMA for a large period, we expect an increase in the stock price. Thus a buy signal could be initiated. Simiarly an opposite logic holds for generating sell signals

![what-is-a-exponential-moving-average](https://github.com/user-attachments/assets/13dc9ce2-b4d3-4a78-ad00-c81a08cec75a)

**A** : Closing price in our case,  **n** : Number of days , **Wx** : weight for day X
![image](https://github.com/user-attachments/assets/2aa2d605-7692-4ded-af5b-159766f8aa71)

The convergence and divergence of exponential  moving average of 26 day and 18 day periods to generate buy and sell signals. The strategy was tested on Nifty 50 stocks like Apple, L&T tp understand the generalisabiltiy. Decisions were taken based on the closing prices for the day.
3) **Relatve Strenght Index** : This metric relies upon the **Support** and **Resistance** threhsolds for stocks. As the name suggests, Restiance is like the upper barrier for the stock and Support is the lower barrier for stock price based on hsitorical data. RSI is calcualted using the following formula.

![RSI](https://github.com/user-attachments/assets/687052ae-0500-4e13-93e9-d4f7c3bf862d)

Usually a large enough tiem period is decided to find the Avg Gain and Avg loss. Then the thresholds for RSI are decided on the basis of **Overbought** or **Oversold**  state of the stock. Specical consdieration has to be made when a breakout or long term loss happens and the strategy has to be modfieid to account for the same.

3)** Donchain Channels** : Donchian Channel draws a line between an asset's peak and low price over a given period of time, generally using candlesticks as a clock. Candlesticks are plot regions on charts that show the open, high, low, close, and time frame of a certain stock. 
1) The upper band represents the previous period's highest high
2) The lower band represents the previous period's lowest Low
3) The centre band reflects the current high and low for that trading period as an average
![image](https://github.com/user-attachments/assets/46e9fc62-b8e4-47f1-a468-237e7322b3be)

Ways to use Donchian Channels : 
1) Breakout Indicator : Donchian channels are used to identify a stock's breakout, which allows traders to take long or short bets. Traders can take a long position and record profits if the stock is trading above the Donchian channels or short the stock if it is trading below the channels.
2) Trading with Middle : The average of the lower and upper bands is used to calculate the centre band. This band is frequently utilized as a breakout sign in Donchian channels. When the stock climbs above the middle band of the Donchian channel, open a long position; when the price drops below the middle band, open a short position.

**Results**
The final algoirithm built using Donchican Channels and RSi was backtested on 2 years of large cap and small cap stock data giving a ** Sharpe Ration** of 0.69.

