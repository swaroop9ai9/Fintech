# Yahoo Finance Python API

# This API Supports to retrieve data especially works for NSE/BSE stocks.
# Also can Retrieve Intraday 1min gradualar Data.

## Usage

This command returns a dataframe which can be further modified to add new columns , exported to excel etc

``` python
hdfc = YahooFinance('HDFC.NS', result_range='1mo', interval='15m', dropna='True').result
```


## Installation

``` bash
git clone https://github.com/swaroop9ai9/Fintech/raptor_finance_api.git
cd raptor_finance_api
python setup.py install
```

### Requirements

- Pandas
- Request

### Note

Make sure to use TICKER symbol from yahoo finance website
https://in.finance.yahoo.com/ 
