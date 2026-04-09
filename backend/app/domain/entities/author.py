from dataclasses import dataclass

@dataclass
class Author:
    """Entidad de dominio para representar un autor."""
    id: int
    name: str
    last_name: str
    email: str
    ip: str

    @property
    def full_name(self) -> str:
        return f"{self.name} {self.last_name}"
