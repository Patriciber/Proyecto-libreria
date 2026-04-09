from typing import List, Optional
from app.domain.entities.author import Author
from app.ports.repositories.author_repository import AuthorRepositoryPort

class AuthorRepositoryMock(AuthorRepositoryPort):
    """Implementación Mock del repositorio de autores con datos del CSV."""

    def __init__(self):
        self._authors = [
            Author(id=0, name="Manuel", last_name="Almedia", email="Manuel.Almeida@eoi.es", ip="ip_Manuel"),
            Author(id=1, name="Claiborne", last_name="Corsor", email="ccorsor0@scientificamerican.com", ip="33.89.79.27"),
            Author(id=2, name="Elyn", last_name="Brockie", email="ebrockie1@trellian.com", ip="96.246.96.43"),
            Author(id=3, name="Kati", last_name="Fradson", email="kfradson2@scribd.com", ip="27.117.206.5"),
            Author(id=4, name="Guy", last_name="Pettersen", email="gpettersen3@sogou.com", ip="178.32.181.200"),
            Author(id=5, name="Cordelia", last_name="Haney", email="chaney4@joomla.org", ip="198.24.177.205"),
            Author(id=6, name="Antonie", last_name="Ducarne", email="aducarne5@last.fm", ip="234.3.154.166"),
            Author(id=7, name="Ellynn", last_name="Murricanes", email="emurricanes6@twitpic.com", ip="12.185.210.107"),
            Author(id=8, name="Herc", last_name="Sheber", email="hsheber7@themeforest.net", ip="151.254.116.113"),
            Author(id=9, name="Jaquelyn", last_name="Hamprecht", email="jhamprecht8@businesswire.com", ip="230.200.115.7"),
            Author(id=10, name="Delmor", last_name="Smetoun", email="dsmetoun9@berkeley.edu", ip="60.80.67.167"),
            Author(id=11, name="Doria", last_name="Hurry", email="dhurrya@t.co", ip="200.55.91.94"),
            Author(id=12, name="Brendis", last_name="Cardinal", email="bcardinalb@parallels.com", ip="134.142.14.197"),
            Author(id=13, name="Rooney", last_name="Rosenzveig", email="rrosenzveigc@mlb.com", ip="246.127.254.118"),
            Author(id=14, name="Becca", last_name="Tadlow", email="btadlowd@hostgator.com", ip="163.100.215.174"),
            Author(id=15, name="Kit", last_name="McMeyler", email="kmcmeylere@walmart.com", ip="149.135.140.98"),
        ]

    async def get_all(self) -> List[Author]:
        return self._authors.copy()

    async def get_by_id(self, author_id: int) -> Optional[Author]:
        return next((a for a in self._authors if a.id == author_id), None)

    async def search_by_name(self, query: str) -> List[Author]:
        q = query.lower()
        return [a for a in self._authors if q in a.name.lower() or q in a.last_name.lower()]
