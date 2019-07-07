from yahoo_fin import stock_info
#import matplotlib.pyplot
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot

#ticker = input('Input the ticker of the stock: ')
ticker = 'NFLX'
share = stock_info.get_data(ticker, start_date = '06/19/2018' , end_date = '06/20/2019')
shr_close_vals = share['adjclose']

local_max = 0
for idx, val in enumerate(shr_close_vals):
    if idx > 0:
        previous = shr_close_vals[idx - 1]
        diff = val - previous

        if diff < 0:
            change = -diff/previous * 100
            print(diff/val)
