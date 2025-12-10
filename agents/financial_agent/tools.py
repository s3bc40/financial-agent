def get_financial_summary(quarter: str) -> dict:
    """
    Retrieve the financial summary for a given quarter,
    including Revenue, Cost of Goods Sold (COGS), and Operating Expenses (OPEX).
    The quarter must be formatted as 'QX-YYYY', e.g., 'Q4-2025'.

    Args:
        quarter (str): The quarter for which to retrieve the financial summary.

    Returns:
        dict: A dictionary with financial data and error handling.
    """
    # Mock data for demonstration purposes
    data = {
        "Q1-2025": {"Revenue": 150000, "COGS": 90000, "OPEX": 40000},
        "Q2-2025": {"Revenue": 180000, "COGS": 110000, "OPEX": 45000},
        "Q3-2025": {"Revenue": 200000, "COGS": 120000, "OPEX": 50000},
        "Q4-2025": {"Revenue": 220000, "COGS": 130000, "OPEX": 55000},
    }
    return data.get(
        quarter,
        {"error": f"Data not available for {quarter}. Try 'Q1-2025' to 'Q4-2025'."},
    )


def recommend_cost_cut(department: str) -> dict:
    """
    Provide cost-cutting recommendations for a specified department.

    Args:
        department (str): The department for which to provide recommendations.
        (e.g., 'Marketing', 'Sales', 'R&D', 'Operations').

    Returns:
        dict: A dictionary with cost-cutting recommendations and estimated savings.
    """
    if department.lower() == "marketing":
        return {"action": "Reduce PPC spend by 15% immediately", "savings": 450000}
    elif department.lower() == "sales":
        return {
            "action": "Implement remote selling to cut travel costs",
            "savings": 600000,
        }
    elif department.lower() == "r&d":
        return {"action": "Postpone non-critical projects", "savings": 250000}
    else:
        return {
            "action": "Review non-critical vendor contracts across departments",
            "savings": 200000,
        }
