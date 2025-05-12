import requests

class TradeAPI:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url

    def search_trades(self, account_id: int, start_timestamp: str, end_timestamp: str = None):
        url = f"{self.base_url}/api/Trade/search"
        headers = {
            "accept": "text/plain",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        payload = {
            "accountId": account_id,
            "startTimestamp": start_timestamp
        }
        if end_timestamp:
            payload["endTimestamp"] = end_timestamp

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and data.get("errorCode") == 0:
                return data.get("trades", [])
            else:
                raise Exception(f"API Error: {data.get('errorMessage')}")
        else:
            raise Exception(f"HTTP Error: {response.status_code} {response.text}")