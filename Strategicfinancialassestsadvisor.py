import math
import re
from datetime import datetime

# --- CONFIGURATION & SYSTEM IDENTITY ---
PROGRAM_NAME = "STRATEGIC FINANCIAL ASSET ADVISOR"

# --- NLP ENGINE: INTENT & CATEGORY MAPPING ---
# Maps user keywords to specific financial categories
NLP_KEYWORDS = {
    "Groceries": ["milk", "food", "vegetables", "fruits", "market", "ration", "grocery", "eggs"],
    "Bills": ["electricity", "water", "wifi", "recharge", "gas", "bill", "rent", "internet"],
    "EMI": ["loan", "installment", "car payment", "home loan", "emi", "credit card", "debt"],
    "Recreational/Fun": ["movie", "party", "trip", "netflix", "gaming", "swiggy", "zomato", "restaurant", "pub"],
    "Other Needs": ["medicine", "doctor", "fuel", "petrol", "repairs", "service", "pharmacy"]
}

def nlp_engine(user_input):
    """Extracts Monetary Amount and Category from natural language sentences."""
    amounts = re.findall(r'\d+', user_input)
    amount = float(amounts[0]) if amounts else 0.0
    
    # Keyword matching for category identification
    detected_cat = "Other Needs"  # Default fallback
    for category, keywords in NLP_KEYWORDS.items():
        if any(word in user_input.lower() for word in keywords):
            detected_cat = category
            break
    return detected_cat, amount

def calculate_monthly_tax(monthly_salary):
    """Calculates estimated monthly income tax based on annual progressive slabs (₹)."""
    annual_income = monthly_salary * 12
    # Simplified Slab Logic
    if annual_income <= 300000:
        annual_tax = 0
    elif annual_income <= 700000:
        annual_tax = (annual_income - 300000) * 0.05
    elif annual_income <= 1000000:
        annual_tax = 20000 + (annual_income - 700000) * 0.10
    elif annual_income <= 1500000:
        annual_tax = 50000 + (annual_income - 1000000) * 0.15
    else:
        annual_tax = 125000 + (annual_income - 1500000) * 0.25
    
    return round(annual_tax / 12, 2)

# --- SYSTEM INITIALIZATION ---
print(f"{'='*65}\n️ {PROGRAM_NAME}\n{'='*65}")

# 1. USER ONBOARDING
name = input("Full Name: ").strip().upper()
age = int(input(" Age: "))
gross_salary = float(input(" Gross Monthly Salary (₹): "))

# 2. AUTO-RISK & TAX ANALYTICS
monthly_tax = calculate_monthly_tax(gross_salary)
net_income = gross_salary - monthly_tax

# Age-Based Asset Allocation Logic
if age < 35:
    risk_profile, strategy = "AGGRESSIVE (GROWTH)", [0.10, 0.30, 0.60] # [FD, SIP, Stocks]
elif 35 <= age <= 55:
    risk_profile, strategy = "BALANCED (MODERATE)", [0.40, 0.40, 0.20]
else:
    risk_profile, strategy = "CONSERVATIVE (SAFE)", [0.70, 0.20, 0.10]

# 3. INTERACTIVE NLP TRANSACTION LOGGING
expenses = []
print(f"\nProfile Initialized: {risk_profile}")
print(f"--- NATURAL LANGUAGE LOGGING ENGINE ---")
print("Ex: 'Spent 500 on milk', 'Paid 15000 for rent', '2000 for petrol'")
print("(Type 'PROCESS' to generate your final audit)")

while True:
    entry = input("You: ")
    if entry.lower() == 'process': break
    
    cat, amt = nlp_engine(entry)
    if amt > 0:
        expenses.append({"cat": cat, "amt": amt})
        print(f"🤖 Bot: Allocated ₹{amt:,} to {cat}.")
    else:
        print("🤖 Bot: No amount detected. Please state the price (e.g., '1000 for food').")

# 4. DATA SYNTHESIS
total_spent = sum(e['amt'] for e in expenses)
surplus = net_income - total_spent
utilization_ratio = (total_spent / net_income) * 100 if net_income > 0 else 100

# 5. FORMAL ADVISORY REPORT
print(f"\n\n{'='*65}\n{PROGRAM_NAME}: FINANCIAL AUDIT\n{'='*65}")
print(f"CLIENT: {name} | AGE: {age} | STRATEGY: {risk_profile}")
print(f"{'-'*65}")
print(f"Gross Monthly Salary:      ₹{gross_salary:,.2f}")
print(f"Projected Monthly Tax:     ₹{monthly_tax:,.2f}")
print(f"Net Realized Income:       ₹{net_income:,.2f}")
print(f"Total Expenditure:         ₹{total_spent:,.2f}")
print(f"{'-'*65}")

# Credit Health Forecast
credit_score = 850 if utilization_ratio < 30 else 720 if utilization_ratio < 60 else 540
print(f"CREDIT SCORE FORECAST:     {credit_score} / 900")

# Overspending Warning
if utilization_ratio > 85:
    print(" STATUS: CRITICAL - EXTREME CAPITAL EXHAUSTION.")
elif utilization_ratio > 60:
    print(" STATUS: CAUTIONARY - SPENDING EXCEEDS OPTIMAL RATIOS.")
else:
    print("STATUS: HEALTHY - EXCELLENT CASH FLOW MANAGEMENT.")

# Savings Target (20% of Net Income)
target_savings = net_income * 0.20
print(f"IDEAL SAVINGS TARGET:      ₹{math.floor(target_savings):,}")

# Strategic Asset Allocation
if surplus > 0:
    print(f"\nASSET ALLOCATION (Surplus ₹{surplus:,.0f}):")
    print(f" > Fixed Income (FD/Gold): ₹{math.floor(surplus * strategy[0]):,}")
    print(f" > Managed Funds (SIP):    ₹{math.floor(surplus * strategy[1]):,}")
    print(f" > Direct Equity (Stocks): ₹{math.floor(surplus * strategy[2]):,}")
else:
    print("\n📉 ALLOCATION SUSPENDED: Deficit or Zero Surplus detected.")

print(f"\n NEXT MONTH EXPENDITURE FORECAST: ₹{math.ceil(total_spent * 1.05):,}")
print(f"{'='*65}")
def get_risk_profile(age, income, total_expenses):
    """
    Categorises user into Safe, Balanced, or Aggressive 
    based on Age and Income Surplus ratio.
    """
    surplus = income - total_expenses
    surplus_ratio = (surplus / income) * 100 if income > 0 else 0

    # 1. AGGRESSIVE (High Growth)
    # Typically: Young (<35) OR High Surplus (>50% of income)
    if age < 35 or surplus_ratio > 50:
        profile = "AGGRESSIVE"
        description = "Focus on Equity/Stocks for high long-term wealth creation."
        allocation = "10% FD | 30% SIP | 60% Stocks"

    # 2. BALANCED (Moderate)
    # Typically: Middle age (35-55) OR Moderate Surplus (20-50%)
    elif 35 <= age <= 55 or 20 <= surplus_ratio <= 50:
        profile = "BALANCED"
        description = "Hybrid approach to balance growth with capital safety."
        allocation = "40% FD | 40% SIP | 20% Stocks"

    # 3. SAFE (Conservative)
    # Typically: Senior (>55) OR Low Surplus (<20%)
    else:
        profile = "SAFE"
        description = "Focus on Capital Preservation and steady interest income."
        allocation = "70% FD | 20% SIP | 10% Stocks"

    return profile, description, allocation

# --- Displaying the Logic for the Project ---
print(f"{'='*60}")
print("STRATEGIC RISK CATEGORIES (AGE & INCOME BASED)")
print(f"{'='*60}")

# Example 1: Young Professional
p1, d1, a1 = get_risk_profile(25, 80000, 30000)
print(f"CATEGORY: {p1}\nCriteria: Age < 35\nStrategy: {d1}\nMix:      {a1}\n")

# Example 2: Mid-Career Professional
p2, d2, a2 = get_risk_profile(45, 150000, 90000)
print(f"CATEGORY: {p2}\nCriteria: Age 35-55\nStrategy: {d2}\nMix:      {a2}\n")

# Example 3: Near Retirement / Low Surplus
p3, d3, a3 = get_risk_profile(60, 100000, 85000)
print(f"CATEGORY: {p3}\nCriteria: Age > 55 or Low Surplus\nStrategy: {d3}\nMix:      {a3}")
print(f"{'='*60}")
