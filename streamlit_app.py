import streamlit as st
import requests
import pandas as pd
import altair as alt

# Configuración inicial de la página
st.set_page_config(page_title="Lumière", page_icon="📚", layout="wide")

# --- SISTEMA DE ESTADO DE SESIÓN (Memoria del navegador) ---
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'is_premium' not in st.session_state:
    st.session_state.is_premium = False
if 'discount_code' not in st.session_state:
    st.session_state.discount_code = ""

# --- LLAMADA AL BACKEND O DATOS LOCALES ---
@st.cache_data(ttl=60) # Caché para no hacer demasiadas peticiones
def load_books():
    try:
        response = requests.get("http://127.0.0.1:8080/api/books")
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return []

books_data = load_books()

# --- MENÚ LATERAL Y NAVEGACIÓN ---
with st.sidebar:
    st.title("📚 Lumière")
    if st.session_state.is_premium:
        st.success("👑 Socio Premium Activo")
    
    st.subheader("Navegación")
    page = st.radio("Ir a:", ["Catálogo y Filtros", "Mi Cesta 🛒", "Mis Favoritos ❤️", "Estadísticas 📊", "Hazte Socio / Social"])
    
    st.divider()
    st.write("🌐 Redes Sociales")
    st.markdown("[Síguenos en Instagram](#)")
    st.markdown("[Nuestra Comunidad 𝕏](#)")
    st.markdown("*Refiere a un amigo y gana 5€*")

# --- FUNCIONES DE AYUDA ---
def get_book_by_id(book_id):
    for b in books_data:
        if b['id'] == book_id:
            return b
    return None

def render_book_card(book):
    # Calcular precio final
    price = book['price']
    is_free = price == 0
    if st.session_state.is_premium and book.get('isPremium', False):
        price = 0 # Gratis para premium
        is_free = True
    elif st.session_state.is_premium and price > 0:
        price = round(price * 0.8, 2) # 20% descuento a socios
    
    with st.container(border=True):
        st.subheader(book['title'])
        st.write(f"**Autor:** {book['author']} | **⭐:** {book['rating']}")
        
        # Etiqueta de precio
        if is_free:
            st.success("GRATIS")
        else:
            if st.session_state.is_premium:
                st.info(f"Precio Socio: ${price} (Antes ${book['price']})")
            else:
                st.warning(f"Precio: ${price}")

        # Acordeón de vista previa
        with st.expander("👁️ Vista Previa del libro"):
            st.write(f"**Categoría:** {book['category'].title().replace('_', ' ')}")
            st.write(f"**Páginas:** {book['pages']} | **Duración Audolibro:** {book['duration']}")
            st.write(f"*{book['desc']}*")
        
        # Botones de Acción
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🛒 Añadir a Cesta", key=f"cart_{book['id']}"):
                item = {"id": book['id'], "title": book['title'], "price": price}
                st.session_state.cart.append(item)
                st.toast(f"Añadido: {book['title']}")
        with col2:
            is_fav = book['id'] in st.session_state.favorites
            fav_text = "❤️ Quitar Favorito" if is_fav else "🤍 Hacer Favorito"
            if st.button(fav_text, key=f"fav_{book['id']}"):
                if is_fav:
                    st.session_state.favorites.remove(book['id'])
                else:
                    st.session_state.favorites.append(book['id'])
                st.rerun() # Recarga para actualizar botón

# --- PANTALLA: CATÁLOGO ---
if page == "Catálogo y Filtros":
    st.title("Explorar la Biblioteca")
    
    if not books_data:
        st.error("Error conectando con el servidor. ¿Está el backend encendido (`uvicorn main:app --port 8080`)?")
        st.stop()

    # Zona de Filtros
    st.subheader("Filtros Avanzados")
    colA, colB, colC = st.columns(3)
    
    with colA:
        search_term = st.text_input("Buscar por título o autor...")
    with colB:
        cats = ["Todas"] + list(set([b["category"] for b in books_data]))
        selected_cat = st.selectbox("Categoría", cats)
    with colC:
        max_price = st.slider("Precio Máximo ($)", 0.0, 30.0, 30.0, 1.0)

    st.divider()

    # Aplicar Filtros
    filtered_books = books_data
    if search_term:
        filtered_books = [b for b in filtered_books if search_term.lower() in b['title'].lower() or search_term.lower() in b['author'].lower()]
    if selected_cat != "Todas":
        filtered_books = [b for b in filtered_books if b['category'] == selected_cat]
    
    # Filtrar por precio original (simplificación)
    filtered_books = [b for b in filtered_books if b['price'] <= max_price]

    if not filtered_books:
        st.info("No hay libros que coincidan con tus filtros.")
    else:
        # Pinta los libros en una cuadrícula de 3 columnas
        cols = st.columns(3)
        for i, book in enumerate(filtered_books):
            with cols[i % 3]:
                render_book_card(book)

# --- PANTALLA: CESTA ---                
elif page == "Mi Cesta 🛒":
    st.title("Tu Cesta de Compra")
    
    if len(st.session_state.cart) == 0:
        st.info("Tu cesta está vacía. ¡Ve al catálogo a descubrir libros!")
    else:
        st.write("Libros a adquirir:")
        total = 0.0
        
        for idx, item in enumerate(st.session_state.cart):
            col1, col2, col3 = st.columns([3, 1, 1])
            col1.write(f"📖 **{item['title']}**")
            col2.write(f"${item['price']}")
            if col3.button("❌", key=f"del_{idx}"):
                st.session_state.cart.pop(idx)
                st.rerun()
            total += item['price']
            
        st.divider()
        st.subheader(f"Total a Pagar: ${round(total, 2)}")
        
        # Simulación de pago
        if st.button("💳 Proceder al Pago", type="primary"):
            st.success("¡Pago simulado con éxito! Los libros se han añadido a tu biblioteca.")
            st.session_state.cart = [] # Vaciar cesta tras pagar
            st.balloons()

# --- PANTALLA: FAVORITOS ---
elif page == "Mis Favoritos ❤️":
    st.title("Tus Libros Guardados")
    fav_books = [get_book_by_id(fid) for fid in st.session_state.favorites if get_book_by_id(fid)]
    
    if not fav_books:
        st.info("Aún no has marcado ningún libro como favorito.")
    else:
        cols = st.columns(3)
        for i, book in enumerate(fav_books):
            with cols[i % 3]:
                render_book_card(book)

# --- PANTALLA: SOCIAL & PREMIUM ---
elif page == "Hazte Socio / Social":
    st.title("👑 Programa de Socios Lumière")
    
    st.write("### Únete a nuestro plan Premium")
    st.write("✅ 20% de descuento en **todos** los libros de pago.")
    st.write("✅ Acceso gratuito ilimitado a libros etiquetados como *Premium*.")
    st.write("✅ Sin compromiso de permanencia.")
    
    if st.session_state.is_premium:
        st.success("¡Ya eres socio! Disfruta de tus ventajas.")
        if st.button("Cancelar Suscripción"):
            st.session_state.is_premium = False
            st.rerun()
    else:
        st.info("Suscripción: $9.99 / mes")
        if st.button("🚀 Suscribirme Ahora", type="primary"):
            st.session_state.is_premium = True
            st.balloons()
            st.rerun()
            
    st.divider()
    
    st.write("### 🎁 Invita a tus amigos y gana libros")
    st.write("Comparte este código en tus redes sociales. Si un amigo se registra usándolo, ¡ambos recibís un libro gratis!")
    code = st.code("LUMIERE-FRIEND-2026", language="text")
    
    col1, col2 = st.columns(2)
    col1.button("Comparte en 𝕏")
    col2.button("Enviar por WhatsApp")

# --- PANTALLA: ESTADÍSTICAS (GRÁFICOS) ---
elif page == "Estadísticas 📊":
    st.title("📊 Dashboard y Estadísticas")
    st.write("Una visualización de los datos actuales de la biblioteca usando `pandas` y `altair`.")
    
    if books_data:
        df = pd.DataFrame(books_data)
        
        # 1. Gráfica: Distribución por categoría
        st.subheader("Libros por Categoría")
        cat_counts = df['category'].value_counts().reset_index()
        cat_counts.columns = ['Categoría', 'Cantidad']
        
        chart_cat = alt.Chart(cat_counts).mark_arc(innerRadius=50).encode(
            theta='Cantidad',
            color='Categoría',
            tooltip=['Categoría', 'Cantidad']
        ).interactive()
        st.altair_chart(chart_cat, use_container_width=True)
        
        # 2. Gráfica: Puntuaciones vs Precios
        st.subheader("Relación entre Puntuación (Estrellas) y Precio")
        chart_scatter = alt.Chart(df).mark_circle(size=200).encode(
            x=alt.X('rating', scale=alt.Scale(domain=[4.0, 5.0]), title='Puntuación ⭐'),
            y=alt.Y('price', title='Precio ($)'),
            color='category',
            tooltip=['title', 'author', 'rating', 'price']
        ).interactive()
        st.altair_chart(chart_scatter, use_container_width=True)
        
        st.caption("Nota: Posiciona el ratón sobre los puntos para ver qué libro es.")
    else:
        st.warning("No hay datos cargados para generar estadísticas.")
