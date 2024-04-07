import math
import requests
import os
import csv
import datetime

class ClassIridium:
    def __init__(self):
        self.BaseURL = "https://borealis.rci.montana.edu"
        self.Session = requests.Session()
        self.Lat = 0
        self.Lon = 0
        self.Alt = 0
        self.Timestamp = None

    def get_iridium_data(self, modem):
        try:
            URL = "{}/api/meta/flights?modem_name={}".format(self.BaseURL, modem)
            req = self.Session.get(URL)
            req.raise_for_status()
            latest_flight = req.json()[-1]

            UID = latest_flight["uid"]

            URL = "{}/api/flight?uid={}".format(self.BaseURL, UID)
            req = self.Session.get(URL)
            req.raise_for_status()
            data = req.json()

            fields = data["fields"]
            values = data["data"]

            entry = values[0]

            self.Timestamp = datetime.datetime.fromtimestamp(entry[fields.index("datetime")]).strftime("%Y%m%d%H%M%S")
            self.Lat = entry[fields.index("latitude")]
            self.Lon = entry[fields.index("longitude")]
            self.Alt = entry[fields.index("altitude")]

            return self.Timestamp, self.Lat, self.Lon, self.Alt

        except requests.exceptions.RequestException as e:
            print("Error occurred during request:", e)
            return None

    def store_iridium_data(self, data):
        if data is not None:
            timestamp, lat, lon, alt = data
            directory = os.path.join(os.getcwd(), "Data", "LogIridium")
            os.makedirs(directory, exist_ok=True)

            date_string = datetime.datetime.now().strftime("%Y%m%d")
            file_name = f"Iridium_{date_string}.csv"
            file_path = os.path.join(directory, file_name)

            with open(file_path, "a", newline='\n') as f:
                sentence = f"Timestamp: {timestamp}, Latitude: {lat}, Longitude: {lon}, Altitude: {alt}\n"
                f.write(sentence)

def calculate_azimuth(lat_ant, lon_ant, lat_bal, lon_bal):
    d_lon = lon_bal - lon_ant
    y = math.sin(d_lon) * math.cos(lat_bal)
    x = math.cos(lat_ant) * math.sin(lat_bal) - math.sin(lat_ant) * math.cos(lat_bal) * math.cos(d_lon)
    azimuth = math.atan2(y, x)
    return (math.degrees(azimuth) + 360) % 360  # Convert radians to degrees and normalize to [0, 360] range

def calculate_elevation(lat_ant, lon_ant, alt_ant, lat_bal, lon_bal, alt_bal):
    R = 6371000  # Earth's radius in meters
    d_lat = math.radians(lat_bal - lat_ant)
    d_lon = math.radians(lon_bal - lon_ant)
    a = math.sin(d_lat / 2) * math.sin(d_lat / 2) + math.cos(math.radians(lat_ant)) * math.cos(math.radians(lat_bal)) * math.sin(d_lon / 2) * math.sin(d_lon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    altitude_diff = alt_bal - alt_ant
    elevation = math.atan2(altitude_diff, distance)

    return math.degrees(elevation)

# Antenna position details
antenna_lat = 29.6204  # Latitude in degrees
antenna_lon = -99.5289  # Longitude in degrees
antenna_alt = 430  # Altitude converted from feet to meters

# Example usage:
InstanceIridium = ClassIridium()
modem_name = "MRSU001" 
iridium_data = InstanceIridium.get_iridium_data(modem_name)

if iridium_data is not None:
    balloon_lat, balloon_lon, balloon_alt = iridium_data[1:]  # Extracting latitude, longitude, and altitude
    print("Balloon position updated using Iridium data:")
    print("Latitude:", balloon_lat)
    print("Longitude:", balloon_lon)
    print("Altitude:", balloon_alt)
else:
    print("Failed to fetch Iridium data. Balloon position remains unchanged.")


azimuth = calculate_azimuth(math.radians(antenna_lat), math.radians(antenna_lon),
                            math.radians(balloon_lat), math.radians(balloon_lon))
elevation = calculate_elevation(math.radians(antenna_lat), math.radians(antenna_lon), antenna_alt, math.radians(balloon_lat), math.radians(balloon_lon), balloon_alt)

print("Azimuth angle:", azimuth)
print("Elevation angle:", elevation)

# lat 29.6204 long -99.5289 alt 430