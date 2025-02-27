import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Datos del proyecto
tasks = [
    {"name": "Preparación", "start": "2023-10-01", "end": "2023-12-31"},
    {"name": "Desarrollo Inicial", "start": "2024-01-01", "end": "2025-06-30"},
    {"name": "Expansión y Validación", "start": "2025-07-01", "end": "2027-06-30"},
    {"name": "Consolidación", "start": "2027-07-01", "end": "2030-06-30"},
    {"name": "Liderazgo Global", "start": "2030-07-01", "end": "2035-12-31"},
]

# Convertir fechas a formato datetime
for task in tasks:
    task["start"] = datetime.strptime(task["start"], "%Y-%m-%d")
    task["end"] = datetime.strptime(task["end"], "%Y-%m-%d")

# Crear el diagrama de Gantt
fig, ax = plt.subplots(figsize=(10, 6))

for i, task in enumerate(tasks):
    ax.barh(task["name"], (task["end"] - task["start"]).days, left=task["start"], color="skyblue")

# Formatear el eje de fechas
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.xticks(rotation=45)
plt.xlabel("Fecha")
plt.ylabel("Fases del Proyecto")
plt.title("Roadmap del Proyecto Laia")
plt.grid(True)
plt.tight_layout()
plt.show()
