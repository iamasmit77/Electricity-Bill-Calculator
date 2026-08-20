#electric bill calculator
print("================================")
print("================================")
print("   ELECTRICITY BILL CALCULATOR")
print("================================")
print("================================")


# Function to calculate energy charge
def calculate_energy_charge(units):

    if units <= 100:
        return units * 3

    elif units <= 200:
        return (100 * 3) + ((units - 100) * 5)

    elif units <= 300:
        return (100 * 3) + (100 * 5) + ((units - 200) * 7)

    else:
        return (100 * 3) + (100 * 5) + (100 * 7) + ((units - 300) * 8)


# Function to calculate late fee
def calculate_late_fee(late_payment):

    if late_payment == "yes":
        return 50
    else:
        return 0


# Function to calculate total bill
def calculate_total(energy_charge, fixed_charge, late_fee):

    return energy_charge + fixed_charge + late_fee


# Taking customer information
name = input("Enter customer name: ")
meter_number = input("Enter meter number: ")
month = input("Enter billing month: ")


# Validating units
try:
    units = float(input("Enter electricity units: "))

    if units < 0:
        print("Units cannot be negative.")
        exit()

except ValueError:
    print("Please enter a valid number.")
    exit()


# Calculating energy charge
energy_charge = calculate_energy_charge(units)


# Fixed charge
fixed_charge = 100


# Taking late payment input
while True:

    late_payment = input("Is payment late? (yes/no): ").lower()

    if late_payment == "yes":
        late_fee = calculate_late_fee(late_payment)
        break

    elif late_payment == "no":
        late_fee = calculate_late_fee(late_payment)
        break

    else:
        print("Please enter only yes or no.")


# Calculating total bill
total_bill = calculate_total(
    energy_charge,
    fixed_charge,
    late_fee
)


# Displaying final bill
print("================================")
print("================================")
print("          ELECTRICITY BILL")
print("================================")
print("================================")

print("Customer Name :", name)
print("Meter Number  :", meter_number)
print("Billing Month :", month)
print("Units Used    :", units)

print("--------------------------------")
print("Energy Charge :", energy_charge)
print("Fixed Charge  :", fixed_charge)
print("Late Fee      :", late_fee)
print("--------------------------------")

print("TOTAL BILL    :", total_bill)

print("================================")
print("================================")