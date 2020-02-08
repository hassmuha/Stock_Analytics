from yahoo_fin import stock_info
#import matplotlib.pyplot
import matplotlib
import math
matplotlib.use('TkAgg')
import matplotlib.pyplot

#ticker = input('Input the ticker of the stock: ')
tickers = ['EWG']
shr_close_vals = []
local_max = []
local_min = []

for idx,ticker in enumerate(tickers):
    share = stock_info.get_data(ticker, start_date = '11/12/2014' , end_date = '11/12/2019')
    shr_close_vals.append(share['adjclose'])
    local_max.append(0.0000000001)
    local_min.append(1000000)

state = 'buy'
shr_idx = 0
invest_amount = 5000

invest_shr_init = math.floor(invest_amount/shr_close_vals[shr_idx][0])
invest_shr_price_init = shr_close_vals[shr_idx][0]

invest_shr = invest_shr_init
invest_shr_price = shr_close_vals[shr_idx][0]

last_sell_shr = invest_shr_init
last_sell_shr_price = shr_close_vals[shr_idx][0]

profit = 0

for idx, val in enumerate(shr_close_vals[0]):
    if idx > 0:
        for ticker_idx,ticker in enumerate(tickers):
            current = shr_close_vals[ticker_idx][idx]
            previous = shr_close_vals[ticker_idx][idx - 1]
            if current > local_max[ticker_idx] or current > local_min[ticker_idx]:
                local_max[ticker_idx] = current
            elif current < local_min[ticker_idx] or current < local_max[ticker_idx]:
                local_min[ticker_idx] = current


        if state=='buy':
            current = shr_close_vals[shr_idx][idx]
            previous = shr_close_vals[shr_idx][idx - 1]
            diff_lmax = local_max[shr_idx] - current #now this is >= 0
            diff_lmax_percent = (diff_lmax/local_max[shr_idx])*100
            if diff_lmax_percent > 10:
                state='sell'
                last_sell_shr = invest_shr
                last_sell_shr_price = current
                print(state)
                print(shr_close_vals[shr_idx].index[idx])
                print(shr_close_vals[shr_idx][idx-3:idx+3])
                print('profit : ',profit)
                print('last_sell_shr : ',last_sell_shr)
                print('last_sell_shr_price: ',last_sell_shr_price)
                print('invest_shr : ',invest_shr)
                print('invest_shr_price: ',invest_shr_price)
                profit = profit+(last_sell_shr*last_sell_shr_price-invest_shr*invest_shr_price)
                print(profit)
                #for ticker_idx,ticker in enumerate(tickers):
                #    local_min[ticker_idx]  = 1000000
                #    local_max[ticker_idx]  = 0.0000000001
                continue

            if ((current-invest_shr_price)/invest_shr_price)*100 > 10:
                state='sell'
                last_sell_shr = invest_shr
                last_sell_shr_price = current
                print(state)
                print(shr_close_vals[shr_idx].index[idx])
                print(shr_close_vals[shr_idx][idx-3:idx+3])
                print('profit : ',profit)
                print('last_sell_shr : ',last_sell_shr)
                print('last_sell_shr_price: ',last_sell_shr_price)
                print('invest_shr : ',invest_shr)
                print('invest_shr_price: ',invest_shr_price)
                profit = profit+(last_sell_shr*last_sell_shr_price-invest_shr*invest_shr_price)
                print(profit)

                local_min[shr_idx]  = 1000000
                local_max[shr_idx]  = 0.0000000001
                continue


        if state=='sell':
            '''if current < local_min[shr_idx]:
                local_min = current
            else:'''
            last_diff_lmin_percent = 0
            for ticker_idx,ticker in enumerate(tickers):
                current = shr_close_vals[ticker_idx][idx]
                previous = shr_close_vals[ticker_idx][idx - 1]

                diff_lmin = current - local_min[ticker_idx] #now this is >= 0
                diff_lmin_percent = (diff_lmin/local_min[ticker_idx])*100
                if diff_lmin_percent > 5 and diff_lmin_percent > last_diff_lmin_percent:
                    state='buy'
                    shr_idx = ticker_idx
                    last_diff_lmin_percent = diff_lmin_percent
            if state=='buy':
                print(state)
                print(shr_close_vals[shr_idx].index[idx])
                print(shr_close_vals[shr_idx][idx-3:idx+3])
                #for ticker_idx,ticker in enumerate(tickers):
                #    local_min[ticker_idx]  = 1000000
                #    local_max[ticker_idx]  = 0.0000000001

                invest_shr = math.floor(invest_amount/shr_close_vals[shr_idx][idx])
                invest_shr_price = shr_close_vals[shr_idx][idx]
                continue






if state=='buy': #end profit calculation
    last_sell_shr = invest_shr
    last_sell_shr_price = current
    profit = profit+(last_sell_shr*last_sell_shr_price-invest_shr*invest_shr_price)
print('Investment Value : ',invest_amount)
print('Return Value : ',invest_amount + profit)
print('% change : ',profit/invest_amount*100)

for idx,ticker in enumerate(tickers):
    shr_close_vals_temp = ((shr_close_vals[idx]-shr_close_vals[idx][0])/shr_close_vals[idx][0])*100
    graph = shr_close_vals_temp.plot(label=ticker, legend=True)
graph.set_ylabel('Return (in %)')
graph.set_xlabel('Date')
matplotlib.pyplot.show()
