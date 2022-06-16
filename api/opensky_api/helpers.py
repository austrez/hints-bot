# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import time
import random
import math

from . import api


ICAO_CODES = {
    'EGSS': 'London',
    'LTAI': 'Antalya',
    'EDDB': 'Berlin',
    'LFPO': 'Paris',
    'OMDB': 'Dubai',
    'ULLI': 'Saint Petersburg',
    'UUDD': 'Moscow',
    'URSS': 'Sochi',
    'CYTZ': 'Toronto',
    'LCLK': 'Larnaca'
}


def load_flights_history():
    icao_codes = list(ICAO_CODES.keys())
    icao_code = random.choice(icao_codes)

    begin = datetime.now() - timedelta(1)
    end = datetime.now()

    begin_unix = math.floor(time.mktime(begin.timetuple()))
    end_unix = math.floor(time.mktime(end.timetuple()))

    arrivals = api.get_airport_arrivals(
        icao_code, begin_unix, end_unix)[0:6]

    departures = api.get_airport_departures(
        icao_code, begin_unix, end_unix)[0:6]

    arrivals_info = ''
    departures_info = ''

    arrival_info = 'Plane from {icao_code} airport arrived at {date}\n\n'
    departure_info = 'Plane from {start_icao} airport departured at {start_date} and arrived to {end_icao} airport at {end_date}\n\n'

    for arrival in arrivals:
        date = datetime.utcfromtimestamp(
            arrival['lastSeen']).strftime('%Y-%m-%d %H:%M:%S')

        arrivals_info += arrival_info.format(
            icao_code=arrival['estDepartureAirport'],
            date=date
        )

    for departure in departures:
        start_date = datetime.utcfromtimestamp(
            arrival['firstSeen']).strftime('%Y-%m-%d %H:%M:%S')
        end_date = datetime.utcfromtimestamp(
            arrival['lastSeen']).strftime('%Y-%m-%d %H:%M:%S')

        departures_info += departure_info.format(
            start_icao=departure['estDepartureAirport'],
            start_date=start_date,
            end_icao=departure['estArrivalAirport'],
            end_date=end_date
        )

    city = ICAO_CODES[icao_code]

    history = f"""
    History of arrivals per 24 hour in {icao_code} airport, {city}:
        
    {arrivals_info}

    -------------------

    History of departures per 24 hour in {icao_code} airport, {city}:

    {departures_info}
    """
    return history
