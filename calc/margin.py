"""rental-vs-mining margin calculator.
Usage: python3 calc/margin.py --mhs 1150 --rent 0.16 --price 172.27
Revenue ref: ~$6.52 per GH/s/day (QPoW, early Oct 2026).
"""
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--mhs", type=float, required=True, help="hashrate in MH/s")
ap.add_argument("--rent", type=float, required=True, help="rental $/hour")
ap.add_argument("--price", type=float, default=172.27, help="token $ price")
ap.add_argument("--rev-per-gh", type=float, default=6.52, help="$ revenue per GH/s/day")
a = ap.parse_args()
gross = a.mhs / 1000 * a.rev_per_gh
cost = a.rent * 24
print(f"gross $/day : {gross:.2f}")
print(f"cost  $/day : {cost:.2f}")
print(f"margin$/day : {gross - cost:+.2f}")
print(f"breakeven $/h: {gross / 24:.4f}  |  breakeven token $: {a.price * cost / gross:.2f} (at same netrev)")
