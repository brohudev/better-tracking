import math
import requests
import os
import datetime

#set these to four digits after decimal. 
antenna_lat = 29.6204  #  degrees
antenna_lon = -99.5289  # degrees
antenna_alt = 425  # meters
modem_name = "MRSU001" 


def get_iridium_data(modem):
    try:
        session = requests.Session()

        url = f"https://borealis.rci.montana.edu/api/meta/flights?modem_name={modem}"
        req = session.get(url)
        req.raise_for_status()
        latest_flight = req.json()[-1]

        uid = latest_flight["uid"]

        url = f"https://borealis.rci.montana.edu/api/flight?uid={uid}"
        req = session.get(url)
        req.raise_for_status()
        data = req.json()

        fields = data["fields"]
        values = data["data"]

        entry = values[0]

        timestamp = datetime.datetime.fromtimestamp(entry[fields.index("datetime")]).strftime("%Y%m%d%H%M%S")
        lat = entry[fields.index("latitude")]
        lon = entry[fields.index("longitude")]
        alt = entry[fields.index("altitude")]

        return timestamp, lat, lon, alt

    except requests.exceptions.RequestException as e:
        print("Error occurred during request:", e)
        return None

def store_iridium_data(data):
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

def calculate_elevation(alt_ant, alt_bal, straight_line_distance):
    height = abs(alt_bal - alt_ant)

    angle = math.atan(height / straight_line_distance)

    angle_degrees = math.degrees(angle)

    return angle_degrees

def calculate_distance(lat_ant, lon_ant, alt_ant, lat_bal, lon_bal, alt_bal):
    lat_ant_rad = math.radians(lat_ant)
    lon_ant_rad = math.radians(lon_ant)
    lat_bal_rad = math.radians(lat_bal)
    lon_bal_rad = math.radians(lon_bal)

    R_meters = 6371000

    alt_ant_meters = alt_ant
    alt_bal_meters = alt_bal

    x_ant = (R_meters + alt_ant_meters) * math.cos(lat_ant_rad) * math.cos(lon_ant_rad)
    y_ant = (R_meters + alt_ant_meters) * math.cos(lat_ant_rad) * math.sin(lon_ant_rad)
    z_ant = (R_meters + alt_ant_meters) * math.sin(lat_ant_rad)

    x_bal = (R_meters + alt_bal_meters) * math.cos(lat_bal_rad) * math.cos(lon_bal_rad)
    y_bal = (R_meters + alt_bal_meters) * math.cos(lat_bal_rad) * math.sin(lon_bal_rad)
    z_bal = (R_meters + alt_bal_meters) * math.sin(lat_bal_rad)

    dx = x_bal - x_ant
    dy = y_bal - y_ant
    dz = z_bal - z_ant

    distance_meters = math.sqrt(dx**2 + dy**2 + dz**2)

    return distance_meters

# returns azimuth, elevation in that order for the ground station to correctly 
def calculate_orientation():
    iridium_data = get_iridium_data(modem_name)

    if iridium_data is not None:
        balloon_lat, balloon_lon, balloon_alt = iridium_data[1:]  # Extracting latitude, longitude, and altitude
        print("Balloon position updated using Iridium data:")
        print("Latitude:", balloon_lat)
        print("Longitude:", balloon_lon)
        print("Altitude:", balloon_alt)
    else:
        print("Failed to fetch Iridium data. Balloon position remains unchanged.")


    azimuth = calculate_azimuth(math.radians(antenna_lat), math.radians(antenna_lon),math.radians(balloon_lat), math.radians(balloon_lon))
    straight_line_distance = calculate_distance(antenna_lat, antenna_lon, antenna_alt, balloon_lat, balloon_lon, balloon_alt)
    elevation = calculate_elevation(antenna_alt, balloon_alt, straight_line_distance)

    azimuth = round(azimuth, 2)
    elevation = round(elevation, 2)

    print("New Azimuth angle for GS:", azimuth)
    print("New Elevation angle for GS:", elevation)
    print("Straight line distance between the two in meters: ", straight_line_distance)
    
    return azimuth, elevation
