# TopstepAPI Python Wrapper

A Python package for interacting with the TopstepX API, including authentication, account management, order placement, position management, trade history, contract search, historical bars, and real-time streaming via SignalR.

---

## Installation

Install from your local directory (editable mode recommended for development):

```bash
pip install -e .
```

Or standard install:

```bash
pip install .
```

**Dependencies:**

- `requests`
- `signalrcore` (for real-time streaming)

---

## Usage

### 1. Import and Authenticate

```python
from topstepapi import TopstepClient

username = "YOUR_USERNAME"
api_key = "YOUR_API_KEY"

client = TopstepClient(username, api_key)
```

---

### 2. Accounts

```python
# List active accounts
accounts = client.account.search_accounts()
print(accounts)
```

---

### 3. Contracts

```python
# Search for contracts
contracts = client.contract.search_contracts("NQ")
print(contracts)

# Search for contract by ID
contract = client.contract.search_contract_by_id("CON.F.US.ENQ.H25")
print(contract)
```

---

### 4. Orders

```python
# Search for orders
orders = client.order.search_orders(account_id=123, start_timestamp="2025-01-01T00:00:00Z")

# Search for open orders
open_orders = client.order.search_open_orders(account_id=123)

# Place an order
order_id = client.order.place_order(
    account_id=123,
    contract_id="CON.F.US.DA6.M25",
    type=2,  # Market
    side=1,  # Sell
    size=1
)

# Cancel an order
client.order.cancel_order(account_id=123, order_id=456)

# Modify an order
client.order.modify_order(account_id=123, order_id=456, size=2, stop_price=1604)
```

---

### 5. Positions

```python
# Search for open positions
positions = client.position.search_open_positions(account_id=123)

# Close a position
client.position.close_position(account_id=123, contract_id="CON.F.US.GMET.J25")

# Partially close a position
client.position.partial_close_position(account_id=123, contract_id="CON.F.US.GMET.J25", size=1)
```

---

### 6. Trades

```python
# Search for trades
trades = client.trade.search_trades(account_id=123, start_timestamp="2025-01-01T00:00:00Z")
```

---

### 7. Historical Bars

```python
bars = client.history.retrieve_bars(
    contract_id="CON.F.US.RTY.Z24",
    live=False,
    start_time="2024-12-01T00:00:00Z",
    end_time="2024-12-31T21:00:00Z",
    unit=3,  # Hour
    unit_number=1,
    limit=7,
    include_partial_bar=False
)
```

---

### 8. Real-Time Streaming (SignalR)

> **Note:** Real-time streaming requires `signalrcore` and is optional.

```python
# Start real-time connection
client.realtime.start()

# Subscribe to account/order/position/trade updates
client.realtime.subscribe_accounts()
client.realtime.subscribe_orders(account_id=123)
client.realtime.subscribe_positions(account_id=123)
client.realtime.subscribe_trades(account_id=123)

# Register event handlers
def on_order_update(data):
    print("Order update:", data)

client.realtime.on_order_update(on_order_update)
```

---

## Notes

- All API requests require a valid session token, handled automatically after login.
- Session tokens are valid for 24 hours; re-authenticate as needed.
- For more details on endpoints and parameters, refer to the official TopstepX API documentation.

---

## License

MIT License
