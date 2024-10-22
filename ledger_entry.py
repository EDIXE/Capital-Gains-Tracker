from linked_deque import LinkedDeque
from stock_purchase import StockPurchase

class LedgerEntry:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.purchases = {}

    def add_purchase(self, stock_purchase):
        price = stock_purchase.cost_per_share
        if price in self.purchases:
            self.purchases[price] += 1
        else:
            self.purchases[price] = 1

    def remove_purchase(self, price, shares_to_sell):
        if price in self.purchases:
            if self.purchases[price] >= shares_to_sell:
                self.purchases[price] -= shares_to_sell
                if self.purchases[price] == 0:
                    del self.purchases[price]
                return shares_to_sell
        return 0
    
    def equals(self, other):
        if isinstance(other, LedgerEntry):
            return self.stock_symbol == other.stock_symbol
        return False

    def display_entry(self):
        display_str = f"{self.stock_symbol}: "
        display_parts = []

        for price, shares in self.purchases.items():
            display_parts.append(f"{price} ({shares} shares)")

        display_str += ", ".join(display_parts)
        print(display_str)


