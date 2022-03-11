"""
URLS Patterns & Examples:-

Flights from {city} to {other city}
Flights from {city} to {other airport}
Book Holidays from {city} to {other city}


Flights from {airport} to {other city}
Flights from {airport} to {other airport}
Book Holidays from {airport}  {to other city}

{airline-name} Flights from {from_destination} to {other city}
{airline-name} from {city}
{airline-name} to {city}

{airways-name} Flights from {from_destination} to {other city}
{airways-name} from {city}
{airways-name} to {city}

{airport-name} Flights from {from_destination} to {other city}
{airport-name} Flights from {city}
{airport-name} Flights to {city}

# {city} flights from {city} to {other-cities}


https://www.myeztrips.com/flights/flights-from-delhi-to-other-city
https://www.myeztrips.com/flights/flights-from-delhi-to-other-airport
https://www.myeztrips.com/holidays/book-holidays-from-delhi-to-other-city

https://www.myeztrips.com/flights/flights-from-a-p-hill-army-air-field-airport-to-other-city
https://www.myeztrips.com/flights/flights-from-a-p-hill-army-air-field-airport-to-other-airport
https://www.myeztrips.com/holidays/book-holidays-from-a-p-hill-army-air-field-airport-to-other-city

https://myeztrips.com/airlines/cheap-qatar-airways-flights-from-aachen-to-aachen
https://myeztrips.com/airlines/cheap-japan-airlines-flights-from-aachen
https://myeztrips.com/airlines/cheap-japan-airlines-flights-to-aachen

https://myeztrips.com/airlines/cheap-aachen-airways-flights-from-other-cities-to-other-cities
https://myeztrips.com/airlines/cheap-aachen-airlines-flights-from-other-cities-to-other-cities
https://myeztrips.com/airlines/cheap-aachen-airports-flights-from-aachen-to-other-cities
https://myeztrips.com/airlines/cheap-aachen-flights-from-other-cities-to-other-cities

https://myeztrips.com/airlines/cheap-aachen-airlines-flights
https://myeztrips.com/airlines/cheap-aachen-airways-flights
https://myeztrips.com/airlines/cheap-aachen-flights

https://myeztrips.com/airlines/cheap-aachen-airlines-flights-from-aachen
https://myeztrips.com/airlines/cheap-aachen-airways-flights-from-aachen
https://myeztrips.com/airlines/cheap-aachen-flights-from-aachen

"""

from csv import DictReader


class CreateUrlFiles:
    file_no = 1
    url_counter = 0

    file_name_t = "sitemap/sitemap_{}.txt"

    file = open(file_name_t.format(file_no), "w")

    def generate_urls(self):
        base_url = "https://www.myeztrips.com/"
        base_url_airlines = f"{base_url}airlines/"

        cities = self.get_listing("cities")
        airports = self.get_listing("airports")

        for from_destination in cities + airports:
            for i, destinations in enumerate([cities, airports]):
                for to_destination in destinations:
                    url = f"{base_url}flights/flights-from-{from_destination}-to-{to_destination}"
                    self.write_url(url)

                    # avoid making urls like book-holiday-days-from-{from_destination}-to-{airport}
                    if i > 0:
                        continue
                    hd_url = f"{base_url}holidays/book-holidays-from-{from_destination}-to-{to_destination}"
                    self.write_url(hd_url)

        for from_city in cities:
            for to_city in cities:
                for combination in ['airlines', 'airways', 'airports']:
                    url = f"{base_url_airlines}cheap-{from_city}-{combination}-flights-from-{from_city}-to-{to_city}"
                    url2 = f"{base_url_airlines}cheap-{from_city}-{combination}-flights-from-{to_city}"
                    url3 = f"{base_url_airlines}cheap-{from_city}-{combination}-flights-to-{to_city}"

                    self.write_url(url)
                    self.write_url(url2)
                    self.write_url(url3)

                url = f"{base_url_airlines}cheap-{from_city}-flights-from-{from_city}-to-{to_city}"
                url2 = f"{base_url_airlines}cheap-{from_city}-flights-from-{to_city}"
                url3 = f"{base_url_airlines}cheap-{from_city}-flights-to-{to_city}"

                self.write_url(url)
                self.write_url(url2)
                self.write_url(url3)

    def write_url(self, url):
        if self.url_counter == 50000:
            self.url_counter = 0
            self.file_no += 1
            self.file = open(self.file_name_t.format(self.file_no), "w")

        self.url_counter += 1
        self.file.write('%s\n' % url)

    def get_listing(self, file_name):
        return [r['name'].replace(' ', '-').lower().strip() for r
                in DictReader(open(f"{file_name}.csv")) if r['name'].strip()]


CreateUrlFiles().generate_urls()
