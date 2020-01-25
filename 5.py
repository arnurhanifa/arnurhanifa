def findHighestProfit(price):
    n = len(price)
    profit = 0
    for i in range (n-2):
        if price[i] < price[i+1]:
            profit = profit + (price[i+1]-price[i])
    if profit !=0:
        print(profit)
    else:
        print("Tidak bisa mendapatkan profit pada hari-hari ini")

#[10, 2, 11, 20, 3, 5]
#[10, 6, 4, 3, 2, 1]
findHighestProfit([10, 2, 11, 20, 3, 5])
