import json

with open('hotels.json', 'r') as f:
    data = json.load(f)

hotelName = ""

for x in range(1):
    print(f"Hotel name: {data["properties"][x]["name"]}")
    hotelName = data["properties"][x]["name"]
    print()
    print(f"link name: {data["properties"][x]["link"]}")
    print()
    print(f"latitude name: {data["properties"][x]["gps_coordinates"]["latitude"]}")
    print()
    print(f"longitude name: {data["properties"][x]["gps_coordinates"]["longitude"]}")

HotelHtml = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Hotel Info</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background: #f4f4f4;
    display: flex;
    justify-content: center;
    padding-top: 60px;
  }

  .hotel-card {
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    padding: 20px 30px;
    width: 300px;
    text-align: center;
  }

  .hotel-card h2 {
    margin: 0 0 10px;
    font-size: 1.3em;
  }

  .hotel-card a {
    color: #0066cc;
    text-decoration: none;
    font-weight: bold;
  }

  .hotel-card a:hover {
    text-decoration: underline;
  }

  .coords {
    margin-top: 12px;
    font-size: 0.9em;
    color: #555;
  }
</style>
</head>
<body>

<div class="hotel-card">
  <h2>""" + hotelName + """</h2>
  <a href="https://example.com/hotel-page" target="_blank">View Hotel Page</a>
  <div class="coords">
    <p>Latitude: 39.9612</p>
    <p>Longitude: -82.9988</p>
  </div>
</div>

</body>
</html>"""
    
with open("hotelFront.html", "w", encoding="utf-8") as file:
    file.write(HotelHtml)

""""
client = serpapi.Client(api_key="3b8aa096c0bb4807037fce9ee1a406ae1c5bf16613564770c98093d5862fe07b")
results = client.search({
  "engine": "google_hotels",
  "q": "Bali Resorts",
  "check_in_date": "2026-09-18",
  "check_out_date": "2026-09-19"
})
"""

