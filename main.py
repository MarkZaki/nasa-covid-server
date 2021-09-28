from flask import Flask, jsonify
from constants import *
from controllers.locations import fetch_locations, fetch_country
from lib.http import HttpGetRequest
from lib.search import binary_search

app = Flask(__name__)


def main():

    @app.route("/covid/all/")
    def covid_all():
        http = HttpGetRequest(COVID_URL)
        data = http.get("/")
        return jsonify(data["latest"])

    @app.route("/covid/locations/")
    def covid_locations():
        return jsonify(fetch_locations())

    @app.route("/covid/locations/id/<country_id>/")
    def covid_country_id(country_id):
        return fetch_country(country_id)

    @app.route("/covid/locations/name/<country_name>/")
    def covid_country_name(country_name):
        locations = fetch_locations()
        index_of_country = binary_search(locations, 0, len(locations) - 1, "country", country_name)
        if index_of_country == -1:
            return {"Error": "Country not found!"}
        return fetch_country(str(locations[index_of_country]["id"]))

    @app.route("/covid/locations/code/<country_code>/")
    def covid_country_code(country_code):
        locations = fetch_locations()
        index_of_country = binary_search(locations, 0, len(locations) - 1, "country_code", country_code)
        if index_of_country == -1:
            return {"Error": "Country not found!"}
        return fetch_country(str(locations[index_of_country]["id"]))


if __name__ == '__main__':
    main()
    app.run(debug=True)
