# Vergleich: Klassisches Bertrand-Modell vs. Dynamisches Modell

## 1. Nachfragefunktion

### Klassisches Bertrand-Modell

- **Lineare Nachfragefunktion**: \( Q(p) = a - bp \)
- Verhalten:
  - Bei \( p₁ < p₂ \): Firma 1 erhält die gesamte Nachfrage.
  - Bei \( p₁ = p₂ \): Nachfrage wird gleichmäßig aufgeteilt (50/50).
  - Bei \( p₁ > p₂ \): Firma 1 erhält keine Nachfrage.
- Mathematisch ausgedrückt:

  \[
  Q₁(p₁, p₂) = 
  \begin{cases} 
  a - bp₁, & \text{wenn } p₁ < p₂ \\
  \frac{a - bp₁}{2}, & \text{wenn } p₁ = p₂ \\
  0, & \text{wenn } p₁ > p₂
  \end{cases}
  \]

### Unser dynamisches Modell

- **Grundnachfrage**: \( Q(p) = \text{market\_size} \cdot (1 - \frac{p}{\text{max\_price}}) \)
- **Logistische Marktaufteilung basierend auf Preisdifferenzen**:

  \[
  \text{market\_share}(p₁, p₂) = \frac{1}{1 + e^{-\text{sensitivity} \cdot \frac{p₂ - p₁}{\frac{p₁ + p₂}{2}}}}
  \]

- Gesamtfunktion:

  \[
  Q₁(p₁, p₂) = Q(p₁) \cdot \text{market\_share}(p₁, p₂)
  \]

---

## 2. Gewinnfunktion

### Klassisches Bertrand-Modell

\[
\pi₁(p₁, p₂) = 
\begin{cases} 
(p₁ - c) \cdot (a - bp₁), & \text{wenn } p₁ < p₂ \\
(p₁ - c) \cdot \frac{a - bp₁}{2}, & \text{wenn } p₁ = p₂ \\
0, & \text{wenn } p₁ > p₂
\end{cases}
\]

- \( c \): Grenzkosten.

### Unser dynamisches Modell

\[
\pi₁(p₁, p₂) = (p₁ - c) \cdot \text{market\_size} \cdot \left(1 - \frac{p₁}{\text{max\_price}}\right) \cdot \text{market\_share}(p₁, p₂)
\]

---

## 3. Preisanpassungsmechanismus

### Klassisches Bertrand-Modell

- **Verhalten**:
  - Sofortige Anpassung zum Nash-Gleichgewicht.
  - Nash-Gleichgewicht bei \( p₁ = p₂ = c \).
  - Keine explizite Zeitdynamik.

### Unser dynamisches Modell

- **Graduelle Preisanpassung** mit maximaler Änderungsrate von 8% pro Periode.
- Preisanpassungsregel:

  \[
  p₁(t+1) = 
  \begin{cases} 
  \max(c, p₂(t) \cdot (1 - \text{random}(0, 0.08))), & \text{wenn } p₁(t) > p₂(t) \\
  p₁(t), & \text{sonst}
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

- Eindeutiges Nash-Gleichgewicht bei \( p₁ = p₂ = c \).
- Sofortige Konvergenz.
- **"Bertrand-Paradox"**: Null-Gewinn im Gleichgewicht.

### Unser dynamisches Modell

- Gleiches Nash-Gleichgewicht bei \( p₁ = p₂ = c \).
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
\text{price\_diff} = \frac{p₂ - p₁}{\frac{p₁ + p₂}{2}}
\]

- Berücksichtigt relative statt absolute Preisunterschiede.
- Realistischere Abbildung der Konsumentenwahrnehmung.
