# Support_Resistance_Kmeans
Automatically detects support and resistance levels for all major and minor forex pairs on multiple timeframes (1 week, 2 weeks, 1 month, 3 months, and when price was 4% below current price) using kmeans unsupervised learning from sklearn and plots them using mplfinance


A continuation from https://github.com/Coelodonta/Machine_Learning_Support_Resistance


Change access token in line 14 of get_data.py to your oanda api access token. 

NOTE: Data pulling will only work when forex market is open
