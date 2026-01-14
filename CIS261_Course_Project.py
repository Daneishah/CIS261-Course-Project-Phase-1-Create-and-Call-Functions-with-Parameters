# Daneisha Hunt CIS261 Create and Call Functions with Parameters

def get_employee_name():
    name = input("Enter employee name (or End to finish):")
    return name

def get_total_hours():
    hours = float(input("Enter total hours worked:"))
    return hours

def get_hourly_rate():
    rate = float(input("Enter hourly rate:"))
    return rate

def get_tax_rate():
    tax_rate = float(input("Enter income tax rate (example: .20 for 20%):"))
    return tax_rate

def calculate_pay():
    gross_pay = hours * rate
    income_tax = gross_pay * get_tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
