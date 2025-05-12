import requests

class HistoryAPI:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url

    def retrieve_bars(
        self,
        contract_id: str,
        live: bool,
        start_time: str,
        end_time: str,
        unit: int,
        unit_number: int,
        limit: int,
        include_partial_bar: bool
    ):
        url = f"{self.base_url}/api/History/retrieveBars"
        headers = {
            "accept": "text/plain",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        payload = {
            "contractId": contract_id,
            "live": live,
            "startTime": start_time,
            "endTime": end_time,
            "unit": unit,
            "unitNumber": unit_number,
            "limit": limit,
            "includePartialBar": include_partial_bar
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and data.get("errorCode") == 0:
                return data.get("bars", [])
            else:
                raise Exception(f"API Error: {data.get('errorMessage')}")
        else:
            raise Exception(f"HTTP Error: {response.status_code} {response.text}")