import requests

class PositionAPI:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url

    def close_position(self, account_id: int, contract_id: str):
        url = f"{self.base_url}/api/Position/closeContract"
        headers = {
            "accept": "text/plain",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        payload = {
            "accountId": account_id,
            "contractId": contract_id
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and data.get("errorCode") == 0:
                return True
            else:
                raise Exception(f"API Error: {data.get('errorMessage')}")
        else:
            raise Exception(f"HTTP Error: {response.status_code} {response.text}")

    def partial_close_position(self, account_id: int, contract_id: str, size: int):
        url = f"{self.base_url}/api/Position/partialCloseContract"
        headers = {
            "accept": "text/plain",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        payload = {
            "accountId": account_id,
            "contractId": contract_id,
            "size": size
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and data.get("errorCode") == 0:
                return True
            else:
                raise Exception(f"API Error: {data.get('errorMessage')}")
        else:
            raise Exception(f"HTTP Error: {response.status_code} {response.text}")

    def search_open_positions(self, account_id: int):
        url = f"{self.base_url}/api/Position/searchOpen"
        headers = {
            "accept": "text/plain",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        payload = {
            "accountId": account_id
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and data.get("errorCode") == 0:
                return data.get("positions", [])
            else:
                raise Exception(f"API Error: {data.get('errorMessage')}")
        else:
            raise Exception(f"HTTP Error: {response.status_code} {response.text}")