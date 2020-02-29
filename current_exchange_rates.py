import requests
import pandas as pd
import matplotlib.pyplot as plt

usd = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/usd/last/10/?format=json').json()
eur = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/eur/last/10/?format=json').json()
chf = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/chf/last/10/?format=json').json()

ax = plt.gca()

df_date = pd.DataFrame(data=usd['rates'], columns=['effectiveDate']).rename(columns={"effectiveDate": "Date"})
df_usd = pd.DataFrame(data=usd['rates'], columns=['mid']).rename(columns={"mid": "USD"})
df_eur = pd.DataFrame(data=eur['rates'], columns=['mid']).rename(columns={"mid": "EUR"})
df_chf = pd.DataFrame(data=chf['rates'], columns=['mid']).rename(columns={"mid": "CHF"})

df_result = pd.concat(
    [df_date, df_eur.reindex(df_date.index), df_usd.reindex(df_date.index), df_chf.reindex(df_date.index)], axis=1)

df_result.plot(kind='line', x='Date', y='USD', ax=ax)
df_result.plot(kind='line', x='Date', y='EUR', color="green", ax=ax)
df_result.plot(kind='line', x='Date', y='CHF', color='red', ax=ax)

plt.title("Piotr Szuta 2020")
plt.show()
