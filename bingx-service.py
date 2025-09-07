import requests
from config import API_KEY

BASE_URL = "https://open-api.bingx.com"

def send_get_request():
    url = f"{BASE_URL}/openApi/spot/v1/common/symbols"
    headers = {
        "X-BX-APIKEY": API_KEY
    }
    response = requests.get(url, headers=headers)

    # Raise exception if request failed
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    try:
        symbols = send_get_request()
        print("✅ BingX Spot Symbols:")
        print(symbols)
    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)