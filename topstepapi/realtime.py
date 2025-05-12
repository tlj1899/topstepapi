
from signalrcore.hub_connection_builder import HubConnectionBuilder

class RealTimeClient:
    def __init__(self, token: str, hub: str = "user"):
        base_url = "https://gateway-rtc-demo.s2f.projectx.com/hubs/"
        self.hub_url = f"{base_url}{hub}?access_token={token}"
        self.connection = HubConnectionBuilder()\
            .with_url(self.hub_url)\
            .with_automatic_reconnect({
                "type": "raw",
                "keep_alive_interval": 10,
                "reconnect_interval": 5
            })\
            .build()

    def start(self):
        self.connection.start()

    def stop(self):
        self.connection.stop()

    def subscribe_accounts(self):
        self.connection.send("SubscribeAccounts", [])

    def subscribe_orders(self, account_id):
        self.connection.send("SubscribeOrders", [account_id])

    def subscribe_positions(self, account_id):
        self.connection.send("SubscribePositions", [account_id])

    def subscribe_trades(self, account_id):
        self.connection.send("SubscribeTrades", [account_id])

    def on_account_update(self, handler):
        self.connection.on("GatewayUserAccount", handler)

    def on_order_update(self, handler):
        self.connection.on("GatewayUserOrder", handler)

    def on_position_update(self, handler):
        self.connection.on("GatewayUserPosition", handler)

    def on_trade_update(self, handler):
        self.connection.on("GatewayUserTrade", handler)