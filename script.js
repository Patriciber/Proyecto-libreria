document.addEventListener('DOMContentLoaded', () => {

    // --- APP STATE & MOCK DATA ---
    let appState = {
        lang: 'es',
        isLoggedIn: false,
        isPremium: false,
        userName: 'Invitado',
        activeTab: 'inicio',
        activeCategory: 'all',
        searchQuery: '',
        isSidebarCollapsed: localStorage.getItem('sidebarCollapsed') === 'true',
        cart: []
    };

    const sidebar = document.getElementById('sidebar');
    const btnSidebarToggle = document.getElementById('btnSidebarToggle');

    // Function to apply sidebar state (collapsed or expanded)
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

    // Toggle Sidebar Event
    btnSidebarToggle?.addEventListener('click', () => {
        appState.isSidebarCollapsed = !appState.isSidebarCollapsed;
        applySidebarState();
    });

    // Initial sidebar state on load
    applySidebarState();

    let mockBooks = [];

    // Fetch books from the API
    async function fetchBooks() {
        try {
            // Updated to /api/books/ with trailing slash to match FastAPI router
            const response = await fetch('/api/books/');
            if (!response.ok) {
                throw new Error(`Server responded with status ${response.status}: ${response.statusText}`);
            }
            const data = await response.json();
            mockBooks = data;
            renderBooks();
        } catch (error) {
            console.error('Error fetching books from backend:', error);
            // Fallback mock data if API is down
            mockBooks = [
                { id: 1, title: 'Ecos del Futuro', author: 'Visionarios', desc: 'Tecnologías del mañana.', content: 'Texto completo de Ecos del Futuro...', rating: 4.8, category: 'tecnologia', isPremium: false, isFavorite: false, icon: 'ri-rocket-2-fill', coverStyle: 'mockup-1', price: 0 },
                { id: 2, title: 'Crónicas Galácticas', author: 'S.F. Writer', desc: 'Exploración espacial.', content: 'Texto completo de Crónicas Galácticas...', rating: 4.2, category: 'ciencia_ficcion', isPremium: true, isFavorite: false, icon: 'ri-planet-line', coverStyle: 'mockup-2', price: 0 },
                { id: 3, title: 'El Enigma del Tiempo', author: 'Jane Doe', desc: 'Misterio temporal.', content: 'Texto completo del Enigma del Tiempo...', rating: 4.5, category: 'misterio', isPremium: false, isFavorite: false, icon: 'ri-time-line', coverStyle: 'mockup-3', price: 0 },
                { id: 4, title: 'Amor Digital', author: 'Cyber Cupid', desc: 'Romance en bits.', content: 'Texto completo de Amor Digital...', rating: 4.0, category: 'romance', isPremium: false, isFavorite: false, icon: 'ri-heart-pulse-fill', coverStyle: 'mockup-1', price: 0 }
            ];
            renderBooks();
        }
    }

    // --- I18N (TRANSLATIONS) ---
    const translations = {
        es: {
            page_title: 'Lumière - Biblioteca Digital',
            menu_label: 'MENÚ', nav_inicio: 'Inicio', nav_explore: 'Explorar', nav_library: 'Mi Biblioteca', nav_favorites: 'Favoritos',
            categories_label: 'CATEGORÍAS', cat_all: 'Todos', cat_scifi: 'Ciencia Ficción', cat_fantasy: 'Fantasía', cat_romance: 'Romance', cat_mystery: 'Misterio',
            login_prompt: 'Iniciar Sesión', search_placeholder: 'Buscar libros, autores, géneros...', btn_premium: 'Premium',
            hero_tag: 'Bestseller del Mes', hero_title: 'Ecos del Futuro', hero_desc: 'Una inmersión profunda en las tecnologías que moldearán nuestro mañana, escrita por los visionarios de hoy.',
            btn_read_now: 'Leer Ahora (Gratis)', btn_save: 'Guardar', section_trending: 'Tendencias Actuales', btn_view_all: 'Ver todos',
            section_explore: 'Explorar Catálogo', section_library: 'Mi Biblioteca', empty_library: 'Aún no has guardado libros para leer más tarde.',
            section_favorites: 'Mis Favoritos', news_title: 'Únete a Lumière Premium', news_desc: 'Recibe promociones exclusivas, descuentos en libros de pago y recomendaciones personalizadas por correo electrónico.',
            email_placeholder: 'Tu correo electrónico...', btn_subscribe: 'Suscribirse', partners_title: 'Con el apoyo de nuestros socios:',
            btn_preview: 'Vista Previa',
            auth_title: 'Bienvenido a Lumière', auth_desc: 'Inicia sesión o crea una cuenta para guardar tus libros y acceder a contenido Premium.',
            tab_login: 'Iniciar Sesión', tab_register: 'Registrarse', label_email: 'Correo Electrónico', label_password: 'Contraseña', label_name: 'Nombre Completo',
            btn_login_submit: 'Entrar', btn_register_submit: 'Crear Cuenta',
            price_free: 'Gratis', price_premium_only: 'Solo Premium'
        },
        en: {
            page_title: 'Lumière - Digital Library',
            menu_label: 'MENU', nav_inicio: 'Home', nav_explore: 'Explore', nav_library: 'My Library', nav_favorites: 'Favorites',
            categories_label: 'CATEGORIES', cat_all: 'All', cat_scifi: 'Sci-Fi', cat_fantasy: 'Fantasy', cat_romance: 'Romance', cat_mystery: 'Mystery',
            login_prompt: 'Log In', search_placeholder: 'Search books, authors, genres...', btn_premium: 'Premium',
            hero_tag: 'Bestseller of the Month', hero_title: 'Echoes of the Future', hero_desc: 'A deep dive into the technologies shaping our tomorrow, written by today’s visionaries.',
            btn_read_now: 'Read Now (Free)', btn_save: 'Save', section_trending: 'Trending Now', btn_view_all: 'View all',
            section_explore: 'Explore Catalog', section_library: 'My Library', empty_library: 'You haven’t saved any books for later yet.',
            section_favorites: 'My Favorites', news_title: 'Join Lumière Premium', news_desc: 'Get exclusive promotions, discounts on paid books, and personalized recommendations via email.',
            email_placeholder: 'Your email address...', btn_subscribe: 'Subscribe', partners_title: 'Supported by our partners:',
            btn_preview: 'Preview',
            auth_title: 'Welcome to Lumière', auth_desc: 'Log in or create an account to save your books and access Premium content.',
            tab_login: 'Log In', tab_register: 'Register', label_email: 'Email Address', label_password: 'Password', label_name: 'Full Name',
            btn_login_submit: 'Enter', btn_register_submit: 'Create Account',
            price_free: 'Free', price_premium_only: 'Premium Only'
        }
    };

    function updateLanguage() {
        const lang = appState.lang;
        const dict = translations[lang];

        // Update simple text elements
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) el.textContent = dict[key];
        });

        // Update placeholders (Line 110 fix: ensure element can have a placeholder)
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (dict[key] && (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA')) {
                el.placeholder = dict[key];
            }
        });

        // Update active language button
        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
        });

        renderBooks();
    }

    // Language switcher events
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            appState.lang = e.target.getAttribute('data-lang');
            updateLanguage();
        });
    });

    // --- RENDER LOGIC ---
    function formatPrice(book) {
        const dict = translations[appState.lang];
        if (book.isPremium && book.price === 0) {
            return `<span class="price-tag premium">${dict.price_premium_only}</span>`;
        }
        if (book.price === 0) {
            return `<span class="price-tag free">${dict.price_free}</span>`;
        }
        return `<span class="price-tag paid">$${book.price}</span>`;
    }

    function getBookCoverHTML(book) {
        const imageMap = {
            'tecnologia': 'assets/tech_book_cover.png',
            'ciencia_ficcion': 'assets/scifi_book_cover.png',
            'misterio': 'assets/mystery_book_cover.png',
            'romance': 'assets/romance_book_cover.png',
            'fantasia': 'assets/fantasy_book_cover.png',
            'autoayuda': 'assets/selfhelp_book_cover.png'
        };
        const coverSrc = imageMap[book.category];
        if (coverSrc) {
            return `<img src="${coverSrc}" class="book-cover-img" alt="${book.title} portadilla">`;
        }
        return '';
    }

    // Create the HTML card for a book
    function createBookCard(book) {
        const cartBtn = book.price > 0 ? 
            `<button class="card-action-btn" data-action="add-to-cart" data-id="${book.id}">
                <i class="ri-shopping-cart-2-add-line"></i>
             </button>` : '';

        return `
                <div class="book-card" tabindex="0" data-id="${book.id}">
                    <div class="book-cover ${book.coverStyle}">
                        ${getBookCoverHTML(book)}
                        ${formatPrice(book)}
                        <button class="card-action-btn ${book.isFavorite ? 'active' : ''}" data-action="favorite" data-id="${book.id}" style="right: ${book.price > 0 ? '60px' : '10px'}">
                            <i class="ri-heart-${book.isFavorite ? 'fill' : 'line'}"></i>
                        </button>
                        ${cartBtn}
                        <i class="${book.icon}"></i>
                        <div class="overlay">
                            <button class="play-btn" data-action="open-modal" data-id="${book.id}"><i class="ri-play-fill"></i></button>
                        </div>
                    </div>
                    <div class="book-info">
                        <h3>${book.title}</h3>
                        <p class="author">${book.author}</p>
                        <div class="rating"><i class="ri-star-fill"></i> ${book.rating}</div>
                    </div>
                </div>
            `;
    }

    // Render book grids
    function renderBooks() {
        const mainGrid = document.getElementById('mainBookGrid');
        const exploreGrid = document.getElementById('exploreBookGrid');
        const favGrid = document.getElementById('favoritesBookGrid');

        // Robust check to ensure mockBooks is an array
        const books = Array.isArray(mockBooks) ? mockBooks : [];

        if (mainGrid) mainGrid.innerHTML = books.slice(0, 4).map(createBookCard).join('');

        if (exploreGrid) {
            let filteredBooks = appState.activeCategory === 'all'
                ? [...books]
                : books.filter(b => b.category === appState.activeCategory);

            if (appState.searchQuery && appState.searchQuery.trim() !== '') {
                const queryLower = appState.searchQuery.trim().toLowerCase();
                filteredBooks = filteredBooks.filter(book =>
                    (book.title?.toLowerCase().includes(queryLower)) ||
                    (book.author?.toLowerCase().includes(queryLower)) ||
                    (book.desc?.toLowerCase().includes(queryLower)) ||
                    (book.category?.toLowerCase().includes(queryLower))
                );
            }

            exploreGrid.innerHTML = filteredBooks.map(createBookCard).join('');
        }

        if (favGrid) {
            const favBooks = mockBooks.filter(b => b.isFavorite);
            favGrid.innerHTML = favBooks.map(createBookCard).join('');
        }

        attachCardEvents();
    }

    // --- TAB SYSTEM ---
    const navItems = document.querySelectorAll('.nav-item, .category-filter, .pill');
    const tabContents = document.querySelectorAll('.tab-content');

    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const tabId = item.getAttribute('data-tab');
            const category = item.getAttribute('data-category');

            if (tabId) {
                appState.activeTab = tabId;
                // Update Sidebar Nav
                document.querySelectorAll('.sidebar .nav-item').forEach(nav => nav.classList.remove('active'));
                if (item.classList.contains('nav-item')) item.classList.add('active');

                // Update Main Content
                tabContents.forEach(content => {
                    content.classList.remove('active');
                    if (content.id === `tab-${tabId}`) content.classList.add('active');
                });
            } else if (category) {
                // Quick category filter from sidebar
                appState.activeTab = 'explorar';
                appState.activeCategory = category;

                document.querySelectorAll('.sidebar .nav-item').forEach(nav => nav.classList.remove('active'));
                const exp = document.querySelector('[data-tab="explorar"]');
                if (exp) exp.classList.add('active');

                document.querySelectorAll('.category-filter, .pill').forEach(f => {
                    const cat = f.getAttribute('data-category');
                    f.classList.toggle('active', cat === category);
                });

                tabContents.forEach(c => c.classList.remove('active'));
                const t = document.getElementById('tab-explorar');
                if (t) t.classList.add('active');

                renderBooks();
            }
        });
    });

    // --- MODALS ---
    const bookModal = document.getElementById('bookModal');
    const authModal = document.getElementById('authModal');
    const modalBody = document.querySelector('.modal-body');
    const readingContainer = document.getElementById('readingContainer');

    // Attach events to book cards
    function attachCardEvents() {
        document.querySelectorAll('.book-card').forEach(card => {
            card.addEventListener('click', (e) => {
                if (e.target.closest('.card-action-btn')) {
                    const btn = e.target.closest('.card-action-btn');
                    const action = btn.getAttribute('data-action');
                    const bookId = parseInt(btn.getAttribute('data-id'));
                    
                    if (action === 'favorite') {
                        toggleFavorite(e, bookId);
                    } else if (action === 'add-to-cart') {
                        e.stopPropagation();
                        addToCart(bookId);
                    }
                    return;
                }
                const bookId = parseInt(card.getAttribute('data-id'));
                const book = mockBooks.find(b => b.id === bookId);
                if (book) openBookModal(book);
            });
        });
    }

    // Toggle Favorites
    function toggleFavorite(e, id) {
        e.stopPropagation();
        if (!appState.isLoggedIn) {
            openAuthModal();
            return;
        }
        const b = mockBooks.find(book => book.id === parseInt(id));
        if (b) {
            b.isFavorite = !b.isFavorite;
            renderBooks(); // Redraw grids
        }
    }

    // Open Modal with Book details
    function openBookModal(book) {
        modalBody.classList.remove('reading-active');
        document.getElementById('modalTitle').innerText = book.title;
        document.getElementById('modalAuthor').innerText = book.author;
        document.getElementById('modalDesc').innerText = book.desc;
        document.getElementById('readingTitle').innerText = book.title;
        document.getElementById('readingContentText').innerText = book.content;

        const coverDiv = document.getElementById('modalCover');
        coverDiv.className = `modal-cover ${book.coverStyle}`;
        coverDiv.innerHTML = getBookCoverHTML(book) || `<i class="${book.icon}"></i>`;

        const priceEl = document.getElementById('modalPrice');
        priceEl.innerHTML = formatPrice(book).replace('price-tag', 'price-tag large');

        bookModal.classList.add('active');
    }

    // Open Auth Modal
    function openAuthModal() {
        authModal.classList.add('active');
    }

    // Modal main action (Read now)
    document.getElementById('modalMainAction').addEventListener('click', () => {
        const title = document.getElementById('modalTitle').innerText;
        const book = mockBooks.find(b => b.title === title);

        if (book.isPremium && !appState.isPremium) {
            if (!appState.isLoggedIn) {
                openAuthModal();
            } else {
                alert(appState.lang === 'es' ? 'Libro Premium. Por favor, adquiere una suscripción.' : 'Premium Book. Please upgrade your plan.');
            }
            return;
        }
        modalBody.classList.add('reading-active');
    });

    // Back to details from reader view
    document.getElementById('btnBackToDetails').addEventListener('click', () => {
        modalBody.classList.remove('reading-active');
    });

    // Preview Book
    document.getElementById('modalPreviewAction').addEventListener('click', () => {
        const title = document.getElementById('modalTitle').innerText;
        const book = mockBooks.find(b => b.title === title);
        if (book) {
            alert(`${book.title} - Preview:\n\n${book.content.slice(0, 150)}...`);
        }
    });

    // Search Logic
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            appState.searchQuery = e.target.value;
            renderBooks();
        });
    }

    // Close Modals
    document.getElementById('closeModalBtn').addEventListener('click', () => bookModal.classList.remove('active'));
    document.getElementById('closeAuthModalBtn').addEventListener('click', () => authModal.classList.remove('active'));

    // User Profile Button
    document.getElementById('userProfileBtn').addEventListener('click', () => {
        if (!appState.isLoggedIn) openAuthModal();
    });

    // System Status Diagnostic
    document.getElementById('btnSystemStatus')?.addEventListener('click', async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('/api/v1/status');
            const data = await response.json();
            
            // Robust check for data properties to avoid crashes if server returns an error
            if (data.status === 'error' || !data.persistence) {
                alert(`⚠️ DIAGNÓSTICO: El servidor reportó un problema.\n\nError: ${data.message || 'Desconocido'}\nDetalle: ${data.error || 'N/A'}`);
                return;
            }

            const statusMsg = `
🔍 DIAGNÓSTICO DEL SISTEMA
--------------------------------
Estado: ${data.status.toUpperCase()}
Versión: ${data.version}
Persistencia: ${data.persistence.mode}
Configuración: ${data.persistence.database_mode_config}

📊 DATOS CARGADOS:
- Libros: ${data.data_count.books}
- Usuarios: ${data.data_count.users}

Logueado actualmente: ${appState.isLoggedIn ? 'SÍ (' + appState.userName + ')' : 'NO'}
            `;
            alert(statusMsg);
        } catch (error) {
            console.error('Error al obtener el estado del sistema:', error);
            alert('Error: No se pudo conectar con el servidor de diagnóstico o el formato de respuesta es inválido.');
        }
    });

    // Close modals on outside click
    [bookModal, authModal].forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) modal.classList.remove('active');
        });
    });

    // --- READER CONTROLS LOGIC ---
    const readerSettings = {
        fontSize: parseInt(localStorage.getItem('readerFontSize')) || 18,
        fontFamily: localStorage.getItem('readerFontFamily') || 'sans',
        theme: localStorage.getItem('readerTheme') || 'light'
    };

    const readingContentText = document.getElementById('readingContentText');

    // Apply visual settings to the reader container
    function applyReaderSettings() {
        if (readingContentText) {
            readingContentText.style.fontSize = `${readerSettings.fontSize}px`;
        }
        
        if (readingContainer) {
            readingContainer.classList.toggle('font-serif', readerSettings.fontFamily === 'serif');
            readingContainer.classList.remove('theme-light', 'theme-sepia', 'theme-dark');
            readingContainer.classList.add(`theme-${readerSettings.theme}`);
        }

        // Highlight active theme in UI
        document.querySelectorAll('.theme-dot').forEach(dot => {
            dot.classList.toggle('active', dot.getAttribute('data-theme') === readerSettings.theme);
        });

        // Persist to localStorage
        localStorage.setItem('readerFontSize', readerSettings.fontSize);
        localStorage.setItem('readerFontFamily', readerSettings.fontFamily);
        localStorage.setItem('readerTheme', readerSettings.theme);
    }

    // Font size listeners
    document.getElementById('increaseFont')?.addEventListener('click', () => {
        if (readerSettings.fontSize < 32) {
            readerSettings.fontSize += 2;
            applyReaderSettings();
        }
    });

    document.getElementById('decreaseFont')?.addEventListener('click', () => {
        if (readerSettings.fontSize > 12) {
            readerSettings.fontSize -= 2;
            applyReaderSettings();
        }
    });

    // Toggle font family (Sans vs Serif)
    document.getElementById('toggleFontFamily')?.addEventListener('click', () => {
        readerSettings.fontFamily = readerSettings.fontFamily === 'sans' ? 'serif' : 'sans';
        applyReaderSettings();
    });

    // Theme selection (Light, Sepia, Dark)
    document.querySelectorAll('.theme-dot').forEach(dot => {
        dot.addEventListener('click', () => {
            readerSettings.theme = dot.getAttribute('data-theme');
            applyReaderSettings();
        });
    });

    // Initial apply
    applyReaderSettings();

    // --- AUTH ---
    document.getElementById('loginForm')?.addEventListener('submit', (e) => {
        e.preventDefault();
        appState.isLoggedIn = true;
        appState.userName = e.target.querySelector('input[type="email"]').value.split('@')[0];
        updateProfileUI();
        authModal.classList.remove('active');
    });

    // Update user profile UI
    function updateProfileUI() {
        const nameEl = document.getElementById('userNameDisplay');
        const planEl = document.getElementById('userPlanDisplay');
        const avatarImg = document.getElementById('userAvatarImg');
        const placeholder = document.getElementById('userAvatarPlaceholder');

        if (appState.isLoggedIn) {
            nameEl.innerText = appState.userName;
            nameEl.removeAttribute('data-i18n'); // Stop translating name once set
            planEl.style.display = 'block';
            planEl.innerText = appState.isPremium ? 'Premium Member' : 'Free Member';
            avatarImg.style.display = 'block';
            placeholder.style.display = 'none';
        }
    }

    // --- INITIALIZATION ---
    updateLanguage();
    fetchBooks();
    
    // --- CART MANAGEMENT ---
    function updateCartBadge() {
        const badge = document.getElementById('cartBadge');
        if (badge) {
            badge.textContent = appState.cart.length;
            badge.style.display = appState.cart.length > 0 ? 'inline-block' : 'none';
        }
    }

    function addToCart(bookId) {
        const book = mockBooks.find(b => b.id === bookId);
        if (book && book.price > 0 && !appState.cart.some(i => i.id === bookId)) {
            appState.cart.push(book);
            updateCartBadge();
            alert(`Añadido: ${book.title} al carrito.`);
        } else if (appState.cart.some(i => i.id === bookId)) {
            alert('El libro ya está en tu carrito.');
        }
    }

    function renderCartModal() {
        const container = document.getElementById('cartItemsContainer');
        const subtotalEl = document.getElementById('cartSubtotal');
        const checkoutBtn = document.getElementById('checkoutBtn');
        
        if (!container) return;

        if (appState.cart.length === 0) {
            container.innerHTML = '<p style="text-align: center; color: var(--text-dim)">El carrito está vacío.</p>';
            subtotalEl.textContent = '$0.00';
            checkoutBtn.disabled = true;
            return;
        }

        checkoutBtn.disabled = false;
        let subtotal = 0;
        
        container.innerHTML = appState.cart.map(book => {
            subtotal += book.price;
            return `
                <div class="cart-item">
                    <div class="cart-item-info">
                        <h4>${book.title}</h4>
                        <span class="cart-item-price">$${book.price.toFixed(2)}</span>
                    </div>
                    <button class="cart-item-remove" onclick="removeFromCart(${book.id})"><i class="ri-delete-bin-line"></i></button>
                </div>
            `;
        }).join('');
        
        subtotalEl.textContent = '$' + subtotal.toFixed(2);
    }
    
    window.removeFromCart = function(bookId) {
        appState.cart = appState.cart.filter(b => b.id !== bookId);
        updateCartBadge();
        renderCartModal();
    };

    const cartToggleBtn = document.getElementById('cartToggleBtn');
    if (cartToggleBtn) {
        cartToggleBtn.addEventListener('click', (e) => {
            e.preventDefault();
            renderCartModal();
            document.getElementById('cartModal').classList.add('active');
        });
    }

    // Modal click-outside dismissal updates
    window.onclick = function(event) {
        if (event.target === document.getElementById('authModal')) {
            document.getElementById('authModal').classList.remove('active');
        }
        if (event.target === document.getElementById('cartModal')) {
            document.getElementById('cartModal').classList.remove('active');
        }
    };

    updateCartBadge();
});
