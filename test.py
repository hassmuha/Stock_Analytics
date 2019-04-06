# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si

few_days = si.get_data('msft' , start_date = '01/01/1999' , end_date = '01/10/1999')
print(few_days)
