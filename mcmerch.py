def main():
    inputNumItems = int(input("Enter the number of items: "))
    inputPrice = float(input("Enter the price of the item: "))
    inputProvince = str(input("Enter the province code: "))

    total_cost = inputNumItems * inputPrice

    discount = calculate_discount(total_cost)
    after_discount = total_cost - discount

    tax = calculate_province_tax(after_discount, inputProvince)
    after_tax_discount = after_discount + tax
    print("Total cost: ${:.2f}".format(after_tax_discount))

def calculate_province_tax(total_cost, province):
    """ Add province tax to the total cost based on the province code. """
    if province in tax_rates:
        return total_cost * tax_rates[province]

    else:
        print("Unknown province code. No tax applied.")
        return 0

def calculate_discount(total_cost):
    """ Calculate the discount for the given total cost. """
    for threshold, discount_rate in discounts:
        if total_cost >= threshold:
            return total_cost * discount_rate
    return 0


tax_rates = {
    "QC": 0.14975,
    "ON": 0.13,
    "MB": 0.05,
    "NS": 0.15,
    "BC": 0.05,
}

discounts = [
    (50000, 0.15),
    (10000, 0.10),
    (7000, 0.07),
    (5000, 0.05),
    (1000, 0.03),
]

if __name__ == "__main__":
    main()