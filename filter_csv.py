# coding: iso-8859-1 -*-

import yfinance as yahooFinance
liste_actions_moins_risquees = []
liste_actions_risquees = []

msftInformation      = yahooFinance.Ticker("msft")
AppleInformation     = yahooFinance.Ticker("aapl")
GoogleInformation    = yahooFinance.Ticker("goog")
FacebookInformation  = yahooFinance.Ticker("FB")
LVMHFInformation     = yahooFinance.Ticker("LVMHF")
NFLXInformation = yahooFinance.Ticker('NFLX')
liste = [msftInformation, AppleInformation, GoogleInformation, FacebookInformation, LVMHFInformation, NFLXInformation]

maxi = max(msftInformation.info["beta"], AppleInformation.info["beta"], GoogleInformation.info["beta"], FacebookInformation.info["beta"], LVMHFInformation.info["beta"], NFLXInformation.info["beta"])

for elt in liste:
    print("L'action {} appartient au secteur {}. Son prix actuel est de {}$ et son beta est de {}.\n".format(elt.info['shortName'], elt.info['sector'], elt.info['regularMarketPrice'], elt.info['beta']))
    if elt.info['beta'] == maxi:
        nom=elt.info['shortName']
    if elt.info["beta"] > 1:
        liste_actions_risquees.append(elt.info['shortName'])
    elif elt.info["beta"] < 1:
        liste_actions_moins_risquees.append(elt.info['shortName'])

liste_actions_moins_risquees = ', '.join(liste_actions_moins_risquees)
liste_actions_risquees = ', '.join(liste_actions_risquees)

print("Parmi ces actions, celle dont le beta est le plus élevé est {}" .format(nom))
print("Les titres les plus risqués sont :", liste_actions_risquees)
print("Les titres les moins risqués sont :", liste_actions_moins_risquees)

