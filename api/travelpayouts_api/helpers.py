# -*- coding: utf-8 -*-
import random

from . import api


TRIPS = [
    {
        "departure_station_id": "2006004",
        "departure_station_name": "Москва Октябрьская",
        "arrival_station_id": "2004000",
        "arrival_station_name": "Санкт-Петербург"
    }, {
        "departure_station_id": "2010000",
        "departure_station_name": "Ярославль",
        "arrival_station_id": "2004000",
        "arrival_station_name": "Санкт-Петербург"
    }, {
        "departure_station_id": "2004572",
        "departure_station_name": "Удомля",
        "arrival_station_id": "2004000",
        "arrival_station_name": "Санкт-Петербург"
    }, {
        "departure_station_id": "2004600",
        "departure_station_name": "Тверь",
        "arrival_station_id": "2004000",
        "arrival_station_name": "Санкт-Петербург"
    }, {
        "departure_station_id": "2030100",
        "departure_station_name": "Тюмень",
        "arrival_station_id": "2004000",
        "arrival_station_name": "Санкт-Петербург"
    }, {
        "departure_station_id": "2010161",
        "departure_station_name": "Котлас",
        "arrival_station_id": "2004000",
        "arrival_station_name": "Санкт-Петербург"
    }, {
        "departure_station_id": "2004001",
        "departure_station_name": "Санкт-Петербург-Главн.",
        "arrival_station_id": "2020830",
        "arrival_station_name": "Арчеда"
    }, {
        "departure_station_id": "2004001",
        "departure_station_name": "Санкт-Петербург-Главн.",
        "arrival_station_id": "2020600",
        "arrival_station_name": "Астрахань"
    }, {
        "departure_station_id": "2004003",
        "departure_station_name": "Санкт-Петербург-Витеб.",
        "arrival_station_id": "2004710",
        "arrival_station_name": "Бабаево"
    }, {
        "departure_station_id": "2004003",
        "departure_station_name": "Санкт-Петербург-Витеб.",
        "arrival_station_id": "2004523",
        "arrival_station_name": "Ашево"
    }
]


def get_trips_schedule():
    trip = random.choice(TRIPS)

    departure_code = trip['departure_station_id']
    arrival_code = trip['arrival_station_id']

    response = api.get_trips_schedule(departure_code, arrival_code)

    if response == []:
        return "No dule info"

    trips = response["trips"]

    departure_dest = trip['departure_station_name']
    arrival_dest = trip['arrival_station_name']

    trips_info = ''
    trip_info = 'Train number {train_number} departures from {start_station} at {start_time} and arrives to {end_station} at {end_time}\n\n'

    for trip in trips:
        trips_info += trip_info.format(
            train_number=trip["trainNumber"],
            start_station=departure_dest,
            start_time=trip["departureTime"],
            end_station=arrival_dest,
            end_time=trip["arrivalTime"]
        )

    schedule = f"""
    Train schedule:
        
    {trips_info}
    """

    return schedule
