
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

print(get_phone(country=1, area=123, first=234, last=3456))