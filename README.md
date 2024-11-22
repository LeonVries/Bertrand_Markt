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
