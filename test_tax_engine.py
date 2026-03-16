import unittest
from tax_engine import TaxEngine

class TestTaxEngine(unittest.TestCase):
    def setUp(self):
        # Wird vor jedem Test ausgeführt
        self.engine = TaxEngine()

    def test_fifo_logic(self):
        # Prüft, ob Gewinne korrekt nach dem FIFO-Prinzip berechnet werden
        self.engine.buy(10, 100)  # Tranche 1
        self.engine.buy(10, 150)  # Tranche 2
        
        # 10 Stück von 100€ zu 200€ -> 1000€ Gewinn
        # 5 Stück von 150€ zu 200€ -> 250€ Gewinn
        # Gesamt: 1250€
        self.engine.sell(15, 200)
        
        self.assertEqual(self.engine.realized_gain, 1250.0)
        self.assertEqual(len(self.engine.holdings), 1, "Es sollte noch eine Tranche übrig sein.")
        self.assertEqual(self.engine.holdings[0]['amount'], 5, "Die zweite Tranche sollte noch 5 Stück enthalten.")

if __name__ == '__main__':
    unittest.main()