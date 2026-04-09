# Documentación de Categorías y Datos de Libros - Lumière Frontend

Esta documentación detalla cómo el frontend de Lumière gestiona las categorías de libros y los datos iniciales para asegurar una experiencia de usuario fluida, incluso sin conexión al backend.

## Categorías Automáticas
El sistema soporta las siguientes categorías, sincronizadas entre la interfaz (HTML) y la lógica de filtrado (JS):

| ID Categoría | Nombre (ES) | Nombre (EN) | Icono |
| :--- | :--- | :--- | :--- |
| `all` | Todos | All | `ri-layout-grid-line` |
| `ciencia_ficcion` | Ciencia Ficción | Sci-Fi | `ri-rocket-line` |
| `fantasia` | Fantasía | Fantasy | `ri-magic-line` |
| `romance` | Romance | Romance | `ri-empathize-line` |
| `misterio` | Misterio | Mystery | `ri-search-eye-line` |
| `tecnologia` | Tecnología | Technology | `ri-macbook-line` |
| `terror` | Terror | Horror | `ri-skull-line` |
| `romance` | Romance | Romance | `ri-empathize-line` |

## Estructura de Datos del Libro
Cada libro en el frontend sigue este esquema de objeto:

```javascript
{
    id: Number,         // ID único
    title: String,      // Título del libro
    author: String,     // Autor
    category: String,   // ID de categoría (ver tabla arriba)
    price: Number,      // 0 para gratis, >0 de pago
    is_premium: Boolean, // Requiere suscripción premium
    rating: Number,     // Calificación (0.0 - 5.0)
    cover: String,      // Ruta a la imagen de portada
    cover_style: String, // Clase CSS para el estilo del mockup
    icon: String,       // Clase del icono de Remix Icon
    description: String, // Sinopsis corta
    content: String      // Texto para la vista previa de lectura
}
```

## Sistema de Respaldo (Fallback)
Para garantizar que la aplicación sea funcional de inmediato, el script intenta obtener libros de la API (`http://127.0.0.1:8080/api/books/`). Si la API no responde o devuelve un catálogo vacío, el frontend carga automáticamente 4 libros predeterminados de alta calidad con portadas generadas por IA.

## Vista Previa de Lectura
La vista previa se activa desde el modal de detalles del libro. Ofrece:
- **Modos de Lectura**: Claro, Sepia y Oscuro.
- **Control de Tipografía**: Ajuste dinámico del tamaño de fuente.
- **Presentación Premium**: Títulos y autores con degradados y diseño optimizado para la lectura.
