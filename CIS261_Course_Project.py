# Daneisha Hunt CIS261 Create and Call Functions with Parameters
# Payroll Proof of concept

def get_employee_name():
    """Prompt the user for an employee name and return it."""
    name = input("Enter employee name (or 'End' to finish): ")
    return name

def get_total_hours():
    """Prompt the user for total hours worked and return it as a float."""
    hours = float(input("Enter total hours worked: "))
    return hours

def get_hourly_rate():
    """Prompt the user for hourly rate and return it as a float."""
    rate = float(input("Enter hourly rate: "))
    return rate

def get_tax_rate():
    """Prompt the user for tax rate and return it as a float. Example: .20 for 20%"""
    tax_rate = float(input("Enter income tax rate (example: .20 for 20%): "))
    return tax_rate

def calculate_pay(hours, rate, tax_rate):
    """Calculate gross pay, income tax and net pay. Returns: gross_pay, income_tax, net_pay"""
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
    print("\n--- Employee Payroll ---")
    print(f"Name: {name}")
    print(f"Hours Worked: {hours}")
    print(f"Hourly Rate: {rate}")
    print(f"Gross Pay: {gross_pay}")
    print(f"Tax Rate: {tax_rate}")
    print(f"Income Tax: {income_tax}")
    print(f"Net Pay: {net_pay}")

def display_totals(employee_count, total_hours, total_gross, total_tax, total_net):
    print("\n--- Payroll Totals ---")
    print(f"Total Employees: {employee_count}")
    print(f"Total Hours: {total_hours}")
    print(f"Total Gross Pay: {total_gross}")
    print(f"Total Income Taxes: {total_tax}")
    print(f"Total Net Pay: {total_net}")

# Main Program Loop

if __name__ == "__main__":
    employee_count = 0


