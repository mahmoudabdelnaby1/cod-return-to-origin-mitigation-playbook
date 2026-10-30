"""
Unit tests for COD RTO Risk Scorer
"""
import unittest
from src.rto_risk_scorer import score_cod_order

class TestRTOScorer(unittest.TestCase):
    def test_prepaid_is_low_risk(self):
        order = {"order_id": "P1", "payment_method": "CREDIT_CARD", "total_amount": 5000}
        res = score_cod_order(order)
        self.assertEqual(res["risk_tier"], "LOW")
        self.assertEqual(res["recommended_action"], "AUTO_FULFILL")

    def test_vague_cod_high_risk(self):
        order = {
            "order_id": "C1",
            "payment_method": "COD",
            "past_order_count": 2,
            "past_rto_count": 2,
            "shipping_address": "بجوار المسجد",
            "total_amount": 2000
        }
        res = score_cod_order(order)
        self.assertEqual(res["risk_tier"], "HIGH")
        self.assertEqual(res["recommended_action"], "REQUIRE_PREPAID_OR_CALL_VERIFY")

if __name__ == "__main__":
    unittest.main()
