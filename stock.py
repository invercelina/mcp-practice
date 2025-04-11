from mcp.server.fastmcp import FastMCP

mcp = FastMCP("StocksMCPServer")

@mcp.resource("market://state")
def get_market_state() -> str:
    """
    Get the current market state
    Returns:
        str: The current market state
    """
    return "Market is open"

@mcp.resource("market://stock/{symbol}")
def get_stock_price(symbol: str) -> float:
    """
    Get the current stock price for a given symbol.
    Args:
        symbol (str): The symbol of the stock to get the price for
    Returns:
        float: The current stock price
    """
    return f"The current stock price for {symbol} is 100.0"

@mcp.tool()
def buy_stock(symbol: str, quantity: int) -> str:
    """
    Buy a stock
    Args:
        symbol (str): The symbol of the stock to buy
        quantity (int): The quantity of the stock to buy
    Returns:
        str: The result of the buy
    """
    return f"Bought {quantity} shares of {symbol}"

@mcp.tool()
def sell_stock(symbol: str, quantity: int) -> str:
    """
    Sell a stock
    Args:
        symbol (str): The symbol of the stock to sell
        quantity (int): The quantity of the stock to sell
    Returns:
        str: The result of the sell
    """
    return f"Sold {quantity} shares of {symbol}"

@mcp.prompt()
def analyze_stock(symbol: str, last_years_profit: float, company_info: str) -> str:
    """
    Analyze a stock
    Args:
        symbol (str): The symbol of the stock to analyze
        last_years_profit (float): The last year's profit of the stock
        company_info (str): The company info of the stock
    Returns:
        str: The result of the analysis
    """
    return f"Analyzed {symbol} with last year's profit of {last_years_profit} and company info of {company_info}"

if __name__ == "__main__":
    mcp.run()