# Dynamisches Bertrand-Duopol Modell

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Eine Python-Implementierung eines dynamischen Bertrand-Duopol Modells mit gradueller Preisanpassung und realistischer Marktaufteilung.

## 📝 Inhaltsverzeichnis
- [Überblick](#überblick)
- [Funktionen](#funktionen)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Mathematisches Modell](#mathematisches-modell)
  - [Parameter-Definitionen](#parameter-definitionen)
  - [Zeitliche Notation](#zeitliche-notation)
  - [Nachfragefunktion](#nachfragefunktion)
  - [Präzisierung der Übergangsbegriffe](#pr%C3%A4zisierung-der-%C3%BCbergangsbegriffe)
  - [Mathematische Einschränkungen](#mathematische-einschr%C3%A4nkungen)
- [Unterschiede zum klassischen Bertrand-Modell](#unterschiede-zum-klassischen-bertrand-modell)
- [Lizenz](#lizenz)

## 🎯 Überblick

Dieses Projekt implementiert eine erweiterte Version des klassischen Bertrand-Duopol Modells mit:
- Gradueller Preisanpassung
- Realistischer Marktaufteilung
- Dynamischer Zeitentwicklung
- Visualisierung der Ergebnisse

## 🔧 Funktionen

- Simulation der Preisentwicklung zweier konkurrierender Unternehmen
- Berechnung von Marktanteilen, Gewinnen und Nachfrage
- Visualisierung der Ergebnisse (Preise, Gewinne, Marktanteile)
- Konfigurierbare Parameter (Grenzkosten, Marktgröße, Preissensitivität)
- Maximal 8% Preisanpassung pro Zeiteinheit

## 📦 Installation

```bash
# Repository klonen
git clone https://github.com/LeonVries/basic
cd dynamic-bertrand-model

# Abhängigkeiten installieren
pip install numpy matplotlib
```

## 💻 Verwendung

```python
from bertrand_dynamics import BertrandDynamics

# Modell initialisieren
model = BertrandDynamics(
    marginal_cost=10,
    market_size=1000,
    max_price=50,
    price_sensitivity=2.0
)

# Simulation durchführen
prices_1, prices_2, profits_1, profits_2, shares_1, shares_2 = model.simulate(
    initial_price_1=45,
    initial_price_2=40,
    num_periods=50
)

# Ergebnisse visualisieren
model.plot_results(prices_1, prices_2, profits_1, profits_2, shares_1, shares_2)
```

## 📐 Mathematisches Modell

### Parameter-Definitionen

#### Klassische Parameter
- **`c`**: Grenzkosten der Produktion (marginal cost)
- **`market_size`**: Maximale Nachfragemenge bei Preis = 0 (entspricht Parameter `a` im klassischen Modell)
- **`max_price`**: Prohibitivpreis, bei dem Nachfrage = 0 (entspricht `a/b` im klassischen Modell)

**Zusammenhang zum klassischen Modell:**

Die Nachfragefunktion \( Q(p) = a - bp \) lässt sich wie folgt umschreiben:

\[
Q(p) = \text{market\_size} \cdot \left(1 - \frac{p}{\text{max\_price}}\right)
\]

Mit den Beziehungen:
- \( a = \text{market\_size} \)
- \( b = \frac{\text{market\_size}}{\text{max\_price}} \)

#### Begründung der Parameterwahl
- **`marginal_cost = 10`**: Typische Produktionskosten, ausreichend Spielraum für Preisanpassungen.
- **`market_size = 1000`**: Repräsentative Marktgröße für Simulationen.
- **`max_price = 50`**: Realistische Preis-Kosten-Spanne, entspricht \(5 \times \text{marginal\_cost}\).
- **`price_sensitivity = 2.0`**: Realistische Elastizitätsschätzung.

### Zeitliche Notation

Die Dynamik der Preise wird wie folgt beschrieben:

\[
p_1(t+1) = \begin{cases} 
\max(c, p_2(t) \cdot (1 - \delta(t))), & \text{wenn } p_1(t) > p_2(t) \\
p_1(t), & \text{sonst}
\end{cases}
\]

Mit \( \delta(t) \sim U(0, \text{max\_underbid}) \).

### Nachfragefunktion

#### Grundnachfrage
\[
Q(p, t) = \max(0, \text{market\_size} \cdot \left(1 - \frac{p}{\text{max\_price}}\right))
\]

#### Effektive Nachfrage
Die Nachfrage eines Unternehmens \(i\) in Periode \(t\):

\[
Q_i(p_i, p_j, t) = Q(p_i, t) \cdot s_i(t)
\]

### Präzisierung der Übergangsbegriffe

- **Granulare Preisanpassung**:
  - Schrittweise Änderungen (max. 8% pro Periode)
  - Diskrete Zeitschritte
- **Differenzierbare Marktanteilsfunktion**:
  - Logistische Funktion mit stetiger erster Ableitung
  - Stetige Übergänge
- **Approximative Nash-Dynamik**:
  - Diskrete Zeitentwicklung, Annäherung an das Nash-Gleichgewicht.

### Mathematische Einschränkungen

- **Diskrete Zeitschritte**: \( t \in \{0, 1, \ldots, T-1\} \).
- **Endliche Preisänderungen**: \( \Delta p_i(t) \leq \text{max\_underbid} \cdot p_i(t) \).
- **Begrenzte Wertebereiche**:
  - \( p_i(t) \in [c, \text{max\_price}] \).
  - \( s_i(t) \in [0, 1] \).
  - \( Q_i(t) \in [0, \text{market\_size}] \).

## 📊 Unterschiede zum klassischen Bertrand-Modell

### Klassisches Modell
- **Binäre Marktaufteilung** (Winner-takes-all).
- **Sofortige Preisanpassung**.
- Nash-Gleichgewicht bei Grenzkosten.
- Keine explizite Zeitdimension.

### Dynamisches Modell
- **Kontinuierliche Marktaufteilung** durch logistische Funktion.
- **Graduelle Preisanpassung** (max. 8% pro Periode).
- **Realistische Marktdynamik**.
- Explizite zeitliche Modellierung.

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.

## 👥 Beitragen

Beiträge sind willkommen! Bitte lesen Sie [CONTRIBUTING.md](CONTRIBUTING.md) für Details zum Prozess für Pull Requests.

## ✉️ Kontakt

Leon de Vries - (leondevries.de) - mail@leondevries.de

Projekt Link: [https://github.com/LeonVries/basic](https://github.com/LeonVries/basic)
