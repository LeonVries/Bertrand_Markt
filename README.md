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

### Nachfragefunktion
```
Q(p) = market_size * (1 - p/max_price)
```

### Marktanteil
```
market_share(p₁, p₂) = 1 / (1 + e^(-sensitivity * (p₂ - p₁)/((p₁ + p₂)/2)))
```

### Gewinnfunktion
```
π₁(p₁, p₂) = (p₁ - c) * Q(p₁) * market_share(p₁, p₂)
```

### Preisanpassung
```
p₁(t+1) = max(c, p₂(t) * (1 - random(0, 0.08))), wenn p₁(t) > p₂(t)
p₁(t+1) = p₁(t), sonst
```

## 📊 Unterschiede zum klassischen Bertrand-Modell

### Klassisches Modell
- Binäre Marktaufteilung (Winner-takes-all)
- Sofortige Preisanpassung
- Nash-Gleichgewicht bei Grenzkosten
- Keine explizite Zeitdimension

### Unser dynamisches Modell
- Kontinuierliche Marktaufteilung durch logistische Funktion
- Graduelle Preisanpassung (max. 8% pro Periode)
- Realistische Marktdynamik
- Explizite Modellierung der zeitlichen Entwicklung

### Hauptinnovationen
1. **Logistische Marktanteilsfunktion**
   - Stetige Übergänge
   - Parametrisierbare Preissensitivität
   - Realistische Nachfrageverteilung

2. **Gedämpfte Preisanpassung**
   - Verhindert unrealistische Preissprünge
   - Modelliert Marktträgheit

3. **Relative Preisdifferenzen**
   - Berücksichtigt relative statt absolute Preisunterschiede
   - Realistische Konsumentenwahrnehmung

## 📈 Beispiel-Output

Das Modell erzeugt drei Grafiken:
1. Preisentwicklung beider Unternehmen
2. Gewinnentwicklung im Zeitverlauf
3. Marktanteilsentwicklung

## 🔬 Parameter

| Parameter | Beschreibung | Standardwert |
|-----------|--------------|--------------|
| `marginal_cost` | Grenzkosten der Produktion | - |
| `market_size` | Maximale Marktnachfrage | - |
| `max_price` | Maximaler Preis | - |
| `max_underbid` | Maximale Preissenkung pro Periode | 0.08 |
| `price_sensitivity` | Preissensitivität der Kunden | 2.0 |

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.

## 👥 Beitragen

Beiträge sind willkommen! Bitte lesen Sie [CONTRIBUTING.md](CONTRIBUTING.md) für Details zum Prozess für Pull Requests.

## ✉️ Kontakt

Leon de Vries - (leondevries.de) - mail@leondevries.de

Projekt Link: [https://github.com/LeonVries/basic](https://github.com/LeonVries/basic)



# Vergleich: Klassisches Bertrand-Modell vs. Dynamisches Modell

## 1. Nachfragefunktion

### Klassisches Bertrand-Modell

- **Lineare Nachfragefunktion**: \( Q(p) = a - b \cdot p \)
- Verhalten:
  - Bei \( p_1 < p_2 \): Firma 1 erhält die gesamte Nachfrage.
  - Bei \( p_1 = p_2 \): Nachfrage wird gleichmäßig aufgeteilt (50/50).
  - Bei \( p_1 > p_2 \): Firma 1 erhält keine Nachfrage.
- Mathematisch ausgedrückt:

  \[
  Q_1(p_1, p_2) = 
  \begin{cases} 
  a - b \cdot p_1, & \text{wenn } p_1 < p_2 \\
  \frac{a - b \cdot p_1}{2}, & \text{wenn } p_1 = p_2 \\
  0, & \text{wenn } p_1 > p_2
  \end{cases}
  \]

### Unser dynamisches Modell

- **Grundnachfrage**: 

  \[
  Q(p) = \text{market\_size} \cdot \left(1 - \frac{p}{\text{max\_price}}\right)
  \]

- **Logistische Marktaufteilung basierend auf Preisdifferenzen**:

  \[
  \text{market\_share}(p_1, p_2) = \frac{1}{1 + e^{-\text{sensitivity} \cdot \frac{p_2 - p_1}{\frac{p_1 + p_2}{2}}}}
  \]

- Gesamtfunktion:

  \[
  Q_1(p_1, p_2) = Q(p_1) \cdot \text{market\_share}(p_1, p_2)
  \]

---

## 2. Gewinnfunktion

### Klassisches Bertrand-Modell

\[
\pi_1(p_1, p_2) = 
\begin{cases} 
(p_1 - c) \cdot (a - b \cdot p_1), & \text{wenn } p_1 < p_2 \\
(p_1 - c) \cdot \frac{a - b \cdot p_1}{2}, & \text{wenn } p_1 = p_2 \\
0, & \text{wenn } p_1 > p_2
\end{cases}
\]

- \( c \): Grenzkosten.

### Unser dynamisches Modell

\[
\pi_1(p_1, p_2) = (p_1 - c) \cdot \text{market\_size} \cdot \left(1 - \frac{p_1}{\text{max\_price}}\right) \cdot \text{market\_share}(p_1, p_2)
\]

---

## 3. Preisanpassungsmechanismus

### Klassisches Bertrand-Modell

- **Verhalten**:
  - Sofortige Anpassung zum Nash-Gleichgewicht.
  - Nash-Gleichgewicht bei \( p_1 = p_2 = c \).
  - Keine explizite Zeitdynamik.

### Unser dynamisches Modell

- **Graduelle Preisanpassung** mit maximaler Änderungsrate von 8% pro Periode.
- Preisanpassungsregel:

  \[
  p_1(t+1) = 
  \begin{cases} 
  \max(c, p_2(t) \cdot (1 - \text{random}(0, 0.08))), & \text{wenn } p_1(t) > p_2(t) \\
  p_1(t), & \text{sonst}
  \end{cases}
  \]

---

## 4. Hauptunterschiede und Erweiterungen

- **Marktaufteilung**:
  - Klassisch: Diskrete "Winner-takes-all"-Struktur.
  - Dynamisch: Kontinuierliche Marktaufteilung durch logistische Funktion.

- **Zeitliche Dimension**:
  - Klassisch: Statisches Gleichgewicht.
  - Dynamisch: Explizite Modellierung der Anpassungsdynamik.

- **Preisanpassung**:
  - Klassisch: Instantan.
  - Dynamisch: Graduell mit Maximalrate.

- **Nachfrageverteilung**:
  - Klassisch: Binär (alles oder nichts).
  - Dynamisch: Kontinuierlich basierend auf relativem Preisunterschied.

---

## 5. Nash-Gleichgewicht

### Klassisches Bertrand-Modell

- Eindeutiges Nash-Gleichgewicht bei \( p_1 = p_2 = c \).
- Sofortige Konvergenz.
- **"Bertrand-Paradox"**: Null-Gewinn im Gleichgewicht.

### Unser dynamisches Modell

- Gleiches Nash-Gleichgewicht bei \( p_1 = p_2 = c \).
- Graduelle Konvergenz zum Gleichgewicht.
- Positive Gewinne während des Anpassungsprozesses.
- Realistischere Abbildung der Marktdynamik.

---

## 6. Mathematische Innovationen unseres Modells

### Logistische Marktanteilsfunktion:

\[
\text{market\_share} = \frac{1}{1 + e^{-\text{sensitivity} \cdot \text{price\_diff}}}
\]

- Ermöglicht stetige Übergänge.
- Parametrisierbare Preissensitivität.
- Vermeidet unrealistische Sprünge in der Nachfrage.

### Gedämpfte Preisanpassung:

\[
\text{new\_price} = \max(c, \text{old\_price} \cdot (1 - \text{random}(0, \text{max\_adjustment})))
\]

- Verhindert unrealistische Preissprünge.
- Modelliert Trägheit im Markt.

### Relative Preisdifferenzen:

\[
\text{price\_diff} = \frac{p_2 - p_1}{\frac{p_1 + p_2}{2}}
\]

- Berücksichtigt relative statt absolute Preisunterschiede.
- Realistischere Abbildung der Konsumentenwahrnehmung.
