import numpy as np
import matplotlib.pyplot as plt

class BertrandDynamics:
    def __init__(self, marginal_cost, market_size, max_price, max_underbid=0.08, price_sensitivity=2.0):
        """
        Initialisiert das dynamische Bertrand-Modell
        
        Parameters:
        marginal_cost (float): Grenzkosten der Produktion
        market_size (float): Marktgröße (maximale Nachfrage)
        max_price (float): Maximaler Startpreis
        max_underbid (float): Maximale Unterbietung pro Zeiteinheit (default: 8%)
        price_sensitivity (float): Wie stark reagieren Kunden auf Preisunterschiede
        """
        self.mc = marginal_cost
        self.market_size = market_size
        self.max_price = max_price
        self.max_underbid = max_underbid
        self.price_sensitivity = price_sensitivity
        
    def market_share(self, own_price, other_price):
        """
        Berechnet den Marktanteil basierend auf relativem Preisunterschied
        Verwendet eine logistische Funktion für smoothe Übergänge
        """
        if own_price >= self.max_price or other_price >= self.max_price:
            return 0
        
        price_diff = (other_price - own_price) / ((own_price + other_price) / 2)
        share = 1 / (1 + np.exp(-self.price_sensitivity * price_diff))
        return share
        
    def demand(self, price, own_share):
        """Lineare Nachfragefunktion mit Marktanteil"""
        base_demand = max(0, self.market_size * (1 - price/self.max_price))
        return base_demand * own_share
    
    def profit(self, own_price, other_price):
        """Berechnet den Gewinn eines Unternehmens"""
        share = self.market_share(own_price, other_price)
        quantity = self.demand(own_price, share)
        return (own_price - self.mc) * quantity
    
    def simulate(self, initial_price_1, initial_price_2, num_periods=50):
        """
        Simuliert die Preisdynamik über mehrere Perioden
        
        Parameters:
        initial_price_1 (float): Startpreis Unternehmen 1
        initial_price_2 (float): Startpreis Unternehmen 2
        num_periods (int): Anzahl der Simulationsperioden
        
        Returns:
        tuple: Arrays mit Preisen, Gewinnen und Marktanteilen beider Unternehmen
        """
        prices_1 = np.zeros(num_periods)
        prices_2 = np.zeros(num_periods)
        profits_1 = np.zeros(num_periods)
        profits_2 = np.zeros(num_periods)
        shares_1 = np.zeros(num_periods)
        shares_2 = np.zeros(num_periods)
        
        prices_1[0] = initial_price_1
        prices_2[0] = initial_price_2
        
        for t in range(num_periods-1):
            # Berechne Marktanteile
            shares_1[t] = self.market_share(prices_1[t], prices_2[t])
            shares_2[t] = self.market_share(prices_2[t], prices_1[t])
            
            # Berechne Gewinne
            profits_1[t] = self.profit(prices_1[t], prices_2[t])
            profits_2[t] = self.profit(prices_2[t], prices_1[t])
            
            # Preisanpassung mit maximaler Unterbietung
            if prices_1[t] > prices_2[t]:
                # Unternehmen 1 ist teurer und passt an
                new_price = max(
                    self.mc,
                    prices_2[t] * (1 - np.random.uniform(0, self.max_underbid))
                )
                prices_1[t+1] = new_price
                prices_2[t+1] = prices_2[t]
            else:
                # Unternehmen 2 ist teurer oder gleich teuer und passt an
                new_price = max(
                    self.mc,
                    prices_1[t] * (1 - np.random.uniform(0, self.max_underbid))
                )
                prices_2[t+1] = new_price
                prices_1[t+1] = prices_1[t]
        
        # Letzte Periode
        shares_1[-1] = self.market_share(prices_1[-1], prices_2[-1])
        shares_2[-1] = self.market_share(prices_2[-1], prices_1[-1])
        profits_1[-1] = self.profit(prices_1[-1], prices_2[-1])
        profits_2[-1] = self.profit(prices_2[-1], prices_1[-1])
        
        return prices_1, prices_2, profits_1, profits_2, shares_1, shares_2
    
    def plot_results(self, prices_1, prices_2, profits_1, profits_2, shares_1, shares_2):
        """Visualisiert die Simulationsergebnisse"""
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
        
        # Preise
        ax1.plot(prices_1, label='Unternehmen 1')
        ax1.plot(prices_2, label='Unternehmen 2')
        ax1.axhline(y=self.mc, color='r', linestyle='--', label='Grenzkosten')
        ax1.set_title('Preisentwicklung')
        ax1.set_ylabel('Preis')
        ax1.legend()
        
        # Gewinne
        ax2.plot(profits_1, label='Unternehmen 1')
        ax2.plot(profits_2, label='Unternehmen 2')
        ax2.set_title('Gewinnentwicklung')
        ax2.set_ylabel('Gewinn')
        ax2.legend()
        
        # Marktanteile
        ax3.plot(shares_1, label='Unternehmen 1')
        ax3.plot(shares_2, label='Unternehmen 2')
        ax3.set_title('Marktanteilsentwicklung')
        ax3.set_ylabel('Marktanteil')
        ax3.set_xlabel('Periode')
        ax3.legend()
        
        plt.tight_layout()
        plt.show()

# Beispiel für die Verwendung
model = BertrandDynamics(
    marginal_cost=10,
    market_size=1000,
    max_price=50,
    price_sensitivity=2.0  # Höhere Werte = stärkere Reaktion auf Preisunterschiede
)

# Simulation mit unterschiedlichen Startpreisen
prices_1, prices_2, profits_1, profits_2, shares_1, shares_2 = model.simulate(
    initial_price_1=45,
    initial_price_2=40
)

# Visualisierung der Ergebnisse
model.plot_results(prices_1, prices_2, profits_1, profits_2, shares_1, shares_2)