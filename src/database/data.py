from ast import Dict
from typing import Optional





# def get_local_names(lat: float, lon: float) -> Optional[Dict[str, str]]:
#     """
#     Gets local city names by their latitude (lat) and longitude (lon),
#     returning only Ukrainian (uk) and English (en) names.

#     :param lat: Latitude of the place
#     :param lon: Longitude of the place
#     :return: Dictionary with local city names or None if the query fails
#     """
#     response = requests.get(open_weather_url(lat, lon), params={"lat": lat, "lon": lon})

#     if response.status_code == 200:
#         data = response.json()
#         if data and isinstance(data, list) and "local_names" in data[0]:
#             local_names = data[0]["local_names"]
#             return {key: local_names[key] for key in ("uk", "en") if key in local_names}

#     print(f"Request error: {response.status_code}")
#     return None

# def get_cities_data():
#     for city in cities_data:
#         local_names = get_local_names(city["lat"], city["lon"])

#         if local_names:
#             city["name_uk"] = local_names.get("uk", None)
#             city["name_en"] = local_names.get("en", None)
#         else:
#             city["name_uk"] = None
#             city["name_en"] = None
#         time.sleep(1)
#         return cities_data

# cities_list = get_cities_data()
# print(cities_list)
