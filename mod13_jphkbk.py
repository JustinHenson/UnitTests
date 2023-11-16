import unittest
from datetime import datetime

def valid_input(symbol, chart_type, time_series, start_date, end_date):
    # Validates Stock Symbol Format
    if not (symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7):
        return False
    
    # Validates Chart Type Choice
    if not (chart_type.isdigit() and chart_type in ["1", "2"]):
        return False
    
    # Validates Time Series Choice
    if not (time_series.isdigit() and 1 <= int(time_series) <= 4):
        return False
    
    # Validates Start and End Date format: YYYY-MM-DD
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return False
    
    return True

class TestUserInputs(unittest.TestCase):

    # Tests known good inputs
    def test_valid_inputs(self):
        self.assertTrue(valid_input("IBM", "1", "1", "2020-01-01", "2021-01-01"))

    # Test NonValid Symbol Input
    def test_symbol_validation(self):
        self.assertFalse(valid_input("321", "1", "2", "2020-01-01", "2021-01-01"))

    # Tests NonValid Chart Type Input
    def test_chartType_validation(self):
        self.assertFalse(valid_input("IBM", "3", "1", "2020-01-01", "2021-01-01"))

    # Tests NonValid Time Series Input
    def test_timeSeries_validation(self):
        self.assertFalse(valid_input("IBM", "1", "5", "2020-01-01", "2021-01-01"))

    # Tests NonValid DataTime Start Input
    def test_dateTimeStart_validation(self):
        self.assertFalse(valid_input("IBM", "1", "1", "01-01-2020", "2021-01-01"))

    # Tests NonValid DataTime Start End Input
    def test_dateTimeEnd_validation(self):
        self.assertFalse(valid_input("IBM", "1", "1", "2020-01-01", "01-01-2021"))

if __name__ == "__main__":
    unittest.main()