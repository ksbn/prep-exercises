# Exercise: Add type annotations, run through mypy, and fix all bugs.
 
# Bugs found by mypy:
# 1. open_account("Tobi", 9.13) - missing first argument `balances`, wrong type for amount (float not int)
# 2. open_account("Olya", "£7.13") - missing first argument `balances`, amount is a string not int
# 3. format_pence_as_str() - wrong function name, should be format_pence_as_string()
 
def open_account(balances: dict[str, int], name: str, amount: int) -> None:
    balances[name] = amount
 
def sum_balances(accounts: dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total
 
def format_pence_as_string(total_pence: int) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = int(total_pence / 100)
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"
 
balances = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}
 
open_account(balances, "Tobi", 913)   # Fix 1: added balances, converted 9.13 to pence (913)
open_account(balances, "Olya", 713)   # Fix 2: added balances, converted "£7.13" to pence (713)
 
total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)  # Fix 3: corrected function name
 
print(f"The bank accounts total {total_string}")
 