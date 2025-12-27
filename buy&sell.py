prices=[7,2,1,5,6,4,8]
max_profit=0
min_price=float("inf")
n=len(prices)
def buyandsell(prices,max_profit,min_price):
    for i in range(0,n):
        min_price=min(min_price,prices[i])
        max_profit=max(max_profit,prices[i]-min_price)
    return max_profit     

print(buyandsell(prices,max_profit,min_price)) 