import csv
import json
import requests

"""
This program retrieves data from the Electric Power Board (EPB)'s Power Outage and Restore map.
Link: https://epb.com/outage-and-storm-center/energy-outages/

The location of each outage and restore retrieved on each run is written to an outage and restore CSV,
respectively. This data will then be used in conjunction with other emergency- and service-related data
to track the (potential) effects of the snowstorm in the Chattanooga, TN area on January 10, 2025.
"""

"""
Retrieves the outages from the webpage and writes their data to outages.csv.
"""
def get_outages():   
    # Grab the JSON data
    r = requests.get(url="https://api.epb.com/web/api/v1/outages/power/incidents")

    # Convert to dictionary
    data = json.loads(r.content)

    # "data" is a Dict with keys "district_metrics", "outage_points", and "summary"

    # Add each outage from data["outage_points"] to the "outages" List
    outages = []
    for outage in data["outage_points"]:
        outages.append(outage)

    # Write to CSV
    fieldnames = ["crew_qty", "customer_qty", "incident_status", "latitude", "longitude"]
    with open("outages.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(outages)


"""
Retrieves the restores from the webpage and writes their data to restores.csv.
"""
def get_restores():
    # Grab the JSON data
    r = requests.get(url="https://api.epb.com/web/api/v1/outages/power/restores")

    # Convert to dictionary
    data = json.loads(r.content)

    # "data" is a Dict with keys "district_metrics", "restore_points", "summary", and "timespan_label"

    # Add each restore from data["restore_points"] to the "restores" List
    restores = []
    for restore in data["restore_points"]:
        restores.append(restore)

    # Write to CSV
    fieldnames = ["customer_qty", "incident_status", "latitude", "longitude"]
    with open("restores.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(restores)


get_outages()
get_restores()