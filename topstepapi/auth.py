import requests

class AuthClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.token = None

    def login(self, username: str, api_key: str) -> bool:
        url = f"{self.base_url}/api/Auth/loginKey"
        payload = {
            "userName": username,
            "apiKey": api_key
        }
        headers = {
            "accept": "text/plain",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        # print("Login response:", response.json()) 

        if response.status_code == 200:
            data = response.json()
            if data.get("success") and data.get("errorCode") == 0:
                self.token = data.get("token")
                return True
        return False

    def get_token(self) -> str:
        return self.token