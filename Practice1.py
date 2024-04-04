userName = input("What is your name? ")
userB4Tax = float(input("Enter the amount of your purchase "))
userTaxed = userB4Tax * 0.1

print("\nHello ", userName, ", here is your sales receipt:")
print(format("Subtotal = $ ", '13s') + format(userB4Tax, ',.2f'))
print(format("     Tax = $   ", '13s') + format(userTaxed, ',.2f'))
print("             " +("-" * 8))
print(format("   Total = $ ", '13s') + format(userTaxed + userB4Tax, ',.2f'))
