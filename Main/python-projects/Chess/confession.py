def yes_or_no():
    response = input("do you love me (yes/no): ").lower()

    if response == "yes":
        confession = input("do you want a kiss? ")
        print(f"Your confession: {confession}")

    elif response == "no":
        confession = input("What did you do this time? ")
        print(f"Your confession: {confession}")

    else:
        print("Please respond with 'yes' or 'no'.")
        yes_or_no()

yes_or_no()