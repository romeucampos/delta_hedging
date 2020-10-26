
# Delta Hedge Deribit

## install

```bash
git clone https://github.com/romeucampos/delta_hedging.git
cd delta_hedging
pip install -r requirements.txt
```

## Configuration

```json
{
    "KEY": "XvkLkkEY",
    "SECRET": "z8MAadPGXqJDKH5__SBXMg0D7Ip7KhfwLvEZQ6aE3Nc",
    "AMPLITUDE": 1.5,
    "SYMBOL": "BTC-PERPETUAL",
    "INITIAL_HEDGER": true,
    "TIME_LOOP" : 10,
    "URL_TEST": true
}
```

## Basic Usage

1. Make the synthetic straddle or buy call or buy put.
2. Run the script.
 ```bash
python delta_hedging.py
2020-10-15 08:08:53 - Delta: -0.0012 - LN: -0.19% - Last trade: 11341.5 - Last ticker: 11320.0
2020-10-15 08:08:59 - Delta: -0.0013 - LN: -0.19% - Last trade: 11341.5 - Last ticker: 11320.0
2020-10-15 08:09:05 - Delta: -0.0013 - LN: -0.19% - Last trade: 11341.5 - Last ticker: 11320.0
2020-10-15 08:09:11 - Delta: -0.0013 - LN: -0.19% - Last trade: 11341.5 - Last ticker: 11320.5
2020-10-15 08:09:17 - Delta: -0.0013 - LN: -0.19% - Last trade: 11341.5 - Last ticker: 11320.5
```
