import bcrypt
# Parche de compatibilidad
if not hasattr(bcrypt, "__about__"):
    bcrypt.__about__ = type('about', (object,), {'__version__': bcrypt.__version__})

from passlib.context import CryptContext

try:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    h = pwd_context.hash("admin123")
    print(f"Hash created: {h}")
    res = pwd_context.verify("admin123", h)
    print(f"Verify result: {res}")
except Exception as e:
    print(f"Error: {e}")
