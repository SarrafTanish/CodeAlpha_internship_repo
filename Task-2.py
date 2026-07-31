
import csv

# Hardcoded stock prices (in a real app these might come from an API)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 185,
    "META": 470,
    "NFLX": 650,
}


def show_available_stocks() -> None:
    """Print the list of stocks and their prices the user can choose from."""
    print("\nAvailable stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")


def get_portfolio() -> dict:
    """Ask the user for stock symbols and quantities, return them as a dict."""
    portfolio = {}

    print("\nEnter your holdings. Type 'done' as the stock symbol when finished.")
    while True:
        symbol = input("Stock symbol: ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' is not in the price list. Try one of the available stocks.")
            continue

        quantity_input = input(f"Quantity of {symbol}: ").strip()
        if not quantity_input.isdigit():
            print("  Please enter a whole number for quantity.")
            continue

        quantity = int(quantity_input)

        # If the user enters the same stock twice, add to the existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"  Added: {quantity} share(s) of {symbol}")

    return portfolio


def calculate_investment(portfolio: dict) -> tuple:
    """
    Calculate the value of each holding and the total investment.
    Returns (line_items, total) where line_items is a list of
    (symbol, quantity, price, value) tuples.
    """
    line_items = []
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        line_items.append((symbol, quantity, price, value))
        total += value

    return line_items, total


def display_summary(line_items: list, total: float) -> None:
    """Print a formatted summary of the portfolio to the console."""
    print("\n--- Portfolio Summary ---")
    print(f"{'Stock':<8}{'Qty':<6}{'Price':<10}{'Value':<10}")
    for symbol, quantity, price, value in line_items:
        print(f"{symbol:<8}{quantity:<6}${price:<9}${value:<9}")
    print("-" * 34)
    print(f"Total Investment: ${total}")


def save_to_txt(line_items: list, total: float, filename: str = "portfolio_summary.txt") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("=" * 34 + "\n")
        f.write(f"{'Stock':<8}{'Qty':<6}{'Price':<10}{'Value':<10}\n")
        for symbol, quantity, price, value in line_items:
            f.write(f"{symbol:<8}{quantity:<6}${price:<9}${value:<9}\n")
        f.write("-" * 34 + "\n")
        f.write(f"Total Investment: ${total}\n")
    print(f"Saved summary to {filename}")


def save_to_csv(line_items: list, total: float, filename: str = "portfolio_summary.csv") -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for symbol, quantity, price, value in line_items:
            writer.writerow([symbol, quantity, price, value])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])
    print(f"Saved summary to {filename}")


def main() -> None:
    print("=== Stock Portfolio Tracker ===")
    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    line_items, total = calculate_investment(portfolio)
    display_summary(line_items, total)

    choice = input("\nSave summary to a file? (txt/csv/no): ").strip().lower()
    if choice == "txt":
        save_to_txt(line_items, total)
    elif choice == "csv":
        save_to_csv(line_items, total)
    else:
        print("Summary not saved.")


if __name__ == "__main__":
    main()