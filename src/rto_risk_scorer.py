"""
Cash on Delivery (COD) Return-to-Origin (RTO) Risk Scorer
Predictive risk scoring for MENA e-commerce orders:
- Historical buyer behavior (past cancellations / uncollected parcels)
- Address completeness index (missing street, missing building #, vague location)
- High basket value COD penalty
- Recommends operational intervention: Auto-Approve, WhatsApp OTP, or Require Prepaid Card
"""
import re
import json
import argparse
from typing import Dict, Any

VAGUE_ADDRESS_WORDS = ["قريب من", "بجوار", "عند السنترال", "شارع رئيسي", "near", "opposite"]

def score_cod_order(order: Dict[str, Any]) -> Dict[str, Any]:
    score = 0  # 0 to 100 risk scale
    reasons = []
    
    payment_method = order.get("payment_method", "COD").upper()
    if payment_method != "COD":
        return {
            "order_id": order.get("order_id"),
            "rto_risk_score": 5,
            "risk_tier": "LOW",
            "recommended_action": "AUTO_FULFILL",
            "reasons": ["Prepaid payment method eliminates RTO refusal risk"]
        }
        
    # Baseline COD risk
    score += 20
    
    # 1. Past cancellation history
    past_orders = order.get("past_order_count", 0)
    past_returns = order.get("past_rto_count", 0)
    if past_orders > 0:
        return_rate = past_returns / past_orders
        if return_rate > 0.4:
            score += 35
            reasons.append(f"High historical return rate: {round(return_rate*100)}%")
    else:
        # First time buyer
        score += 15
        reasons.append("First-time COD buyer")
        
    # 2. Address quality check
    address = order.get("shipping_address", "").lower()
    if len(address) < 15:
        score += 20
        reasons.append("Address is too short (< 15 characters)")
    if any(w in address for w in VAGUE_ADDRESS_WORDS):
        score += 10
        reasons.append("Address uses vague descriptive landmarks without building number")
        
    # 3. Basket value check
    amount = float(order.get("total_amount", 0.0))
    if amount > 1500:
        score += 15
        reasons.append("High basket value for COD order (> 1500)")
        
    final_score = min(100, score)
    
    if final_score >= 65:
        tier = "HIGH"
        action = "REQUIRE_PREPAID_OR_CALL_VERIFY"
    elif final_score >= 40:
        tier = "MEDIUM"
        action = "SEND_WHATSAPP_OTP_CONFIRMATION"
    else:
        tier = "LOW"
        action = "AUTO_FULFILL"
        
    return {
        "order_id": order.get("order_id", "ORD_UNKNOWN"),
        "rto_risk_score": final_score,
        "risk_tier": tier,
        "recommended_action": action,
        "reasons": reasons
    }

def main():
    sample = {
        "order_id": "ORD-5542",
        "payment_method": "COD",
        "past_order_count": 0,
        "shipping_address": "قريب من السنترال",
        "total_amount": 1800
    }
    res = score_cod_order(sample)
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
