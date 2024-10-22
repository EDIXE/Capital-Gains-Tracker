from linked_deque import LinkedDeque
from ledger_entry import LedgerEntry
from stock_purchase import StockPurchase

class StockLedger:
    def __init__(self):
        self.entries = LinkedDeque()

    def buy(self, stock_symbol, shares_bought, price_per_share):
        for _ in range(shares_bought):
            purchase = StockPurchase(stock_symbol, price_per_share)
            if self.contains(stock_symbol):
                entry = self.get_entry(stock_symbol)
                entry.add_purchase(purchase)
            else:
                new_entry = LedgerEntry(stock_symbol)
                new_entry.add_purchase(purchase)
                self.entries.add_to_back(new_entry)

    def sell(self, stock_symbol, shares_sold, price_per_share):
        if self.contains(stock_symbol):
            entry = self.get_entry(stock_symbol)
            sold = entry.remove_purchase(price_per_share, shares_sold)
            if sold > 0:
                print(f"Sold {sold} shares of {stock_symbol} at {price_per_share}.")
        else:
            print("Stock not found.")

    def display_ledger(self):
        current = self.entries.front
        print("---- Stock Ledger ----")
        while current is not None:
            current.get_data().display_entry()
            current = current.get_next_node()

    def contains(self, stock_symbol):
        current = self.entries.front
        while current is not None:
            if current.get_data().equals(LedgerEntry(stock_symbol)):
                return True
            current = current.get_next_node()
        return False

    def get_entry(self, stock_symbol):
        current = self.entries.front
        while current is not None:
            if current.get_data().equals(LedgerEntry(stock_symbol)):
                return current.get_data()
            current = current.get_next_node()
        return None

