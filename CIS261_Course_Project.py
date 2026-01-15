

# Daneisha Hunt CIS261 Create and Call Functions with Parameters
# Payroll Proof of concept

def get_employee_name():
    """Prompt the user for an employee name and return it."""
    name = input("\nEnter employee name (or 'End' to finish): ")
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
    """Display one employee's payroll results."""
    print("\n--- Employee Payroll ---")
    print(f"Emplyee Name: {name}")
    print(f"Total Hours Worked: {hours}")
    print(f"Hourly Rate: {rate}")
    print(f"Gross Pay: {gross_pay}")
    print(f"Income Tax Rate: {tax_rate}")
    print(f"Income Taxes: {income_tax}")
    print(f"Net Pay: {net_pay}")

def display_totals(employee_count, total_hours, total_gross_pay, total_income_taxes, total_net_pay):
    """Display totals for all employess after the loop ends."""
    print("\n--- Payroll Totals ---")
    print(f"Total Number of Employees: {employee_count}")
    print(f"Total Hours Worked: {total_hours}")
    print(f"Total Gross Pay: {total_gross_pay}")
    print(f"Total Income Taxes: {total_income_taxes}")
    print(f"Total Net Pay: {total_net_pay}")

# Main Program Loop

if __name__ == "__main__":
    
    #running totals
    employee_count = 0
    total_hours = 0.0
    total_gross_pay = 0.0
    total_income_taxes = 0.0
    total_net_pay = 0.0

    while True:
        name = get_employee_name()

        # Stop Condition
        if name == "End":
            break

        # Input Functions
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        # Calculate function (parameters in, values returned)
        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)

        # Display employee results
        display_employee(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay)

        # Update Totals
        employee_count += 1
        total_hours += hours
        total_gross_pay += gross_pay
        total_income_taxes += income_tax
        total_net_pay += net_pay

    # Display totals after all employees entered
    display_totals(employee_count, total_hours, total_gross_pay, total_income_taxes, total_net_pay)







