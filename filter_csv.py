# coding: iso-8859-1 -*-

import yfinance as yahooFinance

  
msftInformation      = yahooFinance.Ticker("msft")
AppleInformation     = yahooFinance.Ticker("aapl")
GoogleInformation    = yahooFinance.Ticker("goog")
FacebookInformation  = yahooFinance.Ticker("FB")
LVMHFInformation     = yahooFinance.Ticker("LVMHF")
NFLXInformation = yahooFinance.Ticker('NFLX')
liste = [msftInformation, AppleInformation, GoogleInformation, FacebookInformation, LVMHFInformation, NFLXInformation]

maxi = max(msftInformation.info["beta"], AppleInformation.info["beta"], GoogleInformation.info["beta"], FacebookInformation.info["beta"], LVMHFInformation.info["beta"], NFLXInformation.info["beta"])

for elt in liste:
    print("Le beta de l'action {} est de {}".format(elt.info['shortName'], elt.info['beta']))
    if elt.info['beta'] == maxi:
        nom=elt.info['shortName']

print("Parmi ces actions, celle dont le beta est le plus élevé est {}" .format(nom))

