import math
import re
from datetime import datetime

# --- CONFIGURATION & SYSTEM IDENTITY ---
PROGRAM_NAME = "STRATEGIC FINANCIAL ASSET ADVISOR"

# --- NLP ENGINE: INTENT & CATEGORY MAPPING ---
NLP_KEYWORDS = {
    "Groceries": ["milk", "food", "vegetables", "fruits", "market", "ration", "grocery", "eggs"],
    "Bills": ["electricity", "water", "wifi", "recharge", "gas", "bill", "rent", "internet"],
    "EMI": ["loan", "installment", "car payment", "home loan", "emi", "credit card", "debt"],
    "Recreational/Fun": ["movie", "party", "trip", "netflix", "gaming", "swiggy", "zomato", "restaurant", "pub"],
    "Other Needs": ["medicine", "doctor", "fuel", "petrol", "repairs", "service", "pharmacy"]
}

def nlp_engine(user_input):
    amounts = re.findall(r'\d+', user_input)
    amount = float(amounts[0]) if amounts else 0.0
    
    detected_cat = "Other Needs"
    for category, keywords in NLP_KEYWORDS.items():
        if any(word in user_input.lower() for word in keywords):
            detected_cat = category
            break
    return detected_cat, amount

def calculate_monthly_tax(monthly_salary):
    annual_income = monthly_salary * 12
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

# SYSTEM INITIALIZATION 
print(f"{'='*65}\n {PROGRAM_NAME}\n{'='*65}")

# 1. USER ONBOARDING
name = input("Full Name: ").strip().upper()
age = int(input(" Age: "))
gross_salary = float(input(" Gross Monthly Salary (₹): "))

# NEW: GOAL INPUT
print("\n--- FINANCIAL GOAL SETUP ---")
goal_name = input("Enter your dream goal (Car/House/Trip): ")
goal_amount = float(input("Estimated cost of your goal (₹): "))

# 2. AUTO-RISK & TAX ANALYTICS
monthly_tax = calculate_monthly_tax(gross_salary)
net_income = gross_salary - monthly_tax

# Age-Based Asset Allocation
if age < 35:
    risk_profile, strategy = "AGGRESSIVE (GROWTH)", [0.10, 0.30, 0.60]
elif 35 <= age <= 55:
    risk_profile, strategy = "BALANCED (MODERATE)", [0.40, 0.40, 0.20]
else:
    risk_profile, strategy = "CONSERVATIVE (SAFE)", [0.70, 0.20, 0.10]

# 3. EXPENSE LOGGING
expenses = []
print(f"\nProfile Initialized: {risk_profile}")
print("--- NATURAL LANGUAGE LOGGING ENGINE ---")
print("Type expenses like: 'Spent 500 on milk'")
print("(Type 'PROCESS' to generate report)")

while True:
    entry = input("You: ")
    if entry.lower() == 'process': break
    
    cat, amt = nlp_engine(entry)
    if amt > 0:
        expenses.append({"cat": cat, "amt": amt})
        print(f"Bot: Allocated ₹{amt:,} to {cat}.")
    else:
        print("Bot: No amount detected.")

# 4. DATA SYNTHESIS
total_spent = sum(e['amt'] for e in expenses)
surplus = net_income - total_spent
utilization_ratio = (total_spent / net_income) * 100 if net_income > 0 else 100

#  NEW: GOAL CALCULATION 
monthly_goal_investment = max(0, surplus * 0.20)

if monthly_goal_investment > 0:
    months_to_goal = goal_amount / monthly_goal_investment
    years_to_goal = months_to_goal / 12
else:
    months_to_goal = 0
    years_to_goal = 0

# 5. REPORT
print(f"\n{'='*65}\nFINANCIAL AUDIT\n{'='*65}")
print(f"CLIENT: {name} | AGE: {age} | STRATEGY: {risk_profile}")
print(f"Net Income: ₹{net_income:,.2f}")
print(f"Total Spent: ₹{total_spent:,.2f}")

# Credit Score
credit_score = 850 if utilization_ratio < 30 else 720 if utilization_ratio < 60 else 540
print(f"CREDIT SCORE: {credit_score}/900")

# Status
if utilization_ratio > 85:
    print("STATUS: CRITICAL")
elif utilization_ratio > 60:
    print("STATUS: CAUTION")
else:
    print("STATUS: HEALTHY")

# Savings
target_savings = net_income * 0.20
print(f"SAVINGS TARGET: ₹{math.floor(target_savings):,}")

# Investment
if surplus > 0:
    print("\nASSET ALLOCATION:")
    print(f"FD: ₹{math.floor(surplus * strategy[0]):,}")
    print(f"SIP: ₹{math.floor(surplus * strategy[1]):,}")
    print(f"STOCKS: ₹{math.floor(surplus * strategy[2]):,}")

# --- NEW: GOAL OUTPUT ---
print(f"\n🎯 GOAL: {goal_name.upper()} (₹{goal_amount:,.0f})")
if monthly_goal_investment > 0:
    print(f"Monthly Investment: ₹{math.floor(monthly_goal_investment):,}")
    print(f"Time to Achieve: {math.ceil(months_to_goal)} months (~{years_to_goal:.1f} years)")
else:
    print("Goal not achievable with current finances.")

print(f"{'='*65}")
