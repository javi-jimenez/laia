A continuación, te proporcionaré ejemplos de cómo crear **diagramas de Gantt** en diferentes lenguajes de programación. Estos diagramas son útiles para visualizar el **roadmap** del proyecto **Laia** que hemos discutido. Utilizaré bibliotecas populares en cada lenguaje para generar los diagramas.

---

### **1. Python (con Matplotlib y Plotly)**

#### **Código con Matplotlib**
```python
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
```

#### **Código con Plotly (más interactivo)**
```python
import plotly.express as px
import pandas as pd

# Datos del proyecto
data = {
    "Task": ["Preparación", "Desarrollo Inicial", "Expansión y Validación", "Consolidación", "Liderazgo Global"],
    "Start": ["2023-10-01", "2024-01-01", "2025-07-01", "2027-07-01", "2030-07-01"],
    "Finish": ["2023-12-31", "2025-06-30", "2027-06-30", "2030-06-30", "2035-12-31"],
}

df = pd.DataFrame(data)

# Crear el diagrama de Gantt
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", title="Roadmap del Proyecto Laia")
fig.update_yaxes(autorange="reversed")  # Invertir el eje Y para que la primera tarea esté arriba
fig.show()
```

---

### **2. JavaScript (con Chart.js)**

#### **Código en JavaScript**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Diagrama de Gantt - Proyecto Laia</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
</head>
<body>
    <canvas id="ganttChart" width="800" height="400"></canvas>
    <script>
        const tasks = [
            { task: "Preparación", start: "2023-10-01", end: "2023-12-31" },
            { task: "Desarrollo Inicial", start: "2024-01-01", end: "2025-06-30" },
            { task: "Expansión y Validación", start: "2025-07-01", end: "2027-06-30" },
            { task: "Consolidación", start: "2027-07-01", end: "2030-06-30" },
            { task: "Liderazgo Global", start: "2030-07-01", end: "2035-12-31" },
        ];

        const ctx = document.getElementById('ganttChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                datasets: tasks.map((t, i) => ({
                    label: t.task,
                    data: [{
                        x: [t.start, t.end],
                        y: i
                    }],
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                }))
            },
            options: {
                indexAxis: 'y',
                scales: {
                    x: {
                        type: 'time',
                        time: {
                            unit: 'year'
                        }
                    },
                    y: {
                        ticks: {
                            callback: (value, index) => tasks[index].task
                        }
                    }
                }
            }
        });
    </script>
</body>
</html>
```

---

### **3. R (con ggplot2)**

#### **Código en R**
```R
library(ggplot2)
library(scales)

# Datos del proyecto
tasks <- data.frame(
    Task = c("Preparación", "Desarrollo Inicial", "Expansión y Validación", "Consolidación", "Liderazgo Global"),
    Start = as.Date(c("2023-10-01", "2024-01-01", "2025-07-01", "2027-07-01", "2030-07-01")),
    End = as.Date(c("2023-12-31", "2025-06-30", "2027-06-30", "2030-06-30", "2035-12-31"))
)

# Crear el diagrama de Gantt
ggplot(tasks, aes(x = Start, xend = End, y = Task, yend = Task, color = Task)) +
    geom_segment(size = 10) +
    scale_x_date(labels = date_format("%Y-%m-%d")) +
    labs(title = "Roadmap del Proyecto Laia", x = "Fecha", y = "Fases del Proyecto") +
    theme_minimal()
```

---

### **4. Excel (con Gráficos de Barras)**

#### **Pasos en Excel**
1. Abre Excel y crea una tabla con las siguientes columnas:
   - **Task**: Nombre de la tarea.
   - **Start**: Fecha de inicio.
   - **End**: Fecha de fin.
   - **Duration**: Duración en días (calculada como `End - Start`).

2. Selecciona los datos y ve a **Insertar > Gráfico de Barras > Barra Apilada**.

3. Formatea el eje horizontal para mostrar fechas:
   - Haz clic derecho en el eje horizontal > **Formato de Eje**.
   - En **Opciones de Eje**, selecciona "Escala de Tiempo".

4. Personaliza el gráfico con títulos y colores.

---

### **5. Google Sheets (con Gráficos de Barras)**

#### **Pasos en Google Sheets**
1. Abre Google Sheets y crea una tabla con las mismas columnas que en Excel.

2. Selecciona los datos y ve a **Insertar > Gráfico**.

3. En la pestaña **Configuración**, selecciona "Gráfico de Barras".

4. En la pestaña **Personalizar**, ajusta el eje horizontal para mostrar fechas.

---

### **Conclusión**

Estos ejemplos te permiten crear **diagramas de Gantt** en diferentes lenguajes y herramientas. Puedes elegir el que mejor se adapte a tus necesidades o entorno de trabajo.
