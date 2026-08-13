def age_calculator(birth_year, current_year):
    """
    Calculate the age based on birth year and current year.

    Parameters:
    birth_year (int): The year of birth.
    current_year (int): The current year.

    Returns:
    int: The calculated age.
    """
    return current_year - birth_year


def total_characters(string):
    """
    Calculate the total number of characters in a string.

    Parameters:
    string (str): The input string.

    Returns:
    int: The total number of characters in the string.
    """
    return len(string)


def welcome_message_to_country(name, country):
    """
    Generate a welcome message for a given name and country.

    Parameters:
    name (str): The name of the person.
    country (str): The country of the person.

    Returns:
    str: A welcome message including the country.
    """
    return f"Welcome, {name} from {country}!"