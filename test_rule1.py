from yahoo_fin import stock_info
#import matplotlib.pyplot
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot

#ticker = input('Input the ticker of the stock: ')
ticker = 'IQ'
share = stock_info.get_data(ticker, start_date = '01/01/2018' , end_date = '07/07/2019')
shr_close_vals = share['adjclose']

local_max = 0.0000000001
local_min = 1000000
state = 'buy'
investment_init = 1*shr_close_vals[0]
investment = investment_init
profit = 0

for idx, val in enumerate(shr_close_vals):
    if idx > 0:
        current = val
        previous = shr_close_vals[idx - 1]

        if state=='buy':
            if current > local_max:
                local_max = current
            else:
                diff_lmax = local_max - current #now this is >= 0
                diff_lmax_percent = (diff_lmax/local_max)*100
                if diff_lmax_percent > 5:
                    state='sell'
                    print(state)
                    print(shr_close_vals.index[idx])
                    print(shr_close_vals[idx-3:idx+3])
                    local_max = 0.0000000001
                    shares_price = 1*current
                    profit = profit+(shares_price-investment)
                    print(profit)
                    continue

        if state=='sell':
            if current < local_min:
                local_min = current
            else:
                diff_lmin = current - local_min #now this is >= 0
                diff_lmin_percent = (diff_lmin/local_min)*100
                if diff_lmin_percent > 3:
                    state='buy'
                    print(state)
                    print(shr_close_vals.index[idx])
                    print(shr_close_vals[idx-3:idx+3])
                    local_min = 1000000
                    investment = 1*current
                    if (investment > investment_init+profit):
                        print('investment : ',investment)
                        print('investment_init : ',investment_init)
                        print('profit : ',profit)
                        profit =  (investment_init+profit) - investment
                    print(profit)
                    continue

if state=='buy': #end profit calculation
    shares_price = 1*current
    profit = profit+(shares_price-investment)
print('Investment Value : ',investment_init)
print('Return Value : ',investment_init + profit)
print('% change : ',profit/investment_init*100)
graph = shr_close_vals.plot(label=ticker)
graph.set_ylabel('Return (in %)')
graph.set_xlabel('Date')
matplotlib.pyplot.show()
