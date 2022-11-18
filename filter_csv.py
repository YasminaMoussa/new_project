import yfinance as yahooFinance

msftInformation      = yahooFinance.Ticker("msft")
AppleInformation     = yahooFinance.Ticker("aapl")
GoogleInformation    = yahooFinance.Ticker("goog")
FacebookInformation  = yahooFinance.Ticker("FB")
LVMHFInformation     = yahooFinance.Ticker("LVMHF")

liste = [msftInformation, AppleInformation, GoogleInformation, FacebookInformation, LVMHFInformation]

for elt in liste:
    print(elt, elt.info['sector'], elt.info['beta'])