import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel(r'C:\Users\alpef\Desktop\EUR TRY plot\EUR_TRY Historical Data.xlsx')
x = pd.DataFrame(data, columns= ['Date'])
y = pd.DataFrame(data, columns= ['Price'])
plt.plot(x, y)
plt.title('Euro vs Turkish Lira over the years')
plt.xlabel('EUR vs TRY')
plt.ylabel('Years')