import yfinance as yf
import mplfinance as mpf

def get_stock_symbol(company_name):
    try:
        stock_info = yf.Ticker(company_name)
        symbol = stock_info.info['symbol']
        return symbol
    except Exception as e:
        return f"Error finding stock symbol: {e}"

def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period='1d')
        return data
    except Exception as e:
        return f"Error fetching stock data: {e}"

def display_stock_info(company_name, symbol, data):
    if isinstance(data, str):
        print(data)
    else:
        print(f"\nStock Information for {company_name} ({symbol}):")
        print(data)

        # Plotting the candlestick chart
        mpf.plot(data, type='candle', volume=True, show_nontrading=True, title=f"Stock Price for {company_name}")

if __name__ == "__main__":
    while True:
        # Prompt the user to enter the company name
        company_name = input("Enter the company name for a Swedish company (or type 'exit' to end): ")

        if company_name.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        # Get stock symbol
        stock_symbol = get_stock_symbol(company_name)

        if stock_symbol.startswith("No data"):
            print(f"No stock symbol found for {company_name}. Please check the company name.")
        else:
            # Get stock data
            stock_data = get_stock_data(stock_symbol)

            # Display stock information and plot candlestick chart
            display_stock_info(company_name, stock_symbol, stock_data)

            # Ask if the user wants to check another company
            another_company = input("\nDo you want to check another company? (yes/no): ").lower()
            if another_company != 'yes':
                print("Exiting the program. Goodbye!")
                break
