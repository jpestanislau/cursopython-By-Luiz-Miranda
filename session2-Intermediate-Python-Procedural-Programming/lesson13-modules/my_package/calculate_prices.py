from my_package.my_sub_package import format_to_coin
# from my_package.my_sub_package import format_to_coin


def increase_price(value, percent, formatted=False):
    if formatted:
        return format_to_coin.to_real(value + (value * (percent / 100)))
    return value + (value * (percent/100))


def decrease_price(value, percent, formatted=False):
    if formatted:
        return format_to_coin.to_real(value - (value * (percent / 100)))
    return value - (value * (percent/100))
