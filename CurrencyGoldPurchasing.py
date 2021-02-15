import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import mplcyberpunk

style.use('cyberpunk')

start = dt.datetime(2014,1,1)
end = dt.datetime(2019,12,31)
ounce2gram = 28.3495231
unitCurrency = 100
# Cuanto oro compra cada unidad de divisa?

dfGoldUSD = web.DataReader('GC=F','yahoo',start, end)
dfEURUSD = web.DataReader('EURUSD=X','yahoo',start, end)
dfGBPUSD = web.DataReader('GBPUSD=X','yahoo',start, end)
dfBTCUSD = web.DataReader('BTC-USD','yahoo',start, end)

def goldPurchasingPow(df):
    return ounce2gram*unitCurrency*df['Close']/dfGoldUSD['Close']
btcUnit = 0.02  
USDGLD = ounce2gram*unitCurrency/dfGoldUSD['Close'] 
EURGLD = goldPurchasingPow(dfEURUSD)
GBPGLD = goldPurchasingPow(dfGBPUSD)
BTCGLD = ounce2gram*btcUnit*dfBTCUSD['Close']/dfGoldUSD['Close']

USDGLD.interpolate(method='linear').plot(color='#b9ff53',linewidth = 0.5 ,label="100 USD")
EURGLD.interpolate(method='linear').plot(color='#20a6ff',linewidth = 0.5 ,label="100 EUR")
GBPGLD.interpolate(method='linear').plot(color='#9b0fec',linewidth = 0.5 ,label="100 GBP")
BTCGLD.interpolate(method='linear').plot(color='#fde401',linewidth = 0.5 ,label=str(btcUnit)+" BTC")

plt.title("Cuantos gramos de oro se compran con cada divisa?")
plt.grid(True)
plt.legend(loc = 'best')
plt.show()