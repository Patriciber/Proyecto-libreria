from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.author import Author

class AuthorRepositoryPort(ABC):
    """Puerto de salida para la persistencia de autores."""

    @abstractmethod
    async def get_all(self) -> List[Author]:
        pass

    @abstractmethod
    async def get_by_id(self, author_id: int) -> Optional[Author]:
        pass

    @abstractmethod
    async def search_by_name(self, query: str) -> List[Author]:
        pass
