import requests
import json


api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

response = requests.get(api_url)

if response.status_code == 200:

    data = json.loads(response.text)
    
   
    if len(data["list"]) == 4 * 8:  
        print("Test Case 1: PASSED")
    else:
        print("Test Case 1: FAILED")
    
    
    hours = [entry["dt"] for entry in data["list"]]
    if all(hours[i] < hours[i+1] for i in range(len(hours)-1)):
        print("Test Case 2: PASSED")
    else:
        print("Test Case 2: FAILED")
    
    
    for entry in data["list"]:
        temp_min = entry["main"]["temp_min"]
        temp_max = entry["main"]["temp_max"]
        if temp_min <= entry["main"]["temp"] <= temp_max:
            continue
        else:
            print("Test Case 3: FAILED")
            break
    else:
        print("Test Case 3: PASSED")
    
   
    for entry in data["list"]:
        if entry["weather"][0]["id"] == 500 and entry["weather"][0]["description"] == "light rain":
            continue
        else:
            print("Test Case 4: FAILED")
            break
    else:
        print("Test Case 4: PASSED")
    
    
    for entry in data["list"]:
        if entry["weather"][0]["id"] == 800 and entry["weather"][0]["description"] == "clear sky":
            continue
        else:
            print("Test Case 5: FAILED")
            break
    else:
        print("Test Case 5: PASSED")

else:
    print("API request failed with status code:", response.status_code)