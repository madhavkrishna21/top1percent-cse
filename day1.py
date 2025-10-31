# day1.py
class Bill:
    def __init__(self, amount, tip_percent):
        self.amount = amount
        self.tip_percent = tip_percent
        self.tip = amount * (tip_percent / 100)
        self.total = amount + self.tip

    def save_receipt(self):
        with open("receipt.txt", "w", encoding="utf-8") as f:  
            f.write("=== TOP 1% RECEIPT ===\n")
            f.write(f"Bill: ₹{self.amount:.2f}\n")
            f.write(f"Tip ({self.tip_percent}%): ₹{self.tip:.2f}\n")
            f.write(f"Total: ₹{self.total:.2f}\n")
            f.write("Madhav Krishna | AI Startup 2030\n")
        print("Receipt saved to receipt.txt!")

amount = float(input("Bill amount ₹: "))
tip = float(input("Tip %: "))

bill = Bill(amount, tip)
print(f"\nTip: ₹{bill.tip:.2f}")
print(f"Total: ₹{bill.total:.2f}")
bill.save_receipt()
