# Program to calculate the tax of married and unmarried person
def tax_payee_info(n):
    tax_payee_name = input("Enter Tax Payee Name [{0}]: ".format(n + 1))
    address = input("Address [{0}]: ".format(n + 1))
    pan_no = int(input("Enter Pan No. [{0}]: ".format(n + 1)))
    married_status = input("Enter 'Y' for Married and 'N' for Unmarried Status [{0}]: ".format(n + 1))
    for_year = input("Enter FY [{0}]: ".format(n + 1))
    monthly_income = int(input("Enter Tax Payee per month income [Rs.][{0}]: ".format(n + 1)))
    annual_income = monthly_income * 12

    return tax_payee_name, address, pan_no, married_status, for_year, annual_income


def calculate_tax_of_taxPayee(tax_payee_name, address, pan_no, married_status, for_year, annual_income):
    tax_payee_name, address, pan_no, married_status, for_year, annual_income = tax_payee_name, address, pan_no, married_status, for_year, annual_income

    def calculate_tax_of_taxPayee_married():
        tax = 0
        total = 0
        if annual_income <= 450000:
            a = annual_income * 0.01
            total += a
            tax += 1
        elif 450000 < annual_income <= 550000:
            a = 450000 * 0.01
            b = (annual_income - 450000) * 0.1
            tax += (1 + 10)
            total += a + b

        elif 550000 < annual_income <= 650000:
            a = 450000 * 0.01
            b = (550000 - 450000) * 0.1
            c = (annual_income - 550000) * 0.2
            tax += (1 + 10 + 20)
            total += a + b + c

        elif 650000 < annual_income <= 1250000:
            a = 450000 * 0.01
            b = (550000 - 450000) * 0.1
            c = (650000 - 550000) * 0.2
            d = (annual_income - 650000) * 0.3
            tax += (1 + 10 + 20 + 30)
            total += a + b + c + d

        elif 2000000 <= annual_income:
            a = 450000 * 0.01
            b = (550000 - 450000) * 0.1
            c = (650000 - 550000) * 0.2
            d = (1250000 - 650000) * 0.3
            e = (annual_income - 1250000) * 0.36
            tax += (1 + 10 + 20 + 30 + 36)
            total += a + b + c + d + e

        return tax, total

    def calculate_tax_of_taxPayee_unmarried():
        tax = 0
        total = 0
        if annual_income <= 400000:
            a = annual_income * 0.01
            total += a
            tax += 1

        elif 400000 < annual_income <= 500000:
            a = 400000 * 0.01
            b = (annual_income - 400000) * 0.1
            tax += (1 + 10)
            total += a + b

        elif 500000 < annual_income <= 600000:
            a = 400000 * 0.01
            b = (500000 - 400000) * 0.1
            c = (annual_income - 500000) * 0.2
            tax += (1 + 10 + 20)
            total += a + b + c

        elif 600000 < annual_income <= 1300000:
            a = 400000 * 0.01
            b = (500000 - 400000) * 0.1
            c = (600000 - 500000) * 0.2
            d = (annual_income - 600000) * 0.3
            tax += (1 + 10 + 20 + 30)
            total += a + b + c + d

        elif 2000000 <= annual_income:
            a = 400000 * 0.01
            b = (500000 - 400000) * 0.1
            c = (600000 - 500000) * 0.2
            d = (1300000 - 600000) * 0.3
            e = (annual_income - 1300000) * 0.36
            tax += (1 + 10 + 20 + 30 + 36)
            total += a + b + c + d + e

        return tax, total

    if married_status == 'Y':
        tax, total = calculate_tax_of_taxPayee_married()
        taxes = tax
        totals = total
        display_tax_payee(taxes, totals)
    else:
        tax, total = calculate_tax_of_taxPayee_unmarried()
        taxes = tax
        totals = total
        display_tax_payee(taxes, totals)


def data_static_info():
    print("\t\t\t\t\tInland Revenue Department")
    print("\t\t\t\t\t\tLazimpat, Kathmandu")
    print("\t\t\t\t\t\t\tWelcome to")
    print("\t\t\t\t\tIntegrated Tax System(ITS)")


def display_tax_payee(tax_payee_name, address, pan_no, married_status, for_year, annual_income, taxes, totals):
    tax, total = taxes, totals
    tax_payee_name, address, pan_no, married_status, for_year, annual_income = tax_payee_name, address, pan_no, married_status, for_year, annual_income
    print("Tax Payee: {0}\t\t\t\t\t\tAddress: {1}".format(tax_payee_name, address))
    print("PAN No: {0}\t\t\tFY: {1}\t\t\tMarried Status = {2}".format(pan_no, for_year, married_status))
    print()
    print("Tax Payee {0} with PAN {1} fall under {2}% Tax salb.".format(tax_payee_name, pan_no, tax))
    print("{0} (PAN {1}) to pay tax to government is [Rs.] = {2}".format(tax_payee_name, pan_no, total))


def main():
    data_static_info()
    tax_paye_no = int(input("Enter the number of tax payee: "))
    payers = []

    for n in range(tax_paye_no):
        payers.append(tax_payee_info(n)) #appending to list
        print()

    for x in payers:
        print(payers)


main()

f = open("tax.txt", "w+")
f.write(data_static_info())
f.write(main())
f.write(display_tax_payee())
f.close()

f = open("tax.txt", "r")
print(f.read())
f.close()

