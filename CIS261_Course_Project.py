

# Daneisha Hunt CIS261 Create and Call Functions with Parameters
# Payroll Program using lists and dictionaries
# Using Files to Store and Retrieve Data

file_name = "Employee_data.txt"


def get_pay_period_dates():
    """This Function is added per Phase 2 - this function asks for the pay period 
    dates and returns both values. The assignment requires this to be the first 
    function called in the loop."""
    
    from_date = input("\nEnter FROM date (mm/dd/yyyy): ")
    to_date = input("Enter TO date (mm/dd/yyyy): ")
    return from_date, to_date

def get_employee_name():
    """Prompt the user for an employee name and return it."""
    
    name = input("\nEnter employee name (or 'End' to finish): ")
    return name

def get_total_hours():
    """Prompt the user for total hours worked and return it as a float. This allows decimal values"""
    
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

def display_employee(from_date, to_date, name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
    """Display one employee's payroll results."""
    
    print("\n--- Employee Payroll ---")
    print(f"From Date: {from_date}")
    print(f"To Date: {to_date}")
    print(f"Employee Name: {name}")
    print(f"Total Hours Worked: {hours}")
    print(f"Hourly Rate: {rate}")
    print(f"Gross Pay: {gross_pay}")
    print(f"Income Tax Rate: {tax_rate}")
    print(f"Income Taxes: {income_tax}")
    print(f"Net Pay: {net_pay}")

def display_totals(totals):
    """Display totals for all employess after the loop ends."""
    """Phase 2 change: Totals are stored in a dictionary."""
    
    print("\n--- Payroll Totals ---")
    print(f"Total Number of Employees: {totals ['employee_count']}")
    print(f"Total Hours Worked: {totals ['total_hours']}")
    print(f"Total Gross Pay: {totals ['total_gross_pay']}")
    print(f"Total Income Taxes: {totals ['total_income_taxes']}")
    print(f"Total Net Pay: {totals ['total_net_pay']}")

def process_payroll(from_dates, to_dates, names, hours_list, rates, tax_rates):
    """This function runs after all employees are entered.
    It loops through the list, calculates payroll, displays each employee,
    builds totals in a dictionary"""

    #Creates a dictionary to store totals
    totals = {
        "employee_count": 0,
        "total_hours": 0.0,
        "total_gross_pay": 0.0,
        "total_income_taxes": 0.0,
        "total_net_pay": 0.0}

    # Loop through all employees using index numbers
    for i in range(len(names)):

        #Get employee data from lists
        from_date = from_dates[i]
        to_date = to_dates[i]
        name = names[i]
        hours = hours_list[i]
        rate = rates[i]
        tax_rate = tax_rates[i]

        #Calculate payroll
        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)

        #Display employee payroll
        display_employee(from_date, to_date, name, hours, rate, gross_pay, tax_rate, income_tax, net_pay)

        #Update totals dictionary
        totals["employee_count"] += 1
        totals["total_hours"] += hours
        totals["total_gross_pay"] += gross_pay
        totals["total_income_taxes"] += income_tax
        totals["total_net_pay"] += net_pay 

    return totals

# phase 3

def save_employee_record(from_date, to_date, name, hours, rate, tax_rate):
    with open(file_name, "a") as file:
        record = f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax_rate}\n"
        file.write(record)

def is_valid_date_mmddyyyy(date_text):
    if len(date_text) != 10:
        return False
    if date_text[2] != "/" or date_text[5] != "/":
        return False

    for i in range(10):
        if i != 2 and i != 5:
            if not date_text[i].isdigit():
                return False
    return True

def get_report_from_date():
    while True:
        user_input = input("\nEnter From date for report (mm/dd/yyyy) or All: ")
        if user_input.upper() == "ALL":
            return user_input

        if is_valid_date_mmddyyyy(user_input):
            return user_input

        print("Invalid date format. Please try again.")

def display_records(from_date_filter):
    print("\nEmployee Records")

    with open(file_name, "r") as file:
        for line in file:
            data = line.strip().split("|")

            record_from_date = date[0]

            if from_date_filter.upper() == "ALL" or record_from_date == from_date_filter:
                print(line.strip())


#Main Program

def main():

    #list to store employee data (phase 2 changes)
    from_dates = []
    to_dates = []
    names = []
    hours_list = []
    rates = []
    tax_rates = []

    while True:  #call dates first then store inputs
        from_date, to_date = get_pay_period_dates()

        name = get_employee_name()

        # Stop Condition
        if name == "End":
            break

        # Get employee data
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        # Store data into lists
        """.append() is used to store each employee's data into a list 
        so it can be processed later after the input loop ends."""
        from_dates.append(from_date)
        to_dates.append(to_date)
        names.append(name)
        hours_list.append(hours)
        rates.append(rate)
        tax_rates.append(tax_rate)

    #process payrol after all input
    totals = process_payroll(from_dates, to_dates, names, hours_list, rates, tax_rates)

    #Display totals
    display_totals(totals)

#start Program
main()



     


        






