import matplotlib.pyplot as plt

price_110 = [5.4, 6.8, 8.5]
price_120 = [5.5, 8, 8.4]
price_130 = [5.6, 8.36, 8.8]
price_140 = [5.4, 8.4, 8.77]
price_150 = [5.8, 8.37, 8.76]
year = [2003, 2004, 2005]

plt.plot(year,price_110,label = "ІНФО")
plt.plot(year,price_120,label = "АЖІО")
plt.plot(year,price_130,label = "Градобанк")
plt.plot(year,price_140,label = "Відродження")
plt.plot(year,price_150,label = "Укрінбанк")
plt.xticks([2003, 2004, 2005])
plt.xlabel("Рік")
plt.ylabel("Курс")
plt.legend()
plt.grid(True)

def showplot():
    plt.show()