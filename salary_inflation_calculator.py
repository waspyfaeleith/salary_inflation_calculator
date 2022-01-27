from decimal import *
from datetime import datetime

rates = [
    # this data is from https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/czbh/mm23
    {"year": 2000, "rate": 3.0},
    {"year": 2001, "rate": 1.8},
    {"year": 2002, "rate": 1.7},
    {"year": 2003, "rate": 2.9},
    {"year": 2004, "rate": 3.0},
    {"year": 2005, "rate": 2.8},
    {"year": 2006, "rate": 3.2},
    {"year": 2007, "rate": 4.3},
    {"year": 2008, "rate": 4.0},
    {"year": 2009, "rate": -0.5},
    {"year": 2010, "rate": 4.6},
    {"year": 2011, "rate": 5.2},
    {"year": 2010, "rate": 3.2},
    {"year": 2013, "rate": 3.0},
    {"year": 2014, "rate": 2.4},
    {"year": 2015, "rate": 1.0},
    {"year": 2016, "rate": 1.8},
    {"year": 2017, "rate": 3.6},
    {"year": 2018, "rate": 3.3},
    {"year": 2019, "rate": 2.6},
    {"year": 2020, "rate": 1.5},
    {"year": 2021, "rate": 4.1},
]


def filter_rates(rates, year):
    filtered_rates = []
    for rate in rates:
        if rate["year"] > year:
            filtered_rates.append(rate)
    return filtered_rates


def get_multiplier(rate):
    multiplier = rate / 100
    return multiplier


def calc_inflated_salary(rates, base_salary):
    salary = float(base_salary)
    for rate in rates:
        inflation_rate = rate["rate"]
        multiplier = get_multiplier(inflation_rate)
        salary += salary * multiplier
        print(f'{rate["year"]} : { round(salary,2)}')
    return Decimal(salary)


base_salary = int(input("Enter your starting salary: "))
year = int(input("Enter the year you started: "))


inflation_linked_salary = calc_inflated_salary(filter_rates(rates, year), base_salary)

print(
    f"A salary of £{base_salary} in {year} would be worth £{round(inflation_linked_salary,2)} in {datetime.today().year}"
)
