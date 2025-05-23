import requests
import csv

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

headers = {
	"x-rapidapi-key": "4a9f1afa00mshe6f72c2b4428af6p15f789jsn839d5637bfb6",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

querystring = {"formatType":"odi"}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json().get('rank', [])  # Extracting the 'rank' data
    csv_filename = 'batsmen_rankings.csv'

    if data:
        field_names = ['rank', 'name', 'country']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            #writer.writeheader()
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})

        print(f"Data fetched successfully and written to '{csv_filename}'")
    else:
        print("No data available from the API.")

else:
    print("Failed to fetch data:", response.status_code)