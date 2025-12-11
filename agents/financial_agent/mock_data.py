# --- Financial Data for 2024 and 2025 ---
# Data simulates a professional services firm's performance.

FINANCIAL_DATA = {
    # --- YEAR 2024: Historical Data with a Problem ---
    # Q4-2024 is the LOSS SCENARIO, showing high operating expenses that resulted in a negative margin.
    "Q1-2024": {"Revenue": 250000, "COGS": 80000, "OPEX": 150000},
    "Q2-2024": {"Revenue": 260000, "COGS": 85000, "OPEX": 155000},
    "Q3-2024": {"Revenue": 280000, "COGS": 95000, "OPEX": 170000},
    "Q4-2024": {"Revenue": 300000, "COGS": 110000, "OPEX": 210000},
    # --- YEAR 2025: Recovery and Margin Compression ---
    # Q3-2025 is deliberately missing to test data-gap handling.
    "Q1-2025": {"Revenue": 340000, "COGS": 105000, "OPEX": 195000},
    "Q2-2025": {"Revenue": 380000, "COGS": 115000, "OPEX": 220000},
    "Q4-2025": {"Revenue": 420000, "COGS": 135000, "OPEX": 250000},
}

# --- Tool for Cost-Cutting Recommendations ---
COST_CUTTING_ACTIONS = {
    "high_cost_action": "Implement a hiring freeze for non-essential roles, saving 20% of OpEx in 3 months.",
    "low_cost_action": "Review non-critical vendor contracts across departments, leading to estimated savings of $200,000.",
}

# --- Error Messages for Missing/Future Data ---
DATA_ERROR_MESSAGES = {
    "missing": "Financials for Q3-2025 are delayed due to a systems migration. Data is currently unavailable.",
    "future": "Data is still being reconciled for {quarter}. Please try again next month.",
}
