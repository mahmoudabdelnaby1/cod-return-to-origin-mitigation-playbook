#!/usr/bin/env python3
import sys

def score_rto_risk(order):
    risk = 0
    if order.get("payment_method") == "COD":
        risk += 40
    if not order.get("is_phone_verified"):
        risk += 35
    if order.get("order_value", 0) > 800:
        risk += 15
    return {
        "risk_score": risk,
        "recommendation": "BLOCK_COD_REQUIRE_PREPAID" if risk >= 75 else ("CALL_VERIFY" if risk >= 40 else "DISPATCH")
    }

if __name__ == "__main__":
    test_ord = {"payment_method": "COD", "is_phone_verified": False, "order_value": 950}
    print(score_rto_risk(test_ord))
