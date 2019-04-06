from yahoo_fin.stock_info import get_data
#import matplotlib.pyplot
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot



sp500 = get_data('^gspc' , start_date = '01/02/2010' , end_date = '04/06/2019')
ticker = input('Input the ticker of the stock: ')
share = get_data(ticker, start_date = '01/02/2010' , end_date = '04/06/2019')

sp500['new_div_first'] = sp500['adjclose'] / sp500['adjclose'].iloc[0]
sp500['pct_change'] = (sp500['new_div_first']-1)*100

share['new_div_first'] = share['adjclose'] / share['adjclose'].iloc[0]
share['pct_change'] = (share['new_div_first']-1)*100

market_return = sp500['pct_change']
stock_return = share['pct_change']



graph = stock_return.plot(label=ticker, legend=True, x="Time", y = "Percent")
graph.set_ylabel('Return (in %)')
graph.set_xlabel('Date')
graph = market_return.plot(label="S&P 500", legend=True, title = ticker + " vs. the S&P 500")

matplotlib.pyplot.show()
