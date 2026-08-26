amount = int(input("Enter the recharge amount: "))
if amount >= 3599:
    print("Plan Amount: ₹3599")
    print("Unlimited 5G + 2.5GB/day\n365 days validity\nUnlimited calls")
elif amount >= 899:
    print("Plan Amount: ₹899")
    print("Unlimited 5G + 2GB/day\n90 days validity\nUnlimited calls")
elif amount >= 349:
    print("Plan Amount: ₹349")
    print("Unlimited 5G + 2GB/day\n28 days validity\nUnlimited calls")
elif amount >= 299:
    print("Plan Amount: ₹299")
    print("1.5GB/day\n28 days validity\nUnlimited calls")
elif amount >= 200:
    print("Plan Amount: ₹200")
    print("Unlimited 5G+\n28 days validity\nCalls NA")
else:
    print("Invalid recharge amount")