def add_tax(cost_list, tax):
    taxed_list = []
    for cost in cost_list:
        taxed_list.append(cost * (1 + tax))
    return taxed_list

num_purchases = int(input("Number of purchases: "))
tax = float(input("Sales tax: "))

name_list = []
cost_list = []

for i in range(num_purchases):
    name_list.append(input("Customer: "))
    cost_list.append(float(input("Cost: ")))

cost_list_taxed = add_tax(cost_list, tax)

customer_dict = {}

for i in range(len(name_list)):
    if name_list[i] not in customer_dict:
        customer_dict[name_list[i]] = cost_list_taxed[i]
    else:
        customer_dict[name_list[i]] += cost_list_taxed[i]

print(customer_dict)
