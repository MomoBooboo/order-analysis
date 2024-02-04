import unittest
import pandas as pd
from main import read_orders_csv, compute_total_revenue_by_month, compute_total_revenue_by_product, compute_total_revenue_by_customer, identify_top_customers

class TestOrderAnalysis(unittest.TestCase):
    def setUp(self):
        self.orders_df = pd.DataFrame({
            'order_id': [1, 2, 3],
            'customer_id': [101, 102, 101],
            'order_date': ['2022-01-01', '2022-02-01', '2022-01-15'],
            'product_id': [1, 2, 1],
            'product_name': ['A', 'B', 'A'],
            'product_price': [10, 20, 15],
            'quantity': [2, 1, 3]
        })

    def test_read_orders_csv(self):
        file_path = "test_orders.csv"
        self.orders_df.to_csv(file_path, index=False)
        result = read_orders_csv(file_path)
        self.assertTrue(result.equals(self.orders_df))

    def test_compute_total_revenue_by_month(self):
        result = compute_total_revenue_by_month(self.orders_df)
        expected_result = pd.Series([45, 20], name='product_price', dtype='float64', index=pd.PeriodIndex(['2022-01', '2022-02'], freq='M'))
        pd.testing.assert_series_equal(result, expected_result)

    def test_compute_total_revenue_by_product(self):
        result = compute_total_revenue_by_product(self.orders_df)
        expected_result = pd.Series([25, 20], name='product_price', dtype='float64', index=['A', 'B'])
        pd.testing.assert_series_equal(result, expected_result)

    def test_compute_total_revenue_by_customer(self):
        result = compute_total_revenue_by_customer(self.orders_df)
        expected_result = pd.Series([25, 20], name='product_price', dtype='float64', index=[101, 102])
        pd.testing.assert_series_equal(result, expected_result)

    def test_identify_top_customers(self):
        result = identify_top_customers(self.orders_df)
        expected_result = pd.Series([25, 20], name='product_price', dtype='float64', index=[101, 102])
        pd.testing.assert_series_equal(result, expected_result)

if __name__ == '__main__':
    unittest.main()
