from decimal import Decimal

from geopy.distance import geodesic


def calculate_distance(coordenate_origin: tuple, coordenate_destination: tuple) -> Decimal | int:
    
    return geodesic(coordenate_origin, coordenate_destination).km


#punto_a).km
    