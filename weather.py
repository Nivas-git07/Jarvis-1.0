import requests
from datetime import datetime, timedelta

def get_weather(city, date_input=None):
    """
    date_input: Can be a keyword ('today', 'tomorrow', 'yesterday')
                or a specific date string format 'YYYY-MM-DD'.
                Defaults to 'today' if left empty.
    """
    # 1. Normalize textual input keywords into precise date strings
    if date_input is None:
        date_input = "today"
        
    date_str = date_input.lower().strip()
    today_dt = datetime.now()

    if date_str == "today":
        target_date = today_dt.strftime("%Y-%m-%d")
    elif date_str == "tomorrow":
        target_date = (today_dt + timedelta(days=1)).strftime("%Y-%m-%d")
    elif date_str == "yesterday":
        target_date = (today_dt - timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        # If it's not a keyword, assume the user passed a direct string like '2026-07-02'
        target_date = date_str

    try:
        # 2. Fetch coordinates
        geo = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        ).json()

        if "results" not in geo:
            return f"City '{city}' not found"

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        # 3. Request historical + forecast data parameters
        # Adding 'past_days=1' ensures 'yesterday' works seamlessly
        weather = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "daily": (
                    "weather_code,"
                    "temperature_2m_max,"
                    "temperature_2m_min,"
                    "precipitation_probability_max"
                ),
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "wind_speed_10m"
                ),
                "past_days": 1,
                "timezone": "auto"
            }
        ).json()

        # 4. Find where the converted date sits in the payload index
        dates_list = weather["daily"]["time"]
        
        if target_date not in dates_list:
            return f"Date '{date_input}' ({target_date}) is outside the available API window."
            
        day_index = dates_list.index(target_date)

        current = weather["current"]
        max_temp = weather["daily"]["temperature_2m_max"][day_index]
        min_temp = weather["daily"]["temperature_2m_min"][day_index]
        rain = weather["daily"]["precipitation_probability_max"][day_index]

        return {
            "city": city,
            "query_input": date_input,
            "resolved_date": target_date,
            "current_temp": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind": current["wind_speed_10m"],
            "max_temp": max_temp,
            "min_temp": min_temp,
            "rain_probability": rain
        }

    except Exception as e:
        return f"Execution error: {str(e)}"

