import streamlit as st
import networkx as nx
from itertools import permutations
import plotly.graph_objects as go

# Lista de nodos base por duplicación (potencias de 2)
nodos_base = [1 << i for i in range(17)]

# Colores personalizados para cada nodo
colores_personalizados = {
    1: "#00ccff", 2: "#00e6cc", 4: "#00ffff", 8: "#009999",
    16: "#8000ff", 32: "#6600cc", 64: "#cc00cc", 128: "#ff66cc",
    256: "#ff6666", 512: "#ff0000", 1024: "#ff3333", 2048: "#ffffff",
    4096: "#cccccc", 8192: "#999999", 16384: "#666666",
    32768: "#444444", 65536: "#000000"
}

# Funcion para obtener permutaciones válidas de un número
def obtener_permutaciones(n):
    str_n = str(n)
    return sorted(
        set(
            int(''.join(p)) for p in permutations(str_n)
            if p[0] != '0' and int(''.join(p)) != n
        )
    )

# Mostrar controles
st.set_page_config(layout="wide")
st.title("Grafo Interactivo de Duplicación y Permutaciones hasta 65,536")

mostrar_permutaciones = st.checkbox("Mostrar permutaciones", value=True)

nodo_filtro = st.multiselect(
    "Excluir permutaciones de los siguientes nodos:",
    options=[n for n in nodos_base[3:]],
    default=[]
)

# Crear grafo dirigido
G = nx.DiGraph()

# Agregar nodos base y duplicaciones
for i in range(len(nodos_base) - 1):
    n = nodos_base[i]
    dup = nodos_base[i + 1]
    G.add_node(n, color=colores_personalizados[n])
    G.add_node(dup, color=colores_personalizados[dup])
    G.add_edge(n, dup)

# Agregar permutaciones si están activadas y no excluidas
if mostrar_permutaciones:
    for n in nodos_base[3:]:  # desde 8 en adelante
        if n in nodo_filtro:
            continue
        for p in obtener_permutaciones(n):
            if p not in G:
                G.add_node(p, color="#dddddd")
            G.add_edge(n, p)

# Obtener posiciones con spring layout
pos = nx.spring_layout(G, seed=42, k=0.5)

# Convertir a formato para Plotly
edge_x, edge_y = [], []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none', mode='lines')

node_x, node_y, node_text, node_color = [], [], [], []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(str(node))
    node_color.append(G.nodes[node].get('color', '#dddddd'))

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=node_text, textposition='top center',
    hoverinfo='text',
    marker=dict(
        showscale=False,
        color=node_color,
        size=20,
        line_width=2))

# Mostrar grafo
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20, l=5, r=5, t=40),
                    xaxis=dict(showgrid=False, zeroline=False),
                    yaxis=dict(showgrid=False, zeroline=False),
                    height=800,
                    dragmode='pan'
                ))

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
**Controles:**
- 🔍 Usa la **rueda del ratón** o las herramientas de zoom de Plotly.
- 🔄 Usa `Ctrl + R` para refrescar el navegador si deseas reiniciar el grafo.
""")
