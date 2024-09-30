import random
from googlesearch import search

TIME_PERIOD = "2024"

currencies = {
    "USD",
    "DEM",
    "Yen",
    "Euro",
    "Pound",
    "Yuan",
    "Ruble",
    "Rial",
}

currency_multipliers = {
    "USD": 1,
    "DEM": 381.25,
    "Yen": 142.22,
    "Euro": 0.9,
    "Pound": 0.75,
    "Yuan": 7.01,
    "Ruble": 94.36,
    "Rial": 42105
}

def rand_country_value():
    """Choose value for starting country"""
    beginning_country_value = int(random.randint(1,8))
    return beginning_country_value

def rand_class_value():
    """Choose value for starting class"""
    beginning_class_value = int(random.randint(1,100))
    return beginning_class_value

def start_class(beginning_class_value):
    """Converts starting value to class"""
    if beginning_class_value < 10:
        return "Lower Class"
    elif 10 <= beginning_class_value <= 60:
        return "Middle Class"
    elif 60 < beginning_class_value <= 90:
        return "Upper Class"
    elif 90 < beginning_class_value <= 100:
        return "Leader"
    
def start_country(beginning_country_value):
    """Converts starting value to country"""
    if beginning_country_value == 1:
        return("Germany")
    elif beginning_country_value == 2:
        return("Japan")
    elif beginning_country_value == 3:
        return("USA")
    elif beginning_country_value == 4:
        return("France")
    elif beginning_country_value == 5:
        return("United Kingdom")
    elif beginning_country_value == 6:
        return("China")
    elif beginning_country_value == 7:
        return("Russia")
    elif beginning_country_value == 8:
        return("Iran")

def currency_convert(convert_from,convert_to,amount_of_currency):
    if convert_from not in currency_multipliers or convert_to not in currency_multipliers:
        return "Invalid currency for simulation"
    amount_in_usd = amount_of_currency / currency_multipliers[convert_from]
    converted_amount = int(amount_in_usd * currency_multipliers[convert_to])
    return converted_amount


def main():
    beginning_country_value = rand_country_value()
    beginning_class_value = rand_class_value()
    country_name = start_country(beginning_country_value)
    class_name = start_class(beginning_class_value)
    article = "the" if country_name in ["USA", "United Kingdom"] else "" # Fix space in else statement
    article_two = "citizen" if class_name in ["Lower Class","Middle Class","Upper Class"] else "" # Fix space in else statement
    print("The year is",TIME_PERIOD,"in",article,start_country(beginning_country_value),". It is your job as a(n)",start_class(beginning_class_value),
    article_two,"to lead your country to worldwide rule!")
    print("Currency options are as follows: ",currencies)
    convert_from = input("Choose the currency to convert from: ")
    amount_of_currency = float(input("Enter the amount of currency: "))
    convert_to = input("Choose the currency to convert to: ")
    print(convert_from,"is",currency_convert(convert_from,convert_to,amount_of_currency),"in",convert_to,"currency")
    

if __name__ == "__main__":
    main()
