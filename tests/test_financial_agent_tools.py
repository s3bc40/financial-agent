import pytest

from agents.financial_agent.tools import get_financial_summary, recommend_cost_cut


# --- Test Cases for get_financial_summary ---
@pytest.mark.parametrize(
    "quarter_input, expected_revenue, expected_cogs, expected_opex",
    [
        # Test Case 1: Known quarter (Q4-2025)
        ("Q4-2025", 220000, 130000, 55000),
        # Test Case 2: Known quarter (Q3-2025)
        ("Q3-2025", 200000, 120000, 50000),
    ],
)
def test_get_financial_summary_known_quarters(
    quarter_input, expected_revenue, expected_cogs, expected_opex
):
    result = get_financial_summary(quarter_input)

    assert result["Revenue"] == expected_revenue
    assert result["COGS"] == expected_cogs
    assert result["OPEX"] == expected_opex
    assert "error" not in result


def test_get_financial_summary_unknown_quarter():
    """Tests the function handles an unknown quarter by returning an error dictionary."""
    unknown_quarter = "Q1-2026"
    result = get_financial_summary(unknown_quarter)

    assert "error" in result
    assert unknown_quarter in result["error"]


# --- Test Cases for recomment_cost_cut ---
@pytest.mark.parametrize(
    "department_input, expected_action, expected_savings",
    [
        # Test Case 1: Marketing Department
        ("Marketing", "Reduce PPC spend by 15% immediately", 450000),
        # Test Case 2: Sales Department
        ("Sales", "Implement remote selling to cut travel costs", 600000),
        # Test Case 3: R&D Department and case insensitivity
        ("r&d", "Postpone non-critical projects", 250000),
        # Test Case 4: Unknown Department
        ("HR", "Review non-critical vendor contracts across departments", 200000),
    ],
)
def test_recommend_cost_cut_specific_departments(
    department_input, expected_action, expected_savings
):
    """Tests if the function returns the correct recommendation and savings for various departments."""
    result = recommend_cost_cut(department_input)

    assert result["action"] == expected_action
    assert result["savings"] == expected_savings
    assert isinstance(result, dict)
