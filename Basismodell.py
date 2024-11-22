import numpy as np
import matplotlib.pyplot as plt

# Parameter
alpha1 = 100
alpha2 = 100
beta1 = 10
beta2 = 10
gamma12 = 5
gamma21 = 5
c1 = 20
c2 = 20

# Reaktionsfunktionen
def reaction_function_1(p2):
    return (alpha1 + beta1 * c1 + gamma12 * p2) / (2 * beta1)

def reaction_function_2(p1):
    return (alpha2 + beta2 * c2 + gamma21 * p1) / (2 * beta2)

# Berechnung des Nash-Gleichgewichts
A = np.array([[1, -gamma12 / (2 * beta1)],
              [-gamma21 / (2 * beta2), 1]])
b = np.array([(alpha1 + beta1 * c1) / (2 * beta1),
              (alpha2 + beta2 * c2) / (2 * beta2)])

p_star = np.linalg.solve(A, b)
p1_star, p2_star = p_star

print(f"Nash-Gleichgewicht:")
print(f"p1* = {p1_star:.2f}")
print(f"p2* = {p2_star:.2f}")

# Preisbereich
p_range = np.linspace(0, 50, 500)

# Reaktionskurven berechnen
p1_values = reaction_function_1(p_range)
p2_values = reaction_function_2(p_range)

# Plotten der Reaktionsfunktionen
plt.figure(figsize=(10, 6))

plt.plot(p_range, p1_values, label='Reaktionsfunktion von Unternehmen 1', color='blue')
plt.plot(p2_values, p_range, label='Reaktionsfunktion von Unternehmen 2', color='red')

# Nash-Gleichgewichtspunkt
plt.plot(p1_star, p2_star, 'go', label='Nash-Gleichgewicht')

# Begrenzung des Diagramms
plt.xlim(0, 50)
plt.ylim(0, 50)

# Achsenbeschriftungen und Titel
plt.xlabel('Preis von Unternehmen 1, p1')
plt.ylabel('Preis von Unternehmen 2, p2')
plt.title('Reaktionsfunktionen im Bertrand-Modell mit Nash-Gleichgewicht')
plt.legend()
plt.grid(True)
plt.show()
