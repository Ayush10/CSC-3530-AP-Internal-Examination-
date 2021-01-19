def status(value):
    income = int(input("Enter your per month income[Rs.]: "))
    annual = income * 12
    total = 0
    tax = 0
    for i in value:
        if i == 'Y' or i == 'y':
            if annual <= 450000:
                a = annual * 0.01
                total += a
                tax += 1
            elif 450000 < annual <= 550000:
                a = 450000 * 0.01
                b = (annual - 450000) * 0.1
                tax += (1 + 10)
                total += a + b

            elif 550000 < annual <= 650000:
                a = 450000 * 0.01
                b = (550000 - 450000) * 0.1
                c = (annual - 550000) * 0.2
                tax += (1 + 10 + 20)
                total += a + b + c

            elif 650000 < annual <= 1250000:
                a = 450000 * 0.01
                b = (550000 - 450000) * 0.1
                c = (650000 - 550000) * 0.2
                d = (annual - 650000) * 0.3
                tax += (1 + 10 + 20 + 30)
                total += a + b + c + d

            elif 2000000 <= annual:
                a = 450000 * 0.01
                b = (550000 - 450000) * 0.1
                c = (650000 - 550000) * 0.2
                d = (1250000 - 650000) * 0.3
                e = (annual - 1250000) * 0.36
                tax += (1 + 10 + 20 + 30 + 36)
                total += a + b + c + d + e

        elif value == 'N' or value == 'n':
            if annual <= 400000:
                a = annual * 0.01
                total += a
                tax += 1

            elif 400000 < annual <= 500000:
                a = 400000 * 0.01
                b = (annual - 400000) * 0.1
                tax += (1 + 10)
                total += a + b

            elif 500000 < annual <= 600000:
                a = 400000 * 0.01
                b = (500000 - 400000) * 0.1
                c = (annual - 500000) * 0.2
                tax += (1 + 10 + 20)
                total += a + b + c

            elif 600000 < annual <= 1300000:
                a = 400000 * 0.01
                b = (500000 - 400000) * 0.1
                c = (600000 - 500000) * 0.2
                d = (annual - 600000) * 0.3
                tax += (1 + 10 + 20 + 30)
                total += a + b + c + d

            elif 2000000 <= annual:
                a = 400000 * 0.01
                b = (500000 - 400000) * 0.1
                c = (600000 - 500000) * 0.2
                d = (1300000 - 600000) * 0.3
                e = (annual - 1300000) * 0.36
                tax += (1 + 10 + 20 + 30 + 36)
                total += a + b + c + d + e
    return tax, total

#Use function for the input
num = int(input("Enter the number of customers: "))
name = [None] * num
address = [None] * num
pan = [None] * num
married = [None] * num
taxes = [None] * num
amounts = [None] * num

print("\n\t\t\t\t\tInland Revenue Department")
print("\t\t\t\tWelcome to Integrated Tax System")

for count in range(num):
    print(f"\nNumber of Customer: {count+1}")
    name[count] = input("Name: ")
    address[count] = input("Address: ")
    pan[count] = input("Pan No.: ")
    married[count] = input("Enter 'Y' for Married and 'N' for Unmarried: ")
    tax, total = status(married)
    taxes[count] = tax
    amounts[count] = total

for i in range(num):
    print("------------------------------------------------------------------------------------------")
    print("\n\t\t\t\tInland Revenue Department")
    print(f"\t\t\t\t\tLazimpat, Kathmandu")
    print("\t\t\t\t\t\tWelcome to")
    print("\t\t\t\tIntegrated Tax System(ITS)\n")
    print(f"Tax Payee: {name[i]}\t\t\t\tAddress: {address[i]}")
    print(f"PAN No. {pan[i]}\t\t\tFY: 2020/21\t\t\tMarried Status = {married[i]}")
    print(f"Tax Payee {name[i]} with PAN {pan[i]} fall under ({taxes[i]})% Tax salb.")
    print(f"{name[i]} (PAN {pan[i]}) to pay tax to government is [Rs.]= {amounts[i]}")