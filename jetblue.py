#!/usr/bin/env python3
import json
from urllib.request import urlopen, Request
from urllib.error import HTTPError

APIKEY = "49fc015f1ba44abf892d2b8961612378"


def fetch_flight_status(date, number):
    # https://az-api.jetblue.com/flight-status/get-by-number?date=2022-11-08&number=1974
    url = f"https://az-api.jetblue.com/flight-status/get-by-number?date={date}&number={number}"
    headers = {"apikey": APIKEY}
    req = Request(url, headers=headers)
    try:
        return json.load(urlopen(req))
    except HTTPError as ex:
        print("HTTPError %s" % ex.code)
        return json.load(ex)


def main():
    number = 1974
    date = "2022-11-08"
    resp = fetch_flight_status(date, number)
    print(resp)


if __name__ == "__main__":
    main()
