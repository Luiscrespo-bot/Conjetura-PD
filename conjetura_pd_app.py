import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
from itertools import permutations

# Generar permutaciones válidas
def permutaciones_validas(n):
    str_n = str(n)
    perm_set = set()
    for p in permutations(str_n):
        if p[0] != '0':
            perm = int(''.join(p))
            if perm != n:
                perm_set.add(perm)
    return sorted(perm_set)

# Crear el grafo
def construir_grafo_pd(inicial, pasos=3):
    G = nx.DiGraph()
    actual = inicial

    for _ in range(pasos):
        duplicado = 2 * actual
        perms = permutaciones_validas(actual)
        G.add_node(actual, label=str(actual), tipo='base')
        G.add_node(duplicado, label=str(duplicado), tipo='duplicado')
        G.add_edge(actual, duplicado, tipo='duplicacion')

        for p in perms:
            G.add_node(p, label=str(p), tipo='perm')
            G.add_edge(actual, p, tipo='perm')

        actual = duplicado

    return G

# Dibujar grafo
def dibujar_grafo(G):
    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots(figsize=(12, 8))

    nodos_base = [n for n, attr in G.nodes(data=True) if attr['tipo'] == 'base']
    nodos_duplicado = [n for n, attr in G.nodes(data=True) if attr['tipo'] == 'duplicado']
    nodos_perm = [n for n, attr in G.nodes(data=True) if attr['tipo'] == 'perm']

    nx.draw_networkx_nodes(G, pos, nodelist=nodos_base, node_color='skyblue', node_size=800, label='Base')
    nx.draw_networkx_nodes(G, pos, nodelist=nodos_duplicado, node_color='lightgreen', node_size=800, label='Duplicado')
    nx.draw_networkx_nodes(G, pos, nodelist=nodos_perm, node_color='lightcoral', node_size=300, label='Permutaciones')

    edges_perm = [(u, v) for u, v, d in G.edges(data=True) if d['tipo'] == 'perm']
    edges_dupl = [(u, v) for u, v, d in G.edges(data=True) if d['tipo'] == 'duplicacion']

    nx.draw_networkx_edges(G, pos, edgelist=edges_perm, edge_color='red', style='dotted')
    nx.draw_networkx_edges(G, pos, edgelist=edges_dupl, edge_color='green', width=2)

    labels = {n: G.nodes[n]['label'] for n in G.nodes}
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold')

    ax.set_title("Visualización de la Conjetura PD", fontsize=16)
    ax.axis('off')
    return fig

# Streamlit UI
st.title("🔢 Conjetura PD (Permutación-Duplicación)")
st.markdown("Explora cómo los números se reflejan en sus propias permutaciones mientras se duplican.")

inicial = st.number_input("Número inicial (mínimo 2 dígitos):", min_value=10, value=128)
pasos = st.slider("Pasos de duplicación:", min_value=1, max_value=5, value=3)

if st.button("Generar grafo"):
    with st.spinner("Construyendo..."):
        G = construir_grafo_pd(inicial, pasos)
        fig = dibujar_grafo(G)
        st.pyplot(fig)

    st.success("¡Grafo generado!")