# Import der notwendigen Bibliotheken
import streamlit as st
import math

# 1. Titel: Gib der App eine Überschrift.
# st.title() wird verwendet, um den Haupttitel der Anwendung anzuzeigen.
st.title("Schnittdaten-Rechner für Drehen")

# 2. Eingabefelder: Erstelle Felder für die Benutzereingaben.
# st.number_input() erstellt ein Feld, das nur numerische Eingaben akzeptiert.
# 'label' ist der Text, der über dem Eingabefeld angezeigt wird.
# 'min_value' stellt sicher, dass keine negativen Werte oder Null eingegeben werden,
# was zu Fehlern bei der Berechnung führen würde.
# 'value' setzt einen Standardwert.
# 'step' definiert die Schrittweite, wenn auf die kleinen Pfeile geklickt wird.
vc = st.number_input("Schnittgeschwindigkeit vc (in m/min)", min_value=1.0, value=120.0, step=10.0)
d = st.number_input("Durchmesser d (in mm)", min_value=1.0, value=50.0, step=1.0)

# 3. Knopf: Füge einen Knopf hinzu, um die Berechnung auszulösen.
# st.button() erstellt einen klickbaren Knopf. Die Funktion gibt 'True' zurück,
# wenn der Knopf gedrückt wird, andernfalls 'False'.
if st.button("Drehzahl berechnen"):
    # 4. Logik: Führe die Berechnung durch, wenn der Knopf gedrückt wird.
    # Die Formel zur Berechnung der Drehzahl n.
    # vc muss mit 1000 multipliziert werden, um von m in mm umzurechnen,
    # damit die Einheiten mit dem Durchmesser d (in mm) übereinstimmen.
    # math.pi wird für die Konstante Pi (π) verwendet.
    n = (vc * 1000) / (d * math.pi)

    # Runde das Ergebnis auf die nächste ganze Zahl.
    n_gerundet = round(n)

    # 5. Ausgabe: Zeige das Ergebnis in einer grünen Erfolgs-Box an.
    # st.success() zeigt eine Nachricht in einer grünen Box an,
    # ideal für Erfolgsmeldungen.
    # f-String wird verwendet, um das Ergebnis direkt in den Text einzufügen.
    st.success(f"Die berechnete Drehzahl beträgt: {n_gerundet} U/min")

# Optional: Ein kleiner Hinweis zur Formel am Ende der Seite.
st.markdown("---")
st.write("Verwendete Formel: `n = (vc * 1000) / (d * π)`")
