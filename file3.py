import json
import csv
from datetime import datetime,timezone
import requests
import time


city_names = [
    "New York","Nairobi","London","Tokyo","Sydney","Paris","Berlin","Moscow","Cairo","Cape Town",
    "Rio de Janeiro","Buenos Aires","Mexico City","Los Angeles","Toronto","Vancouver","Santiago","Lima",
    "Bogota","Caracas","Sao Paulo","Lisbon","Madrid","Rome","Athens","Istanbul","Dubai","Mumbai","Karachi",
    "Kinsasha","Lagos","Addis Ababa","Cairo","Istanbul","Moscow","Beijing","Shanghai","Tokyo"
]

base_url = "https://api.openweathermap.org/data/2.5/weather?q="
