from bs4 import BeautifulSoup
from requests import get
from datetime import date

locations = {
    'Half Moon Bay': 'https://www.tide-forecast.com/locations/Half-Moon-Bay-California/tides/latest',
    'Huntington Beach': 'https://www.tide-forecast.com/locations/Huntington-Beach/tides/latest',
    'Providence': 'https://www.tide-forecast.com/locations/Providence-Rhode-Island/tides/latest',
    'Wrightsville Beach': 'https://www.tide-forecast.com/locations/Wrightsville-Beach-North-Carolina/tides/latest',
}

columns = [{
    'name': 'Location',
    'width': 20
}, {
    'name': 'Time',
    'width': 10
}, {
    'name': 'Height',
    'width': 5
}]

separator = " "

header = ""
for col in columns:
    header += f"{col['name'].ljust(col['width'], separator)}"

print(f"Tide Information: {date.today().isoformat()}\n")
print(header)

for location, url in locations.items():
    raw_html = get(url).text
    html_content = BeautifulSoup(raw_html, 'lxml')

    table_rows = html_content.find(
        'table', class_='tide-day-tides').find_all('tr')
    low_tide_row = table_rows[3]
    row_cells = low_tide_row.find_all('td')

    time = row_cells[1].find('b').text.strip()
    height = row_cells[2].find(
        'b', class_='js-two-units-length-value__primary').text.strip()

    print(
        f"{location.ljust(columns[0]['width'], separator)}{time.ljust(columns[1]['width'], separator)}{height.ljust(columns[2]['width'], separator)}")
