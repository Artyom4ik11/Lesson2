
goods_prices = [57.8, 46.51, 97.1, 22.21, 432.57, 32.33, 74.43, 274.67, 21.55, 643.73, 345.21,
                65.73, 16.74, 104.84, 64.74]
new_goods_prices = []
for price in goods_prices:
    r = int(price)
    k = round((price - r) * 100)
    new_goods_prices.append(f'{r} руб {k:02d} коп')
print(', '.join(new_goods_prices))
print(id(goods_prices))
goods_prices.sort()
print(id(goods_prices))
print(goods_prices)
alt_goods_prices = sorted(goods_prices, reverse=True)
print(alt_goods_prices)
print(sorted(goods_prices[-5:]))