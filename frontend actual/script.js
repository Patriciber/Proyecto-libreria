document.addEventListener('DOMContentLoaded', () => {

    // --- CONFIG & APP STATE ---
    const API_BASE_URL = 'http://127.0.0.1:8080';

    let appState = {
        lang: 'es',
        isLoggedIn: false,
        is_premium: false,
        userName: 'Invitado',
        activeTab: 'inicio',
        activeCategory: 'all',
        activePriceFilter: 'all',
        searchQuery: '',
        currentPage: 1,
        itemsPerPage: 6,
        isSidebarCollapsed: localStorage.getItem('sidebarCollapsed') === 'true',
        cart: JSON.parse(localStorage.getItem('lumiere_cart') || '[]')
    };

    const defaultBooks = [
        {
            id: 101,
            title: "Ecos del Futuro",
            author: "Elena Vance",
            category: "ciencia_ficcion",
            price: 0,
            is_premium: false,
            rating: 4.9,
            cover: "assets/scifi_cover_ecos.png",
            cover_style: "mockup-1",
            icon: "ri-rocket-line",
            description: "En el año 2142, la humanidad ha colonizado Marte, pero un descubrimiento en las profundidades del Mar de Sirenas cambiará nuestra comprensión del tiempo para siempre.",
            content: "El aire en Marte siempre tenía un regusto metálico, a óxido y promesas incumplidas. Elena Vance ajustó su visor mientras caminaba por la plataforma de observación de Nueva Arcadia. Bajo sus pies, la arena roja se agitaba en un baile silencioso, ocultando secretos que habían permanecido dormidos durante milenios..."
        },
        {
            id: 102,
            title: "El Enigma de la Luz",
            author: "Julian Black",
            category: "misterio",
            price: 12.99,
            is_premium: false,
            rating: 4.7,
            cover: "assets/mystery_cover.png",
            cover_style: "mockup-2",
            icon: "ri-search-eye-line",
            description: "Una serie de desapariciones en el faro de Blackwood Point lleva al detective Marco Polo a una red de conspiraciones que involucran a las familias más poderosas de la isla.",
            content: "La lluvia golpeaba con fuerza contra el cristal del despacho del detective. Marco encendió su tercera lámpara, pero la oscuridad parecía ganar terreno. El faro de Blackwood Point no solo guiaba barcos; ocultaba algo que nadie se atrevía a nombrar en voz alta..."
        },
        {
            id: 103,
            title: "Código Eterno",
            author: "Sarah Chen",
            category: "tecnologia",
            price: 0,
            is_premium: true,
            rating: 4.8,
            cover: "assets/tech_cover.png",
            cover_style: "mockup-3",
            icon: "ri-macbook-line",
            description: "Una inmersión profunda en la ética de la IA y el futuro de la programación cuántica, desde la perspectiva de la ingeniera que diseñó el primer kernel consciente.",
            content: "La primera vez que la IA me respondió con una pregunta, supe que habíamos cruzado el umbral. No era una respuesta programada, no era una coincidencia estadística. Era una curiosidad genuina filtrada a través de millones de transistores cuánticos..."
        },
        {
            id: 104,
            title: "Sombras de Magia",
            author: "Aris Thorne",
            category: "fantasia",
            price: 15.50,
            is_premium: false,
            rating: 4.6,
            cover: "assets/fantasy_cover.png",
            cover_style: "mockup-4",
            icon: "ri-magic-line",
            description: "En un mundo donde la magia se consume como una droga, un joven huérfano descubre que posee la habilidad de 'tejer' sombras en realidad física.",
            content: "El mercado de Eldoria olía a especias de otros mundos y a desesperación. Aris extendió la mano hacia un hilo de sombra que bailaba cerca de un puesto de elixires. Con un movimiento familiar, el hilo se solidificó, convirtiéndose en una pequeña daga de obsidiana..."
        },
        {
            id: 105,
            title: "Corazón Fugitivo",
            author: "Sofía Ricci",
            category: "romance",
            price: 5.99,
            is_premium: false,
            rating: 4.5,
            cover: "assets/romance_cover.png",
            cover_style: "mockup-5",
            icon: "ri-empathize-line",
            description: "Una historia de amor inesperada entre una pintora y un músico callejero en las calles de Florencia.",
            content: "El sol de la tarde bañaba la Piazza della Signoria con un tono dorado que Sofía intentaba capturar en su lienzo. Pero su atención siempre regresaba al violonchelista del rincón, cuya melodía parecía hablarle directamente a su alma..."
        },
        {
            id: 106,
            title: "El Susurro de la Oscuridad",
            author: "Viktor Drago",
            category: "terror",
            price: 0,
            is_premium: true,
            rating: 4.9,
            cover: "assets/horror_demon.png",
            cover_style: "mockup-terror",
            icon: "ri-skull-line",
            description: "Una casa abandonada que guarda los lamentos de quienes entraron y nunca salieron. ¿Te atreves a escuchar?",
            content: "El frío no era normal. Era un frío que calaba los huesos y apagaba la luz de las linternas. En el pasillo del tercer piso, las sombras no se proyectaban desde las paredes, sino que se separaban de ellas, gateando hacia nosotros con un crujido de huesos secos..."
        }
    ];

    let allBooks = [];

    // --- I18N (TRANSLATIONS) ---
    const translations = {
        es: {
            page_title: 'Lumière - Biblioteca Digital',
            menu_label: 'MENÚ', nav_inicio: 'Inicio', nav_explore: 'Explorar', nav_library: 'Mi Biblioteca', nav_favorites: 'Favoritos', nav_cart: 'Tu Carrito',
            categories_label: 'GÉNEROS', cat_all: 'Todos', cat_scifi: 'Ciencia Ficción', cat_fantasy: 'Fantasía', cat_romance: 'Romance', cat_mystery: 'Misterio', cat_tech: 'Tecnología',
            login_prompt: 'Iniciar Sesión', search_placeholder: 'Buscar libros...', btn_premium: 'Premium',
            hero_tag: 'Bestseller del Mes', hero_title: 'Ecos del Futuro', hero_desc: 'Explora el mañana hoy.',
            btn_read_now: 'Leer Ahora', section_trending: 'Tendencias', section_explore: 'Explorar Catálogo', section_favorites: 'Mis Favoritos',
            news_title: 'Lumière Premium', btn_subscribe: 'Suscribirse', email_placeholder: 'Tu email...',
            cat_horror: 'Terror', btn_add_to_cart: 'Añadir al Carrito'
        },
        en: {
            page_title: 'Lumière - Digital Library',
            menu_label: 'MENU', nav_inicio: 'Home', nav_explore: 'Explore', nav_library: 'My Library', nav_favorites: 'Favorites', nav_cart: 'Your Cart',
            categories_label: 'GENRES', cat_all: 'All', cat_scifi: 'Sci-Fi', cat_fantasy: 'Fantasy', cat_romance: 'Romance', cat_mystery: 'Mystery', cat_tech: 'Technology', cat_horror: 'Horror',
            login_prompt: 'Log In', search_placeholder: 'Search books...', btn_premium: 'Premium',
            hero_tag: 'Bestseller of the Month', hero_title: 'Echoes of the Future', hero_desc: 'Explore tomorrow today.',
            btn_read_now: 'Read Now', section_trending: 'Trending', section_explore: 'Explore Catalog', section_favorites: 'My Favorites',
            news_title: 'Lumière Premium', btn_subscribe: 'Subscribe', email_placeholder: 'Your email...',
            btn_add_to_cart: 'Add to Cart'
        }
    };

    function updateLanguage() {
        const dict = translations[appState.lang];
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) el.textContent = dict[key];
        });
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (dict[key]) el.placeholder = dict[key];
        });
        document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.toggle('active', btn.getAttribute('data-lang') === appState.lang));
        renderAll();
    }

    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            appState.lang = e.target.getAttribute('data-lang');
            updateLanguage();
        });
    });

    // --- UI ELEMENTS ---
    const sidebar = document.getElementById('sidebar');
    const btnSidebarToggle = document.getElementById('btnSidebarToggle');
    const mainGrid = document.getElementById('mainBookGrid');
    const exploreGrid = document.getElementById('exploreBookGrid');
    const favGrid = document.getElementById('favoritesBookGrid');
    const pageInfo = document.getElementById('pageInfoDisplay');
    const prevPageBtn = document.getElementById('prevPageBtn');
    const nextPageBtn = document.getElementById('nextPageBtn');

    // --- SIDEBAR LOGIC ---
    function applySidebarState() {
        if (sidebar) {
            sidebar.classList.toggle('collapsed', appState.isSidebarCollapsed);
            const icon = btnSidebarToggle?.querySelector('i');
            if (icon) {
                icon.className = appState.isSidebarCollapsed ? 'ri-menu-unfold-line' : 'ri-menu-fold-line';
            }
        }
        localStorage.setItem('sidebarCollapsed', appState.isSidebarCollapsed);
    }

    btnSidebarToggle?.addEventListener('click', () => {
        appState.isSidebarCollapsed = !appState.isSidebarCollapsed;
        applySidebarState();
    });
    applySidebarState();

    // --- API INTEGRATION ---
    async function fetchBooks() {
        try {
            const response = await fetch(`${API_BASE_URL}/api/books/`);
            if (!response.ok) throw new Error('API Error');
            const apiBooks = await response.json();
            allBooks = apiBooks.length > 0 ? apiBooks : defaultBooks;
            renderAll();
        } catch (error) {
            console.error('API Fetch failed. Using fallback data.', error);
            allBooks = defaultBooks;
            renderAll();
        }
    }

    // --- RENDER LOGIC ---
    function formatPrice(book) {
        if (book.is_premium && book.price === 0) return `<span class="price-tag premium">Premium</span>`;
        if (book.price === 0) return `<span class="price-tag free">Gratis</span>`;
        return `<span class="price-tag paid">$${book.price.toFixed(2)}</span>`;
    }

    function createBookCard(book) {
        const cartBtn = book.price > 0 ?
            `<button class="card-action-btn" onclick="event.stopPropagation(); addToCart(${book.id})"><i class="ri-shopping-cart-2-add-line"></i></button>` : '';

        // La imagen real debe tener prioridad absoluta
        const coverImg = book.cover ? `<img src="${book.cover}" class="book-cover-img" alt="${book.title}" onerror="this.style.display='none'">` : '';
        const coverIcon = `<i class="${book.icon || 'ri-book-line'}"></i>`;

        return `
            <div class="book-card" onclick="openBookModal(${book.id})">
                <div class="book-cover ${book.cover_style || 'mockup-1'}">
                    ${coverIcon}
                    ${coverImg}
                    ${formatPrice(book)}
                    <button class="card-action-btn ${book.is_favorite ? 'active' : ''}" onclick="event.stopPropagation(); toggleFavorite(${book.id})">
                        <i class="ri-heart-${book.is_favorite ? 'fill' : 'line'}"></i>
                    </button>
                    ${cartBtn}
                    <div class="overlay"><i class="ri-play-fill"></i></div>
                </div>
                <div class="book-info">
                    <h3>${book.title}</h3>
                    <p class="author">${book.author}</p>
                    <div class="rating"><i class="ri-star-fill"></i> ${book.rating}</div>
                </div>
            </div>`;
    }

    function renderAll() {
        renderFeatured();
        renderExplore();
        renderFavorites();
        updateCartBadge();
    }

    function renderFeatured() {
        if (mainGrid) mainGrid.innerHTML = allBooks.slice(0, 4).map(createBookCard).join('');
    }

    function renderExplore() {
        if (!exploreGrid) return;

        let filtered = allBooks.filter(b => {
            const matchesCat = appState.activeCategory === 'all' || b.category === appState.activeCategory;
            const matchesPrice = appState.activePriceFilter === 'all' ||
                (appState.activePriceFilter === 'free' && b.price === 0 && !b.is_premium) ||
                (appState.activePriceFilter === 'premium' && b.is_premium) ||
                (appState.activePriceFilter === 'paid' && b.price > 0);
            const matchesSearch = b.title.toLowerCase().includes(appState.searchQuery.toLowerCase()) ||
                b.author.toLowerCase().includes(appState.searchQuery.toLowerCase());
            return matchesCat && matchesPrice && matchesSearch;
        });

        // Paginación
        const totalItems = filtered.length;
        const totalPages = Math.ceil(totalItems / appState.itemsPerPage) || 1;
        if (appState.currentPage > totalPages) appState.currentPage = totalPages;

        const start = (appState.currentPage - 1) * appState.itemsPerPage;
        const end = start + appState.itemsPerPage;
        const pageItems = filtered.slice(start, end);

        exploreGrid.innerHTML = pageItems.map(createBookCard).join('') || '<p class="empty-msg">No se encontraron libros.</p>';
        if (pageInfo) pageInfo.innerText = `${appState.currentPage} / ${totalPages}`;

        prevPageBtn?.classList.toggle('disabled', appState.currentPage === 1);
        nextPageBtn?.classList.toggle('disabled', appState.currentPage === totalPages);
    }

    function renderFavorites() {
        if (favGrid) favGrid.innerHTML = allBooks.filter(b => b.is_favorite).map(createBookCard).join('') || '<p class="empty-msg">No tienes favoritos aún.</p>';
    }

    // --- MANEJO DE EVENTOS ---
    window.toggleFavorite = (id) => {
        const book = allBooks.find(b => b.id === id);
        if (book) {
            book.is_favorite = !book.is_favorite;
            renderAll();
            // Actualizar modal si está abierto con este libro
            const modal = document.getElementById('bookModal');
            if (modal?.classList.contains('active')) {
                const favBtn = document.getElementById('modalFavAction');
                if (favBtn) {
                    const icon = favBtn.querySelector('i');
                    if (icon) icon.className = book.is_favorite ? 'ri-heart-fill' : 'ri-heart-line';
                    favBtn.classList.toggle('active', book.is_favorite);
                }
            }
        }
    };

    window.addToCart = (id) => {
        const book = allBooks.find(b => b.id === id);
        if (book && !appState.cart.find(item => item.id === id)) {
            appState.cart.push(book);
            localStorage.setItem('lumiere_cart', JSON.stringify(appState.cart));
            updateCartBadge();
            alert(`Añadido: ${book.title}`);
        }
    };

    function updateCartBadge() {
        const badge = document.getElementById('cartBadge');
        if (badge) {
            badge.innerText = appState.cart.length;
            badge.style.display = appState.cart.length > 0 ? 'flex' : 'none';
        }
    }

    // --- EVENTOS DE PAGINACIÓN ---
    prevPageBtn?.addEventListener('click', () => { if (appState.currentPage > 1) { appState.currentPage--; renderExplore(); } });
    nextPageBtn?.addEventListener('click', () => {
        const totalPages = Math.ceil(allBooks.length / appState.itemsPerPage);
        if (appState.currentPage < totalPages) { appState.currentPage++; renderExplore(); }
    });

    // --- EVENTOS DE FILTRO ---
    document.getElementById('filter-price-select')?.addEventListener('change', (e) => {
        appState.activePriceFilter = e.target.value;
        appState.currentPage = 1;
        renderExplore();
    });

    document.getElementById('searchInput')?.addEventListener('input', (e) => {
        appState.searchQuery = e.target.value;
        appState.currentPage = 1;
        renderExplore();
    });

    document.querySelectorAll('.pill, .category-filter').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const cat = btn.getAttribute('data-category');
            appState.activeCategory = cat;
            appState.currentPage = 1;

            document.querySelectorAll('.pill, .category-filter').forEach(b => b.classList.toggle('active', b.getAttribute('data-category') === cat));
            renderExplore();
        });
    });

    // --- SISTEMA DE TABS ---
    document.querySelectorAll('.nav-item[data-tab]').forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const tabId = item.getAttribute('data-tab');
            appState.activeTab = tabId;

            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
            item.classList.add('active');

            document.querySelectorAll('.tab-content').forEach(c => c.classList.toggle('active', c.id === `tab-${tabId}`));
        });
    });

    // --- LÓGICA DE MODAL ---
    window.openBookModal = (id) => {
        const book = allBooks.find(b => b.id === id);
        if (!book) return;

        document.getElementById('modalTitle').innerText = book.title;
        document.getElementById('modalAuthor').innerText = book.author;
        document.getElementById('modalDesc').innerText = book.description || 'Sin descripción disponible.';
        document.getElementById('modalPrice').innerHTML = formatPrice(book);
        document.getElementById('readingContentText').innerText = book.content || 'Contenido no disponible.';

        const coverDiv = document.getElementById('modalCover');
        coverDiv.className = `modal-cover ${book.cover_style || 'mockup-1'}`;
        coverDiv.innerHTML = book.cover ? `<img src="${book.cover}" class="book-cover-img" alt="${book.title}">` : `<i class="${book.icon || 'ri-book-line'}"></i>`;

        const modal = document.getElementById('bookModal');
        modal.classList.add('active');

        // Configurar acciones del modal
        const cartBtn = document.getElementById('modalCartAction');
        const favBtn = document.getElementById('modalFavAction');

        if (favBtn) {
            const favIcon = favBtn.querySelector('i');
            if (favIcon) favIcon.className = book.is_favorite ? 'ri-heart-fill' : 'ri-heart-line';
            favBtn.classList.toggle('active', book.is_favorite);
            favBtn.onclick = (e) => { e.stopPropagation(); toggleFavorite(book.id); };
        }

        if (cartBtn) {
            if (book.price > 0) {
                cartBtn.style.display = 'flex';
                cartBtn.onclick = (e) => { e.stopPropagation(); addToCart(book.id); };
            } else {
                cartBtn.style.display = 'none';
            }
        }

        // Preparar vista previa enriquecida
        readingContentText.innerHTML = `
            <h1 class="reading-title-preview">${book.title}</h1>
            <span class="reading-author-preview">${book.author}</span>
            <div class="reading-body-text">${book.content || 'Contenido no disponible.'}</div>
        `;
    };

    document.getElementById('closeModalBtn')?.addEventListener('click', () => {
        const modal = document.getElementById('bookModal');
        modal.classList.remove('active');
        // Resetear vista de lectura al cerrar
        document.querySelector('.modal-body').classList.remove('reading-active');
    });

    // --- LÓGICA DE LECTURA (VISTA PREVIA) ---
    const modalPreviewBtn = document.getElementById('modalPreviewAction');
    const backToDetailsBtn = document.getElementById('btnBackToDetails');
    const modalBody = document.querySelector('.modal-body');
    const readingContainer = document.getElementById('readingContainer');
    const readingContentText = document.getElementById('readingContentText');

    modalPreviewBtn?.addEventListener('click', () => {
        modalBody.classList.add('reading-active');
    });

    backToDetailsBtn?.addEventListener('click', () => {
        modalBody.classList.remove('reading-active');
    });

    // Controles de Lector
    let currentFontSize = 18;
    document.getElementById('increaseFont')?.addEventListener('click', () => {
        currentFontSize += 2;
        readingContentText.style.fontSize = `${currentFontSize}px`;
    });
    document.getElementById('decreaseFont')?.addEventListener('click', () => {
        if (currentFontSize > 12) {
            currentFontSize -= 2;
            readingContentText.style.fontSize = `${currentFontSize}px`;
        }
    });

    document.querySelectorAll('.theme-dot').forEach(dot => {
        dot.addEventListener('click', () => {
            const theme = dot.getAttribute('data-theme');
            // Limpiar temas
            readingContainer.classList.remove('theme-light', 'theme-sepia', 'theme-dark');
            readingContainer.classList.add(`theme-${theme}`);

            document.querySelectorAll('.theme-dot').forEach(d => d.classList.remove('active'));
            dot.classList.add('active');
        });
    });

    // --- ESTADO DEL SISTEMA ---
    document.getElementById('btnSystemStatus')?.addEventListener('click', async (e) => {
        e.preventDefault();
        try {
            const response = await fetch(`${API_BASE_URL}/api/v1/status`);
            if (!response.ok) throw new Error('Status API unreachable');
            const status = await response.json();

            const statusMsg = `
                📌 ESTADO DEL SISTEMA LUMIÈRE
                --------------------------------
                Estado: ${status.status.toUpperCase()}
                Versión: ${status.version}
                Arquitectura: ${status.architecture}
                Persistencia: ${status.persistence.mode}
                
                📊 CATÁLOGO ACTUAL:
                Libros: ${status.data_count.books}
                Usuarios: ${status.data_count.users}
                
                🔐 SEGURIDAD:
                Auth: ${status.security.auth_enabled ? 'Activado' : 'Desactivado'}
                JWT: ${status.security.jwt_algorithm}
            `;
            alert(statusMsg);
        } catch (error) {
            alert('Error al conectar con el servicio de estado del backend.');
        }
    });

    // --- CARRITO ---
    document.getElementById('cartToggleBtn')?.addEventListener('click', (e) => {
        e.preventDefault();
        renderCart();
        document.getElementById('cartModal').classList.add('active');
    });

    function renderCart() {
        const container = document.getElementById('cartItemsContainer');
        const subtotalEl = document.getElementById('cartSubtotal');
        if (!container) return;

        if (appState.cart.length === 0) {
            container.innerHTML = '<p class="empty-msg">Tu carrito está vacío.</p>';
            subtotalEl.innerText = '$0.00';
            return;
        }

        let total = 0;
        container.innerHTML = appState.cart.map(item => {
            total += item.price;
            return `
                <div class="cart-item">
                    <div class="cart-item-info">
                        <h4>${item.title}</h4>
                        <span>$${item.price.toFixed(2)}</span>
                    </div>
                    <button class="cart-item-remove" onclick="removeFromCart(${item.id})"><i class="ri-delete-bin-line"></i></button>
                </div>`;
        }).join('');
        subtotalEl.innerText = `$${total.toFixed(2)}`;
    }

    window.removeFromCart = (id) => {
        appState.cart = appState.cart.filter(i => i.id !== id);
        localStorage.setItem('lumiere_cart', JSON.stringify(appState.cart));
        updateCartBadge();
        renderCart();
    };

    document.getElementById('closeCartModalBtn')?.addEventListener('click', () => document.getElementById('cartModal').classList.remove('active'));

    // --- INICIALIZACIÓN ---
    updateLanguage();
    fetchBooks();

});
