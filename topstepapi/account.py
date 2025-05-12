import requests

class AccountAPI:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url

    def search_accounts(self, only_active: bool = True):
        url = f"{self.base_url}/api/Account/search"
        headers = {
            "accept": "text/plain",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        payload = {
            "onlyActiveAccounts": only_active
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and data.get("errorCode") == 0:
                return data.get("accounts", [])
            else:
                raise Exception(f"API Error: {data.get('errorMessage')}")
        else:
            raise Exception(f"HTTP Error: {response.status_code} {response.text}")