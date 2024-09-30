import random
import sys

TIME_PERIOD = "2024"

currencies = {
    "USD", "DEM", "YEN", "EURO", "POUND", "YUAN", "RUBLE", "RIAL",
}

currency_multipliers = {
    "USD": 1,
    "DEM": 381.25,
    "YEN": 142.22,
    "EURO": 0.9,
    "POUND": 0.75,
    "YUAN": 7.01,
    "RUBLE": 94.36,
    "RIAL": 42105
}

def rand_country_value():
    return random.randint(1, 8)

def rand_class_value():
    return random.randint(1, 100)

def start_class(value):
    if value < 10:
        return "Lower Class"
    elif 10 <= value <= 60:
        return "Middle Class"
    elif 60 < value <= 90:
        return "Upper Class"
    else:
        return "Leader"

def start_country(value):
    countries = ["Germany", "Japan", "USA", "France", "United Kingdom", "China", "Russia", "Iran"]
    return countries[value - 1]

def currency_convert(convert_from, convert_to, amount):
    convert_from = convert_from.upper()
    convert_to = convert_to.upper()
    if convert_from not in currency_multipliers or convert_to not in currency_multipliers:
        print("Error: Invalid currency.")
        sys.exit()
    
    amount_in_usd = float(amount) / currency_multipliers[convert_from]
    converted_amount = round(amount_in_usd * currency_multipliers[convert_to], 2)
    
    if convert_to == "YEN":
        return int(round(converted_amount, 0))
    return converted_amount

def determine_default_currency(country):
    currencies_map = {
        "Germany": "DEM",
        "Japan": "YEN",
        "USA": "USD",
        "Iran": "RIAL",
        "France": "EURO",
        "United Kingdom": "POUND",
        "Russia": "RUBLE",
        "China": "YUAN"
    }
    return currencies_map.get(country)

def starting_money(class_name):
    money_map = {
        "Lower Class": 10000,
        "Middle Class": 50000,
        "Upper Class": 250000,
        "Leader": 1000000
    }
    return money_map.get(class_name, 0)

def convert_starting_money_to_default_currency(class_name, country_name):
    starting_usd = starting_money(class_name)
    default_currency = determine_default_currency(country_name)
    return currency_convert("USD", default_currency, starting_usd)

def main():
    country_value = rand_country_value()
    class_value = rand_class_value()
    
    country_name = start_country(country_value)
    class_name = start_class(class_value)

    print(f"The year is {TIME_PERIOD} in {country_name}. It is your job as a(n) {class_name} to lead your country to worldwide rule!")
    
    default_money = convert_starting_money_to_default_currency(class_name, country_name)
    print(f"As a(n) {class_name}, you start with {default_money} {determine_default_currency(country_name)}.")
    
    print("Currency options are as follows:")
    for name in currencies:
        print(name)

    convert_from = input("Choose the currency type to convert from: ")
    convert_from = convert_from.upper()
    if convert_from not in currencies:
        print("Error: Not a currency type")
        sys.exit()

    amount_of_currency = input("Enter the amount of currency: ")
    try:
        amount_of_currency = float(amount_of_currency)
    except ValueError:
        print("Error: Must be a number")
        sys.exit()

    convert_to = input("Choose the currency type to convert to: ")
    convert_to = convert_to.upper()
    if convert_to not in currencies:
        print("Error: Not a currency type")
        sys.exit()

    converted = currency_convert(convert_from, convert_to, amount_of_currency)
    print(f"{amount_of_currency} {convert_from} is {converted} in {convert_to} currency")

if __name__ == "__main__":
    main()
