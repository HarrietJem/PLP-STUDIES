def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompts the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function to calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Display the result
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else:
        print(f"Discount applied! The final price is: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numerical values for price and discount.")
