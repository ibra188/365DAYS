import pandas as pd  # Importa pandas

# Dizionario dei dati
teacher_dict = {
    "name": "Mr. Smith",
    "age": 35,
    "salary": 50000,
    "courses": "Math,Science,History,English",  # Convertiamo la lista in stringa
    "phone": "555-555-5555",
}

# Creiamo un DataFrame da un dizionario
df = pd.DataFrame([teacher_dict])  # La lista con un solo dizionario

# Salviamo il DataFrame in un CSV
df.to_csv("teacher.csv", index=False)  # Senza colonna degli indici

# Leggiamo il file CSV
df_new = pd.read_csv("teacher.csv")
print(df_new)
