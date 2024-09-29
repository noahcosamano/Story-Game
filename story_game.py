import random

TIME_PERIOD = "2024"

currency_multipliers = {
    "US_DOL": 1,
    "GMN_DEM": 381.25,
    "JPN_YEN": 142.22,
    "FRN_EUR": 0.9,
    "UK_PD": 0.75,
    "CHN_YUAN": 7.01,
    "RSN_RBL": 94.36,
    "IRAN_RIAL": 42105
}

country_to_currency = {
    "USA": "US_DOL",
    "United States": "US_DOL",
    "US": "US_DOL",
    "Germany": "GMN_DEM",
    "Japan": "JPN_YEN",
    "France": "FRN_EUR",
    "UK": "UK_PD",
    "United Kingdom": "UK_PD",
    "Great Britain": "UK_PD",
    "Britain": "UK_PD",
    "China": "CHN_YUAN",
    "Russia": "RSN_RBL",
    "Iran": "IRAN_RIAL"
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
        return "Leading"
    
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
    
def currency_conversion(value, currency_type):
    """Convert the given value using the corresponding currency multiplier."""
    if currency_type in currency_multipliers:
        multiplier = currency_multipliers[currency_type]
        converted_amount = value * multiplier
        return converted_amount
    else:
        raise ValueError("Invalid currency type provided.")

def type_of_currency():
    country_currency = input("Enter the currency type: ")
    if currency



def main():
    beginning_country_value = rand_country_value()
    beginning_class_value = rand_class_value()
    country_name = start_country(beginning_country_value)
    article = "the" if country_name in ["USA", "United Kingdom"] else "" # Fix space in else statement
    print("The year is",TIME_PERIOD,"in",article,start_country(beginning_country_value),". It is your job as a(n)",start_class(beginning_class_value),
    "citizen to lead your country to worldwide rule!")
    

if __name__ == "__main__":
    main()
