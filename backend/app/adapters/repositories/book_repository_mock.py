from typing import List, Optional
from app.domain.entities.book import Book
from app.ports.repositories.book_repository import BookRepositoryPort

class BookRepositoryMock(BookRepositoryPort):
    """
    Adaptador mock del repositorio de libros con contenido realista y portadas profesionales.
    """

    def __init__(self):
        self._books = [
            Book(
                id=1, title="Horizonte Perdido", author="Elena Vargas",
                rating=4.8, pages=120, duration="12h 30m",
                category="ciencia_ficcion", price=0.0, is_premium=False,
                cover_style="mockup-1", icon="ri-planet-line",
                description="En el año 2142, la Tierra ya no es el hogar que conocíamos.",
                content="Prólogo: El Vacío Brillante. Las naves de carga cruzaban el cinturón de asteroides con la elegancia de ballenas plateadas. Elena miraba por la escotilla, sabiendo que el horizonte que conocía se había perdido para siempre. La atmósfera de Marte era roja y hostil, pero era el último refugio para una humanidad que ya no recordaba el olor a lluvia sobre tierra mojada...",
                is_favorite=False,
                cover="assets/scifi_cover.png"
            ),
            Book(
                id=2, title="Código Limpio", author="David Chen",
                rating=4.9, pages=464, duration="15h 10m",
                category="tecnologia", price=14.99, is_premium=True,
                cover_style="mockup-2", icon="ri-macbook-line",
                description="El código no es solo una arquitectura de lógica; es el lenguaje con el que moldeamos la realidad.",
                content="Introducción al Código Limpio. No basta con que el código funcione. El código debe ser legible, mantenible y elegante como una sinfonía de datos. En un mundo saturado de información, la elegancia de un sistema bien diseñado es la diferencia entre el progreso y el caos técnico. En este libro exploraremos los principios de S.O.L.I.D y cómo aplicarlos para salvar proyectos del abismo de la deuda técnica...",
                is_favorite=True,
                cover="assets/tech_cover.png"
            ),
            Book(
                id=3, title="Reino de Sombras", author="Marc Sterling",
                rating=4.5, pages=512, duration="18h 00m",
                category="fantasia", price=9.99, is_premium=False,
                cover_style="mockup-3", icon="ri-sword-line",
                description="Las runas en la superficie de la espada comenzaron a brillar con una luz gélida.",
                content="Las nubes sobre Celestyra eran de un color púrpura antinatural. El Rey de las Sombras no era una leyenda, estaba aquí, y su aliento de invierno eterno ya golpeaba las puertas del Reino. Marc empuñó su espada rúnica, sintiendo el peso de mil generaciones de guardianes que habían fallado antes de él. Esta noche, las sombras no reclamarían más almas...",
                is_favorite=False,
                cover="assets/fantasy_cover.png"
            ),
            Book(
                id=4, title="Amor Cuántico", author="Lucía M.",
                rating=4.6, pages=310, duration="10h 20m",
                category="romance", price=4.99, is_premium=False,
                cover_style="mockup-5", icon="ri-empathize-line",
                description="Dicen que el amor trasciende el tiempo y el espacio.",
                content="En el laboratorio de partículas, Lucía observaba el monitor de entrelazamiento. Dicen que el amor puede viajar entre universos paralelos para encontrar a su alma gemela, y hoy, por fin, la frecuencia de su corazón encontró respuesta en una dimensión que no debia existir. No era solo energía lo que se transfería; era una promesa grabada en los átomos desde el inicio del Big Bang...",
                is_favorite=False,
                cover="assets/romance_cover.png"
            ),
            Book(
                id=5, title="El Enigma del Sótano", author="R. K. Black",
                rating=4.4, pages=390, duration="11h 15m",
                category="misterio", price=0.0, is_premium=True,
                cover_style="mockup-1", icon="ri-search-eye-line",
                description="La mansión Blackwood siempre guardó secretos bajo el barniz de su opulencia.",
                content="La vieja mansión de los Blackwood guardaba un secreto bajo el suelo de roble. Una carta olvidada en el sótano reveló que el enigma de la familia era mucho más oscuro de lo que el inspector retirado imaginó cuando aceptó el caso por simple aburrimiento. El olor a papel antiguo y humedad le confirmó que algunas verdades jamás debieron ser desenterradas...",
                is_favorite=True,
                cover="assets/mystery_cover.png"
            ),
            Book(
                id=6, title="Misterio en la Ciudadela", author="Lena Torres",
                rating=4.6, pages=374, duration="13h 00m",
                category="misterio", price=5.99, is_premium=False,
                cover_style="mockup-5", icon="ri-search-eye-line",
                description="Un peligroso secreto emerge de las profundidades de una antigua citadela.",
                content="Las antorchas parpadeaban en los pasillos de piedra de la Ciudadela. Lena sabía que si llegaba al corazón de la estructura antes del amanecer, la verdad sobre la desaparición de los Ancianos saldría a la luz. Pero la Ciudadela tiene su propia voluntad, y los pasillos parecen moverse cada vez que susurra el viento entre las grietas de la muralla milenaria...",
                is_favorite=False,
                cover="assets/mystery_cover.png"
            ),
            Book(
                id=7, title="Fluoroscopy: El Arte de la Oscuridad", author="Claiborne Corsor",
                rating=4.7, pages=280, duration="9h 45m",
                category="terror", price=20.0, is_premium=True,
                cover_style="mockup-terror", icon="ri-skull-line",
                description="Un experimento médico que salió terriblemente mal en las profundidades de un hospital olvidado.",
                content="Prólogo: El Rayo que Ve. No era una luz común la que emanaba del antiguo fluoroscopio. Era un espectro que no mostraba huesos, sino los pecados tallados en el alma de los pacientes. Claiborne entró en la sala quirúrgica 404, donde el aire sabía a ozono y a desesperación rancia. El monitor parpadeó, mostrando algo que no tenía corazón, pero que latía con una hambre antigua. El rayo no iluminaba el cuerpo, iluminaba el miedo...",
                is_favorite=False,
                cover="assets/horror_demon.png"
            ),
            Book(
                id=8, title="Beam Radiation: El Despertar", author="Elyn Brockie",
                rating=4.3, pages=320, duration="11h 20m",
                category="terror", price=16.0, is_premium=False,
                cover_style="mockup-terror", icon="ri-magic-line",
                description="La radiación no solo quema la piel; a veces quema el velo entre nuestro mundo y el de las sombras.",
                content="Elyn sentía que el silbido de la máquina de tratamiento era en realidad un cántico en una lengua muerta. Cada sesión de radiación Beam no estaba atacando su enfermedad, estaba alimentando a la bruja que dormía en las células de su médula ósea. Cuando las luces del hospital se apagaron, ella finalmente pudo ver en la oscuridad total. Las sombras cobraron vida, susurrando secretos de poder que los médicos jamás podrían comprender...",
                is_favorite=False,
                cover=None
            ),
            Book(
                id=9, title="Patrones de Enmascaramiento", author="Kati Fradson",
                rating=4.5, pages=410, duration="14h 00m",
                category="terror", price=13.0, is_premium=False,
                cover_style="mockup-terror", icon="ri-ghost-line",
                description="En esta casa encantada, las paredes no hablan, pero las sombras ocultan rostros conocidos.",
                content="Kati descubrió que los patrones del papel tapiz de la mansión Fradson cambiaban cuando nadie los miraba. No eran flores ni arabescos; eran las máscaras de todos los que habían muerto en aquellas habitaciones, esperando el momento justo para desprenderse de las paredes y reclamar un nuevo rostro para su colección eterna. La casa no estaba vacía; estaba simplemente esperando a su próxima pieza decorativa...",
                is_favorite=False,
                cover=None
            ),
            Book(
                id=10, title="Revisión del Sujeto Z", author="Guy Pettersen",
                rating=4.2, pages=250, duration="8h 30m",
                category="terror", price=18.0, is_premium=True,
                cover_style="mockup-terror", icon="ri-hospital-line",
                description="Un diario médico que documenta la lenta transformación de un hombre en algo inhumano.",
                content="Día 43: El sujeto ya no reconoce el sabor de la comida normal. Solo el hierro de la sangre parece calmar el temblor de sus manos. Guy escribía con urgencia, sabiendo que las medidas de contención del laboratorio eran insuficientes para lo que el Sujeto Z se estaba convirtiendo: una fuerza de la naturaleza hambrienta y sin alma. La evolución no siempre es hacia arriba; a veces es un descenso al abismo del hambre pura...",
                is_favorite=False,
                cover=None
            ),
            Book(
                id=11, title="Válvulas del Infierno", author="Cordelia Haney",
                rating=4.4, pages=340, duration="12h 15m",
                category="terror", price=14.0, is_premium=False,
                cover_style="mockup-terror", icon="ri-heart-pulse-line",
                description="Un trasplante de corazón que trae consigo los recuerdos de un asesino de otra dimensión.",
                content="La válvula mitral palpitaba con un ritmo que no era el suyo. Cordelia podía escuchar el eco de gritos que no le pertenecían cada vez que su corazón latía. El donante no era humano, o al menos, no lo que nosotros llamamos humano. Las puertas del infierno se habían abierto en su propio pecho, y cada latido era un paso más hacia una realidad de la que no hay retorno posible...",
                is_favorite=False,
                cover=None
            ),
            Book(
                id=12, title="Fusión de Columnas: El Ritual", author="Antonie Ducarne",
                rating=4.6, pages=295, duration="10h 00m",
                category="terror", price=14.0, is_premium=False,
                cover_style="mockup-terror", icon="ri-node-tree",
                description="Un ritual prohibido que busca unir las almas de siete guerreros caídos en un solo cuerpo.",
                content="Antonie recitó las palabras finales mientras las columnas de piedra se fundían con el tejido de los voluntarios. No era solo cirugía; era una fusión de destinos que la historia había intentado olvidar. Cuando el último hueso encajó en su sitio, un grito unísono retumbó en la montaña, anunciando que el guardián de siete cabezas finalmente había despertado. La guerra de los dioses estaba a punto de reiniciarse...",
                is_favorite=False,
                cover=None
            ),
            Book(
                id=13, title="Radiografía del Alma", author="Ellynn Murricanes",
                rating=4.1, pages=180, duration="6h 30m",
                category="terror", price=11.0, is_premium=False,
                cover_style="mockup-terror", icon="ri-scan-line",
                description="Un fotógrafo forense captura algo en una placa de rayos X que no debería existir.",
                content="La placa mostraba una sombra nítida envuelta alrededor de la arteria carótida del cadáver. No era un tumor ni un coágulo. Temía dedos. Ellynn apagó la luz del laboratorio, asustada, pero la imagen seguía brillando en su retina con una intensidad gélida. Alguien, o algo, se alimentaba de la sangre de los muertos antes de que llegaran a la morgue. Y ahora, ese algo sabía que ella lo había visto...",
                is_favorite=False,
                cover=None
            ),
            Book(
                id=14, title="Bypass al Abismo", author="Herc Sheber",
                rating=4.8, pages=350, duration="13h 40m",
                category="terror", price=19.0, is_premium=True,
                cover_style="mockup-terror", icon="ri-flow-chart",
                description="En el espacio profundo, un bypass de energía abre un portal hacia una dimensión desconocida.",
                content="Herc sabía que desviar el flujo de la vena renal principal a través del motor warp era una locura. Pero la nave estaba rodeada. Cuando la energía cruzó el umbral, el espacio se rasgó como seda vieja, revelando un color que no debería existir y unas voces que llamaban por su nombre desde el otro lado de la eternidad. El abismo no estaba vacío; estaba lleno de ojos que no parpadean...",
                is_favorite=True,
                cover=None
            ),
            Book(
                id=15, title="Inserción en el Pericardio", author="Jaquelyn Hamprecht",
                rating=4.3, pages=420, duration="15h 20m",
                category="terror", price=15.0, is_premium=False,
                cover_style="mockup-terror", icon="ri-pulse-line",
                description="Un thriller psicológico donde un cirujano implanta micrófonos en los corazones de sus víctimas.",
                content="Jaquelyn podía escuchar cada suspiro, cada mentira, cada secreto susurrado por el corazón de sus pacientes. No buscaba curarlos; buscaba la partitura perfecta de la traición humana. Pero hoy, su último 'instrumento' comenzó a emitir una señal que ella misma no había programado. Un latido rítmico que deletreaba su propio nombre en código Morse...",
                is_favorite=False,
                cover=None
            ),
            Book(
                id=16, title="La Excisión del Limo", author="Delmor Smetoun",
                rating=4.0, pages=310, duration="10h 10m",
                category="terror", price=13.0, is_premium=False,
                cover_style="mockup-terror", icon="ri-microscope-line",
                description="Una expedición científica en busca de una cura que se convierte en una pesadilla biológica.",
                content="El limo del Amazonas no era una bacteria común. Era una voluntad colectiva que se filtraba en el timo, reprogramando el sistema inmune para que considerara a la propia conciencia como un patógeno. Delmor veía cómo sus colegas empezaban a mirarse con extrañeza, como si estuvieran esperando la orden de su nuevo y viscoso dios. La cura no era para el cuerpo; era para la individualidad...",
                is_favorite=False,
                cover=None
            ),
            Book(
                id=17, title="Aféresis de Sombras", author="Doria Hurry",
                rating=4.7, pages=260, duration="9h 00m",
                category="terror", price=13.0, is_premium=False,
                cover_style="mockup-terror", icon="ri-filter-line",
                description="Un proceso de purificación de sangre que acaba extrayendo la propia alma.",
                content="La máquina separaba los leucocitos con una precisión quirúrgica, pero lo que se acumulaba en la bolsa de retorno era una oscuridad líquida que Doria no recordaba haber visto en los libros de hematología. Con cada ciclo, el paciente se volvía más pálido, más silencioso, hasta que lo único que quedó en la camilla fue un traje vacío y un suspiro de terror que flotaba en el aire estéril de la clínica...",
                is_favorite=False,
                cover=None
            )
        ]

    async def get_all_books(self) -> List[Book]:
        return self._books.copy()

    async def get_books_by_category(self, category: str) -> List[Book]:
        return [book for book in self._books if book.category == category]

    async def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return next((book for book in self._books if book.id == book_id), None)

    async def search_books(self, query: str) -> List[Book]:
        query_lower = query.lower()
        return [
            book for book in self._books
            if (query_lower in book.title.lower() or
                query_lower in book.author.lower() or
                query_lower in book.description.lower() or
                query_lower in book.content.lower())
        ]

    async def get_featured_books(self, limit: int = 3) -> List[Book]:
        sorted_books = sorted(self._books, key=lambda x: x.rating, reverse=True)
        return sorted_books[:limit]