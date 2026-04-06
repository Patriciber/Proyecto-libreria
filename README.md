# Lumière Digital Library - Arquitectura Hexagonal

## 📚 Descripción

API REST para la biblioteca digital Lumière, implementada siguiendo los principios de **Arquitectura Hexagonal (Ports & Adapters)**.

## 🏗️ Arquitectura

### Estructura de Capas

```
app/
├── config.py              # Configuración centralizada
├── container.py           # Contenedor de dependencias
├── logging_config.py      # Configuración de logging
├── middleware.py          # Middleware personalizado
├── main.py               # Punto de entrada FastAPI
├── models/               # Modelos Pydantic (DTOs)
├── domain/               # 📦 DOMINIO (Reglas de negocio puras)
│   ├── entities/         # Entidades del dominio
│   ├── services/         # Servicios de aplicación
│   └── exceptions.py     # Excepciones del dominio
├── ports/                # 🔌 PUERTOS (Interfaces/Contratos)
│   └── repositories/     # Interfaces de repositorios
└── adapters/             # 🔧 ADAPTADORES (Implementaciones concretas)
    └── repositories/     # Implementaciones de repositorios
```

### Principios Aplicados

✅ **Separación de responsabilidades** - Cada capa tiene una única responsabilidad
✅ **Inversión de dependencias** - El dominio no depende de frameworks externos
✅ **Interfaces abstractas** - Puertos definen contratos, no implementaciones
✅ **Inyección de dependencias** - Contenedor centralizado para gestión de dependencias
✅ **Logging estructurado** - Middleware personalizado para trazabilidad
✅ **Manejo robusto de errores** - Excepciones específicas del dominio

## 🚀 Inicio Rápido

### Prerrequisitos
- Python 3.8+
- pip

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <repository-url>
   cd lumiere-library
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install fastapi uvicorn pydantic pydantic-settings
   ```

4. **Ejecutar la aplicación**
   ```bash
   python main.py
   ```

5. **Acceder a la documentación**
   - API Docs: http://localhost:8080/docs
   - Health Check: http://localhost:8080/health

## 📋 Endpoints Disponibles

### Libros
- `GET /api/books` - Lista todos los libros (con filtros opcionales)
- `GET /api/books/{id}` - Obtiene un libro específico
- `GET /api/books/featured/` - Libros destacados
- `GET /api/books/free/` - Libros gratuitos
- `GET /api/books/premium/` - Libros premium

### Newsletter
- `POST /api/newsletter/subscribe` - Suscribir email al newsletter

### Sistema
- `GET /` - Información de la API
- `GET /health` - Health check del sistema

## 🔧 Configuración

### Variables de Entorno (.env)

```env
# API Settings
APP_NAME=Lumière Digital Library API
VERSION=1.0.0

# Server Settings
HOST=127.0.0.1
PORT=8080
RELOAD=true

# CORS Settings
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8080"]

# Database (futuro)
DATABASE_URL=sqlite:///./lumiere.db
```

## 🧪 Testing

### Ejecutar Tests
```bash
# Tests unitarios
pytest tests/unit/

# Tests de integración
pytest tests/integration/

# Coverage
pytest --cov=app --cov-report=html
```

### Estructura de Tests
```
tests/
├── unit/                 # Tests unitarios
│   ├── test_book_service.py
│   └── test_book_repository.py
├── integration/         # Tests de integración
│   └── test_api.py
└── fixtures/            # Datos de prueba
```

## 📊 Monitoreo

### Logs
- **Archivo**: `logs/lumiere.log`
- **Consola**: Output en tiempo real
- **Niveles**: DEBUG, INFO, WARNING, ERROR

### Health Checks
- **Endpoint**: `/health`
- **Métricas**: Estado de servicios, conteo de libros, versión

### Middleware de Logging
- Registra todas las requests HTTP
- Mide tiempo de respuesta
- Loguea errores automáticamente

## 🔄 Ciclo de Desarrollo

### Cambiar Implementación de Repositorio

```python
# En app/container.py
def book_repository(self) -> BookRepositoryPort:
    # Cambiar aquí entre implementaciones
    # return BookRepositoryMock()      # Desarrollo
    return BookRepositorySQL()         # Producción
    # return BookRepositoryMongo()     # Futuro
```

### Agregar Nuevo Servicio

1. **Crear entidad de dominio** en `app/domain/entities/`
2. **Definir puerto** en `app/ports/`
3. **Implementar adaptador** en `app/adapters/`
4. **Crear servicio** en `app/domain/services/`
5. **Registrar en contenedor** en `app/container.py`
6. **Crear router** en `app/routers/`

## 🚢 Despliegue

### Docker (Recomendado)
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

### Producción
```bash
# Usar variables de entorno de producción
export DATABASE_URL="postgresql://..."
export CORS_ORIGINS='["https://tu-dominio.com"]'

# Ejecutar con gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 🤝 Contribución

### Guías de Desarrollo
1. Seguir arquitectura hexagonal estrictamente
2. Tests para toda nueva funcionalidad
3. Documentación actualizada
4. Code review obligatorio

### Commits
```
feat: agregar búsqueda avanzada de libros
fix: corregir validación de email en newsletter
refactor: migrar a SQLAlchemy en repositorio
test: agregar tests de integración para API
```

## 📈 Roadmap

### Fase 2: Base de Datos Real
- [ ] SQLAlchemy + PostgreSQL
- [ ] Migraciones con Alembic
- [ ] Connection pooling

### Fase 3: Seguridad
- [ ] JWT Authentication
- [ ] Role-based access control
- [ ] API Key management

### Fase 4: Escalabilidad
- [ ] Redis caching
- [ ] Background jobs (Celery)
- [ ] API Gateway

### Fase 5: Observabilidad
- [ ] Métricas con Prometheus
- [ ] Tracing distribuido
- [ ] Alertas automáticas

---

## 📞 Soporte

Para preguntas o issues, crear un ticket en el repositorio del proyecto.

**Versión**: 1.0.0
**Última actualización**: 22 de marzo de 2026</content>
<parameter name="filePath">c:\Users\patri\Desktop\ejercicio libreria\README.md