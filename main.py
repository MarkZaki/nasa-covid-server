from flask import Flask, jsonify

from analysis.rate_of_change import rate_of_change
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

    @app.route("/covid/locations/<key>/<value>/")
    def covid_country_key(key, value):
        locations = fetch_locations()
        index_of_country = binary_search(locations, 0, len(locations) - 1, key, value)
        if index_of_country != -1:
            return fetch_country(str(locations[index_of_country]["id"]))
        return {"Error": "Country not found!"}

    @app.route("/covid/locations/<key>/<value>/roc/confirmed/")
    def covid_country_roc_confirmed(key, value):
        locations = fetch_locations()
        index_of_country = binary_search(locations, 0, len(locations) - 1, key, value)
        if index_of_country != -1:
            country =  fetch_country(str(locations[index_of_country]["id"]))
            roc = rate_of_change(country["location"]["timelines"]["confirmed"]["timeline"])
            return jsonify({"confirmed_roc": roc})
        return {"Error": "Country not found!"}

    @app.route("/covid/locations/<key>/<value>/roc/deaths/")
    def covid_country_roc_deaths(key, value):
        locations = fetch_locations()
        index_of_country = binary_search(locations, 0, len(locations) - 1, key, value)
        if index_of_country != -1:
            country = fetch_country(str(locations[index_of_country]["id"]))
            roc = rate_of_change(country["location"]["timelines"]["deaths"]["timeline"])
            return jsonify({"deaths_roc": roc})
        return {"Error": "Country not found!"}


if __name__ == '__main__':
    main()
    app.run(debug=True)
