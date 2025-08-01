(ONLINEGDB HAS FULL CODE AND DEPLOYABLE OPTION)


# Real Estate Investment Analyzer
# Calculates cash flow, cash-on-cash return, and cap rate from user input

from datetime import datetime

# Main function to run the analysis
def analyze_property():
    # Get input from user with validation
    def get_float_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    # Collect input
    income = get_float_input("Enter monthly rental income ($): ")
    expenses = get_float_input("Enter monthly expenses ($): ")
    price = get_float_input("Enter property purchase price ($): ")
    cash_invested = get_float_input("Enter total cash invested ($): ")

    # Calculations
    monthly_cash_flow = income - expenses
    annual_cash_flow = monthly_cash_flow * 12
    coc_return = (annual_cash_flow / cash_invested) * 100 if cash_invested else 0
    cap_rate = (annual_cash_flow / price) * 100 if price else 0

    # Results
    print("\n=== Investment Results ===")
    print(f"Monthly Cash Flow: ${monthly_cash_flow:.2f}")
    print(f"Annual Cash Flow: ${annual_cash_flow:.2f}")
    print(f"Cash-on-Cash Return: {coc_return:.2f}%")
    print(f"Cap Rate: {cap_rate:.2f}%")

    # Log results to file
    with open("investment_log.txt", "a") as log:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"\n\nDate: {now}")
        log.write(f"\nMonthly Income: ${income}")
        log.write(f"\nMonthly Expenses: ${expenses}")
        log.write(f"\nProperty Price: ${price}")
        log.write(f"\nCash Invested: ${cash_invested}")
        log.write(f"\nCash Flow: ${monthly_cash_flow}")
        log.write(f"\nAnnual Cash Flow: ${annual_cash_flow}")
        log.write(f"\nCoC Return: {coc_return:.2f}%")
        log.write(f"\nCap Rate: {cap_rate:.2f}%")
        log.write("\n--------------------------")

# Main entry point
def main():
    print("Welcome to the Real Estate Investment Analyzer!")
    analyze_property()

if __name__ == "__main__":
    main()
