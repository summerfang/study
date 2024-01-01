SPY ETF Historical Dataset
=======================================

NOTE: Only intraday-bars with trading volume are included. Bars with zero volume are excluded.

Timeframes : 1-minute, 5-minutes, 30-minutes, 1-hour, 1-day
(two weeks of split-adjusted sample data for all timeframes is included)



Dates : First Date - 2005-01-03   |  Last Date 2023-05-18


Adjustments
------------

We provide three types of data:
Unadjusted - actual historic traded prices with no adjustments (only the 1-minute and 1-day timeframes are available for unadjusted data)
Split Adjusted - prices adjusted for stock splits and reverse splits only
Split+Dividend Adjusted - prices adjusted for both splits and dividends

More details on the adjustment process is at https://firstratedata.com/about/price_adjustment


Format
-------
Data is in the format : { DateTime (yyyy-MM-dd HH:mm:ss), Open, High, Low, Close, Volume}  

- Volume Numbers are in individual shares
- Timestamps run from the start of the period (eg 1min bars stamped 09:30 run from 09:30.00 to 09:30.59)
- Times with zero volume are omitted (thus gaps in the data sequence are when there have been no trades)


Updates
-------
This dataset is updated daily (update files are available by 3am on the following trading day)*  

 

Notes
-----
 
- Timezone is US Eastern Time    
- Excel will usually fail to open large files directly. 
  To use the data in Excel, open the files using notepad and then break into smaller files or copy/paste into Excel 
- Data license is available at https://firstratedata.com/about/license
 
  
 
* update times are approximate and users may experience small delays in the event of a server or network outage.
 





___________________________
copyright FirstRateData.com