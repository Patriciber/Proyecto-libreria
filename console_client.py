import requests

API_URL = "http://127.0.0.1:8080/api/books"

def main():
    print("================================")
    print("      LUMIÈRE CLI CLIENTE")
    print("================================")
    
    try:
        # Hacemos una petición real al backend en lugar de usar datos simulados
        response = requests.get(API_URL)
        response.raise_for_status()
        books = response.json()
        
        print(f"\n¡Conexión Exitosa! Se encontraron {len(books)} libros en la biblioteca.\n")
        
        for book in books:
            precio_texto = "Gratis" if book['price'] == 0 else f"${book['price']}"
            categoria = book['category'].replace('_', ' ').title()
            
            print(f"[{book['id']}] {book['title']} ")
            print(f"    Autor: {book['author']}")
            print(f"    Categoría: {categoria}")
            print(f"    Puntuación: {book['rating']} estrellas")
            print(f"    Precio: {precio_texto}")
            print("-" * 30)
            
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar a la API local.")
        print("Asegúrate de ejecutar el backend primero con: uvicorn main:app --port 8080")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
