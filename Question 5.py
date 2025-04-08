print("Welcome to the Cookie Dough Fundraiser Tracker!")
print("Enter each classmate's name and how many buckets they sold.")
print("Press enter without typing a name to finish.\n")

sales = {}
name = "start"

for i in range(100):
    name = input("Enter classmate's name: ").title()
    if name == "":
        break

    buckets_input = input(f"How many buckets did {name} sell? ")
    if buckets_input.isdigit():
        buckets = int(buckets_input)
        if name in sales:
            sales[name] += buckets
        else:
            sales[name] = buckets
    else:
        print("Invalid number, skipping this entry.\n")

print("\nFundraiser Results:")
for name in sales:
    total = sales[name]
    prizes = total // 10
    print(f"{name} can redeem {prizes} prize(s) (Total buckets: {total})")