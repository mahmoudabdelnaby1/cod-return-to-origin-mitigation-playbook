# Cash on Delivery (COD) Return-to-Origin (RTO) Mitigation Playbook

> A planning playbook for measuring and addressing Cash on Delivery return-to-origin risk. It does not claim a measured reduction or production-tested flows.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: TEMPLATE_FRAMEWORK](https://img.shields.io/badge/Format-TEMPLATE--FRAMEWORK-green.svg)](#)
[![Tier: 1](https://img.shields.io/badge/Tier-1-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**BOTH** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an open-source COD Return-to-Origin (RTO) mitigation toolkit for MENA: 1) operational playbook (Pre-Purchase Friction, WhatsApp 1-Click Confirmation, Prepaid Incentive Surcharges, Courier SLA Tracking, Blacklist Governance), 2) WhatsApp automated confirmation message templates (Arabic and English), 3) Python risk scoring script (`rto_risk_scorer.py`), 4) Courier handover reconciliation sheet.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `examples/riyadh-fashion-rto-case.md`
- `LICENSE`
- `models/cod-unit-economics-calculator.xlsx`
- `playbooks/cod-otp-verification-sop.md`
- `playbooks/rto-mitigation-master-playbook.md`
- `README.md`
- `scripts/rto_risk_scorer.py`
- `src/rto_risk_scorer.py`
- `templates/courier-sla-scorecard.md`
- `templates/whatsapp-confirmation-flows.md`
- `tests/test_rto.py`
- `tests/test_scorer.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/rto_risk_scorer.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "e-commerce",
  "repository": "cod-return-to-origin-mitigation-playbook",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Multi-Pillar Risk Scoring:** Calculates RTO probability based on address completeness, previous order refusal history, and city delivery performance.
- **Pre-Purchase Friction Rules:** Offers optional confirmation and incentive ideas to evaluate against customer experience, local rules, and account data.
- **Courier SLA Handover Tracking:** Tracks last-mile courier attempts, requiring automated WhatsApp intervention upon the first failed delivery attempt.

---

## 📚 Primary Documentation & Verifiable References

- [Saudi Ministry of Commerce: E-Commerce Delivery and Cancellation Regulations](https://mc.gov.sa/) - Statutory rules governing merchant delivery timelines and customer cancellation rights.
- [Baymard Institute: Cash on Delivery Friction in Emerging Markets](https://baymard.com/) - Empirical analysis of customer refusal drivers and checkout payment incentives.
- [Salla Platform Documentation: COD Order Verification Flows](https://docs.salla.dev/) - Storefront integration for managing cash on delivery orders and OTP validation.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
