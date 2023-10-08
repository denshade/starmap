import csv
import math
import re
import os


def write_coordinates_to_csv(filename, coordinates):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y', 'z'])  # Write the header row

        for x, y, z in coordinates:
            writer.writerow([x, y, z])

def pad(s):
    c = s.lstrip('0')
    if len(c) == 0 or c == "00.0":
        return 0
    return c
def convert_right_inclination_to_degrees(right_inclination):
    components = re.findall(r'[0-9]+(?:\.[0-9]+)?', right_inclination)
    try:
        hours = int(pad(components[0]))  # Extract the numeric part of hours and convert it to an integer
        minutes = int(pad(components[1]))  # Extract the numeric part of minutes and convert it to an integer
        seconds = float(pad(components[2]))  # Extract the numeric part of seconds and convert it to a float
    except:
        raise Exception(right_inclination)
    # Convert each component to degrees
    hours_deg = hours * 15
    minutes_deg = minutes * 0.25
    seconds_deg = seconds * 0.0041667

    # Sum up the degrees from all components
    total_degrees = hours_deg + minutes_deg + seconds_deg

    return total_degrees



def convert_to_degrees(angle):
    components = re.findall(r'-?\d+(?:\.\d+)?', angle)

    degrees = int(components[0])
    minutes = int(components[1])
    seconds = float(components[2])

    total_degrees = degrees + (minutes / 60) + (seconds / 3600)

    return total_degrees


def convert_to_3d_coordinates(right_ascension, inclination, distance):
    # Convert angles from degrees to radians
    ra_rad = math.radians(right_ascension)
    inc_rad = math.radians(inclination)
    if "," in distance:
        distance = distance.replace(",", ".")
    distance = float(distance)
    # Calculate the 3D coordinates
    x = distance * math.cos(ra_rad) * math.cos(inc_rad)
    y = distance * math.sin(ra_rad) * math.cos(inc_rad)
    z = distance * math.sin(inc_rad)

    return x, y, z


coordinates = []


def process_file(csv_file="stars_and.csv", sep=','):
    with open(csv_file, 'r', encoding="ISO-8859-1") as file:
        # Create a CSV reader
        reader = csv.reader(file, delimiter=sep)

        # Read the CSV data row by row
        for row in reader:
            if (row[0].lower() == "name"):
                continue
            # Access the data elements in each row
            # row[0] corresponds to the first column, row[1] to the second column, and so on
            name = row[0]
            if name == "":
                continue
            if len(row) < 3:
                print(f"incorrect row {row}")
            ra = convert_right_inclination_to_degrees(row[1])
            inclination = convert_to_degrees(row[2])
            ly = row[3]
            if ly == "":
                continue
            x, y, z = convert_to_3d_coordinates(ra, inclination, ly)
            #print(f"{x},{y},{z}")
            coordinates.append((x, y, z))


# Open the CSV file

file_list = os.listdir(".")

# Loop over the files that start with 'stars'
for filename in file_list:
    if filename.startswith("stars"):
        print(filename)
        process_file(filename)

write_coordinates_to_csv("objects.csv", coordinates)
