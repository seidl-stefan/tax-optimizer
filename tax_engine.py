# Kleine Tax-Engine von Stefan

import json

class TaxEngine:
    def __init__(self):
        # Für Tranchen nehme ich Dictionarys: {'amount': 10, 'price': 100}, {'amount': 10, 'price': 150}, usw.
        # Jede Tranche wird als ein Element einer Liste abgespeichert bzw. angehängt
        self.holdings = [] 
        self.realized_gain = 0.0
        self.tax_rate = 0.26375  # 26,375% = Abgeltungsteuer = KapESt + Soli (+ eventuell Kirchensteuer)
        self.current_market_price = 0.0

    def buy(self, amount, price):
        self.holdings.append({'amount': amount, 'price': price})

    def sell(self, amount_to_sell, market_price):
        current_gain = 0.0
        remaining_to_sell = amount_to_sell
        while remaining_to_sell > 0 and self.holdings:
            oldest_tranche = self.holdings[0]
            if oldest_tranche['amount'] <= remaining_to_sell:
                qty = oldest_tranche['amount']
                current_gain += qty * (market_price - oldest_tranche['price'])
                remaining_to_sell -= qty
                self.holdings.pop(0)
            else:
                qty = remaining_to_sell
                current_gain += qty * (market_price - oldest_tranche['price'])
                oldest_tranche['amount'] -= qty
                remaining_to_sell = 0
        self.realized_gain += current_gain

    def get_harvesting_potential(self):
        potential_loss = 0.0
        for t in self.holdings:
            if t['price'] > self.current_market_price:
                potential_loss += t['amount'] * (self.current_market_price - t['price'])
        return potential_loss

    def load_scenario(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.current_market_price = data.get('market_price', 0)
            for t in data['transactions']:
                if t['action'] == 'buy':
                    self.buy(t['amount'], t['price'])

    def report_status(self):
        potential = self.get_harvesting_potential()
        tax_saving = abs(potential) * self.tax_rate
        
        print("\n")
        print("="*50)       
        print("TAX ENGINE REPORT")
        print("="*50)
        print(f"Aktueller Kurs:      {self.current_market_price:>8.2f}€")
        print(f"Realisierbarer Gewinn: {self.realized_gain:>8.2f}€")
        print("-"*50)
        print(f"Loss Harvesting Potenzial: {abs(potential):>8.2f}€")
        print(f"Mögliche Steuerersparnis:  {tax_saving:>8.2f}€")
        print("="*50)
        print("\n" + "\n")


if __name__ == "__main__":
    # 1. Instanz für manuellen Test
    print("\n" + "TEST 1: MANUELL")
    engine_manual = TaxEngine()
    engine_manual.current_market_price = 200 # aktueller Preis
    engine_manual.buy(10, 100)
    engine_manual.buy(10, 150)
    engine_manual.sell(15, 200)
    engine_manual.report_status()
    engine_manual.current_market_price = 120 # Preis ist spontan gefallen
    engine_manual.report_status()

    # 2. Instanz für externe Daten
    print("\n" + "TEST 2: JSON")
    engine_external = TaxEngine()
    engine_external.load_scenario('transactions_with_a_plus.json')
    #engine.load_scenario('transactions_with_a_minus.json') 
    engine_external.report_status()

