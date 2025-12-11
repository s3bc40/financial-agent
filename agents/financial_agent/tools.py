from agents.financial_agent.mock_data import DATA_ERROR_MESSAGES, FINANCIAL_DATA


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
    # Handle the specific missing quarter
    if quarter == "Q3-2025":
        return {"error": DATA_ERROR_MESSAGES["missing"]}

    # Handle future quarters (general error)
    if quarter in ["Q1-2026", "Q2-2026"]:
        return {"error": DATA_ERROR_MESSAGES["future"].format(quarter=quarter)}

    # Retrieve data from the imported dictionary
    return FINANCIAL_DATA.get(
        quarter,
        {
            "error": f"Data not available for {quarter}. Try a quarter between 'Q1-2024' and 'Q4-2025'."
        },
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
