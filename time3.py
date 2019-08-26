import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests
import math
url='https://kurs.web.id/api/v1/bni'

getdata=requests.get(url)
data=getdata.json()

dfAAPL=pd.read_csv('AAPL.csv', index_col=False, parse_dates=['Date'])
dfAAPL.set_index('Date', inplace=True)
dfAAPL.sort_index(inplace=True)

y1=[]
for i in range(len(dfAAPL['Close'])):
    hasil=float(dfAAPL['Close'][i]*int(data['beli']))
    y1.append(hasil)

dfFB=pd.read_csv('FB.csv', index_col=False, parse_dates=['Date'])
dfFB.set_index('Date', inplace=True)
dfFB.sort_index(inplace=True)

y2=[]
for i in range(len(dfFB['Close'])):
    hasil=float(dfFB['Close'][i]*int(data['beli']))
    y2.append(hasil)

dfGOOG=pd.read_csv('GOOG.csv', index_col=False, parse_dates=['Date'])
dfGOOG.set_index('Date', inplace=True)
dfGOOG.sort_index(inplace=True)

y3=[]
for i in range(len(dfGOOG['Close'])):
    hasil=float(dfGOOG['Close'][i]*int(data['beli']))
    y3.append(hasil)

dfMSFT=pd.read_csv('MSFT.csv', index_col=False, parse_dates=['Date'])
dfMSFT.set_index('Date', inplace=True)
dfMSFT.sort_index(inplace=True)
y4=[]
for i in range(len(dfMSFT['Close'])):
    hasil=float(dfMSFT['Close'][i]*int(data['beli']))
    y4.append(hasil)

dfTlkm=pd.read_csv('sahamTLKM.csv', index_col=False, parse_dates=['Tanggal'])
dfTlkm.set_index('Tanggal', inplace=True)
dfTlkm.sort_index(inplace=True)

dfIsat=pd.read_csv('sahamISAT.csv', index_col=False, parse_dates=['Tanggal'])
dfIsat.set_index('Tanggal', inplace=True)
dfIsat.sort_index(inplace=True)

dfExcl=pd.read_csv('sahamEXCL.csv', index_col=False, parse_dates=['Tanggal'])
dfExcl.set_index('Tanggal', inplace=True)
dfExcl.sort_index(inplace=True)

dfFREN=pd.read_csv('sahamFREN.csv', index_col=False, parse_dates=['Tanggal'])
dfFREN.set_index('Tanggal', inplace=True)
dfFREN.sort_index(inplace=True)

plt.style.use('seaborn')
plt.plot(
    dfAAPL.index, y1, 'r-',
    dfFB.index, y2, 'y-',
    dfGOOG.index, y3, 'b-',
    dfMSFT.index, y4, 'c-',
    dfTlkm.index, dfTlkm['Close'], 'green',
    dfIsat.index, dfIsat['Close'], 'grey',
    dfExcl.index, dfExcl['Close'], 'pink',
    dfFREN.index, dfFREN['Close'], 'purple'
)
plt.grid(True)
plt.title('Close Saham Aug 2018-2019')
plt.xlabel('Time')
plt.ylabel('Rupiah')
plt.xticks(rotation=60)
plt.legend(['Aple','Facebook','Google','Microsoft', 'Telkom', 'Indosat', 'Xl', 'Smartfren'])
plt.yscale('log')
ax=plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))            #bisa %b, %B, %b  %Y
plt.show()