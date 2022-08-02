from my_package import calculate_prices
import my_package.calculate_prices
from my_package.calculate_prices import increase_price
from my_package.my_sub_package.format_to_coin import to_real as to_real

price = 56.33
print(calculate_prices.increase_price(price, 30, formatted=True))
print(increase_price(price, 100, formatted=True))
print(to_real(price))
