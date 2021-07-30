#Lista de dicionario
from typing import Dict, List

positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    "argentina": 1,
    "mexico": 34,
    "colombia": 45,
}

countries: List[Dict[str, str]] = [
    {
        "name": "Argentina",
        "people": "450000",
    },
    {
        "name": "México",
        "people": "9000000",
    },
    {
        "name": "Colombia",
        "people": "9999999999",
    }
]

#-----------------------------------------------------------------------------------
#Lista de diccionarios con llaves string y sus valores son tuplas
from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
    {
        "coord1": (1,2),
        "coord2": (3,5)
    },
    {
        "coord1": (0,1),
        "coord2": (2,5)
    }
]