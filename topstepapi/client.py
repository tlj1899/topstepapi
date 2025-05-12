from .auth import AuthClient
from .account import AccountAPI
from .contract import ContractAPI
from .order import OrderAPI
from .position import PositionAPI
from .trade import TradeAPI
from .history import HistoryAPI
from .realtime import RealTimeClient


class TopstepClient:
    def __init__(self, username: str, api_key: str, base_url: str = "https://api.topstepx.com"):
        self.auth = AuthClient(base_url)
        self.auth.login(username, api_key)
        self.token = self.auth.get_token()
        self.base_url = base_url

        self.account = AccountAPI(self.token, self.base_url)
        self.contract = ContractAPI(self.token, self.base_url)
        self.order = OrderAPI(self.token, self.base_url)
        self.position = PositionAPI(self.token, self.base_url)
        self.trade = TradeAPI(self.token, self.base_url)
        self.history = HistoryAPI(self.token, self.base_url)