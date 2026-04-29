# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

print("📈 Welcome to Stock Portfolio Tracker")

total_investment = 0

while True:

    # User input
    stock_name = input("\nEnter stock name (AAPL/TSLA/GOOG/MSFT) or 'done' to finish: ").upper()

    # Exit condition
    if stock_name == "DONE":
        break

    # Check stock exists
    if stock_name not in stock_prices:
        print("❌ Stock not found!")
        continue

    # Quantity input
    quantity = int(input("Enter quantity: "))

    # Calculate investment
    investment = stock_prices[stock_name] * quantity

    # Add to total
    total_investment += investment

    print(f"✅ {stock_name} Investment = ${investment}")

# Final total
print("\n💰 Total Investment Value = $", total_investment)

# Save result to text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")

print("📁 Result saved in portfolio.txt")