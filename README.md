
# 🔢 Conjetura PD (Permutación–Duplicación)

**Autor:** Luis Fernando Crespo Soliz  
**Fecha de inicio:** 2025  

## 📖 Descripción

La **Conjetura PD (Permutación–Duplicación)** es una exploración matemática basada en la siguiente idea:

> Para ciertos números naturales `n`, existen permutaciones distintas de sus cifras que, al restarse de `n`, reflejan una estructura interna repetible, mientras `n` se duplica sucesivamente y el patrón continúa.

Por ejemplo:  
128 = 128 - 182 - 218 - 281 - 812 - 821  
128 + 128 = 256

El fenómeno se repite para:  
256 → 512 → 1024 → 2048 → ...

La herramienta en este repositorio permite visualizar este comportamiento, explorar las permutaciones válidas de cualquier número y trazar su progresión.

---

## 🚀 Demo en línea

Accede a la app sin instalar nada:  
👉 [Streamlit Web App (pendiente de despliegue)](https://streamlit.io)

---

## ⚙️ Instalación local

### Requisitos

- Python 3.8+
- pip

### Instalación

```bash
git clone https://github.com/tu_usuario/conjetura-pd-app.git
cd conjetura-pd-app
pip install -r requirements.txt
streamlit run conjetura_pd_app.py
```

---

## 🧠 ¿Qué hace esta herramienta?

- Calcula las permutaciones válidas de un número (sin ceros iniciales).
- Visualiza la duplicación como transición dirigida.
- Dibuja un grafo con los números, sus permutaciones y duplicados.
- Explora paso a paso la evolución de la conjetura.

---

## 📈 Ejemplo visual

Para n = 128 con 4 pasos de duplicación:

```
128 → 256 → 512 → 1024
│     │     │      └─→ Permutaciones de 1024: ...
├─→ Permutaciones de 128: [182, 218, 281, 812, 821]
...
```

La app representa estos pasos mediante un grafo interactivo.

---

## 🧮 Fundamento matemático (en desarrollo)

Dado un número n, definimos:

P(n) = conjunto de permutaciones de sus cifras (excluyendo n)

La conjetura es:  
Existe un subconjunto de P(n) tal que  
n = n - Σ(Pi)  
y el mismo patrón continúa para 2n.

Se propone que esta propiedad puede formar una secuencia infinita de duplicaciones.

---

## 🧩 Contribuciones

Este proyecto está abierto a:

- Mejoras del código o interfaz web.
- Verificación y formalización matemática.
- Inclusión en OEIS (On-Line Encyclopedia of Integer Sequences).
- Visualizaciones alternativas (redes, árboles, animaciones).
- Discusión académica o divulgativa.

---

## 🧾 Licencia

MIT License

---

## 📬 Contacto

Luis Fernando Crespo Soliz  
📧 lfcrespos@gmail.com
