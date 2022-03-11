"""
URLS Patterns & Examples:-

Flights from {city} to {other city}
Flights from {city} to {other airport}
Book Holidays from {city} to {other city}

Flights from {airport} to {other city}
Flights from {airport} to {other airport}
Book Holidays from {airport}  {to other city}

{airline-name} Flights from {city} to {other city}
{airline-name} from {city}
{airline-name} to {city}

base_url = "https://www.myeztrips.com/
listings = [cities, airports]
partial_urls = ["flights/flights", "holidays/book-holidays",
                "airlines/{airline-name}-flights", "{airline-name}]

for from_destination in listings:
    for to_destination in listings:
        for partial_url in partial_urls:
            url = f"{base_url}{partial_url}-from-{from_destination}-to-{to_destination}"


https://www.myeztrips.com/flights/flights-from-delhi-to-other-city
https://www.myeztrips.com/flights/flights-from-delhi-to-other-airport
https://www.myeztrips.com/holidays/book-holidays-from-delhi-to-other-city

https://www.myeztrips.com/flights/flights-from-a-p-hill-army-air-field-airport-to-other-city
https://www.myeztrips.com/flights/flights-from-a-p-hill-army-air-field-airport-to-other-airport
https://www.myeztrips.com/holidays/book-holidays-from-a-p-hill-army-air-field-airport-to-other-city

https://myeztrips.com/airlines/cheap-qatar-airways-flights-from-aachen-to-aachen
https://myeztrips.com/airlines/cheap-japan-airlines-flights-from-aachen
https://myeztrips.com/airlines/cheap-japan-airlines-flights-to-aachen

base_url_airlines = f"{base_url}airlines/"

for from_city in cities:
    for airline_name in airlines:
        for to_city in cities:
            url1 = f"{base_url_airlines}{airline_name}-flights-from-{from_city}-to-{to_city}"

        url2 = f"{base_url_airlines}{airline_name}-flights-from-{from_city}"
        url2 = f"{base_url_airlines}{airline_name}-flights-to-{from_city}"
"""
from csv import DictReader

from scrapy.spiders import Spider


class MyezTripsSpider(Spider):
    name = 'myez_trips_spider'
    file_no = 0
    url_counter = 0
    file_name_t = "sitemap/sitemap_{}.txt"
    file = open(file_name_t.format(file_no), "w")

    start_urls = [

        # Total Cities = 8433  &  # Total Airports = 9205
        "https://www.myeztrips.com/flights/flights-by-cities",
        "https://www.myeztrips.com/flights/flights-by-airports",
        "https://www.myeztrips.com/hotels/hotels-in-cities",
        "https://www.myeztrips.com/hotels/hotels-in-airports",
    ]

    def parse(self, response):
        # for e in response.css('.container.article-content .col-md-3 a::text').getall():
        #     yield {
        #         'name': ''.join(e.split(" to ")[1:]).strip()
        #     }
        listings = response.css('.col-md-3 a::attr(href)').getall()
        self.make_urls(listings)

    def make_urls(self, listings):
        for url in listings:
            if self.url_counter == 50000:
                self.url_counter = 0
                self.file_no += 1
                self.file = open(self.file_name_t.format(self.file_no), "w")

            self.url_counter += 1
            self.file.write('%s\n' % url)
