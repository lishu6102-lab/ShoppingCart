"""Console-Based Shopping Cart System — Frozen Design Version 1.0.

Change the three example starting stock quantities below if needed.
Requires Python 3.10 or newer for match-case.
"""

Products = ["Pen", "Notebook", "Bag"]
Price = [10.0, 50.0, 500.0]

# Example starting quantities; exact starting quantities were not finalized.
Stock = {"Pen": 20, "Notebook": 15, "Bag": 10}

TempStock = []
CartQuantity = []

for i in range(len(Products)):
    TempStock.append(Stock[Products[i]])
    CartQuantity.append(0)


def DisplayCatalogue():
    print("\nHere is the Product Catalogue")
    for i in range(len(Products)):
        print("Product Number:", i + 1)
        print("Product Name:", Products[i])
        print("Price:", Price[i])
        print("Quantity Left:", TempStock[i])
        print()


def ConfirmExit():
    while True:
        print("Do you wish to exit?")
        print("0 = Confirm Exit")
        print("1 = Cancel Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "0":
                return True
            case "1":
                return False
            case _:
                print("Invalid input. Please try again.")


def GetInput(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "0":
            exit_confirmed = ConfirmExit()
            if exit_confirmed:
                raise SystemExit
            continue  # Return to the same prompt when exit is cancelled.
        return user_input


def GetValidInput(prompt, accepted_values):
    while True:
        user_input = GetInput(prompt)
        if user_input in accepted_values:
            return user_input
        print("Invalid input. Please try again.")


def AddProduct(item_number):
    index = item_number - 1

    if TempStock[index] == 0:
        print("Product is out of stock.")
        return

    while True:
        quantity_input = GetInput("Enter quantity: ")
        try:
            quantity = int(quantity_input)
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        if 1 <= quantity <= TempStock[index]:
            CartQuantity[index] = CartQuantity[index] + quantity
            TempStock[index] = TempStock[index] - quantity
            return
        print("Invalid input. Please try again.")


def RemoveProduct():
    if all(quantity == 0 for quantity in CartQuantity):
        print("Your cart is empty.")
        return

    print("Products in your cart")
    for i in range(len(Products)):
        if CartQuantity[i] > 0:
            print(i + 1, Products[i], CartQuantity[i])

    while True:
        item_input = GetInput("Enter product number to remove: ")
        try:
            item_number = int(item_input)
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        index = item_number - 1
        if 0 <= index < len(Products) and CartQuantity[index] > 0:
            break
        print("Invalid input. Please try again.")

    while True:
        removal_input = GetInput("Enter quantity to remove: ")
        try:
            RemovalQuantity = int(removal_input)
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        if 1 <= RemovalQuantity <= CartQuantity[index]:
            CartQuantity[index] = CartQuantity[index] - RemovalQuantity
            TempStock[index] = TempStock[index] + RemovalQuantity
            return
        print("Invalid input. Please try again.")


def ResetCart():
    for i in range(len(Products)):
        CartQuantity[i] = 0
        TempStock[i] = Stock[Products[i]]


def CalculateBill():
    if all(quantity == 0 for quantity in CartQuantity):
        print("Your cart is empty.")
        return False

    subtotal = 0.0
    for i in range(len(Products)):
        item_total = Price[i] * CartQuantity[i]
        subtotal = subtotal + item_total

    if subtotal > 500:
        discount = subtotal * 0.10
    else:
        discount = 0.0

    gst = (subtotal - discount) * 0.18
    grand_total = subtotal - discount + gst

    print("Here is your bill:")
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("GST:", gst)
    print("Grand Total:", grand_total)
    return True


def ConfirmPurchase():
    while True:
        choice = GetValidInput(
            "Enter 1 to confirm purchase or 0 to exit: ", ["1"]
        )
        match choice:
            case "1":
                for i in range(len(Products)):
                    Stock[Products[i]] = TempStock[i]
                print("Purchase Successful")
                ResetCart()
                return


def main():
    while True:
        DisplayCatalogue()

        while True:
            if all(quantity == 0 for quantity in CartQuantity):
                item_input = GetValidInput(
                    "Select product: 1, 2, 3 or 8 to remove: ",
                    ["1", "2", "3", "8"],
                )
            else:
                item_input = GetValidInput(
                    "1, 2, 3 = Product, 5 = Continue, 6 = Billing, "
                    "7 = Reset, 8 = Remove: ",
                    ["1", "2", "3", "5", "6", "7", "8"],
                )

            match item_input:
                case "1" | "2" | "3":
                    item_number = int(item_input)
                    AddProduct(item_number)
                    continue
                case "5":
                    continue
                case "6":
                    bill_created = CalculateBill()
                    if bill_created:
                        ConfirmPurchase()
                        break
                    continue
                case "7":
                    ResetCart()
                    continue
                case "8":
                    RemoveProduct()
                    continue


if __name__ == "__main__":
    main()
