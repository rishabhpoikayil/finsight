functions = [
    {
        'name': 'get_stock_price',
        'description': 'Gets the latest stock price given the ticker symbol of a company.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {'type': 'string', 'description': 'The stock ticker symbol'}
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'calculate_SMA',
        'description': 'Calculate simple moving average for a given ticker and window.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {'type': 'string'},
                'window': {'type': 'integer'}
            },
            'required': ['ticker', 'window']
        }
    },
    {
        'name': 'calculate_EMA',
        'description': 'Calculate exponential moving average for a given ticker and window.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {'type': 'string'},
                'window': {'type': 'integer'}
            },
            'required': ['ticker', 'window']
        }
    },
    {
        'name': 'calculate_RSI',
        'description': 'Calculate relative strength index (RSI) for a stock ticker.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {'type': 'string'}
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'calculate_MACD',
        'description': 'Calculate MACD for a stock ticker.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {'type': 'string'}
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'plot_stock_price',
        'description': 'Plot the stock price over the past year.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {'type': 'string'}
            },
            'required': ['ticker']
        }
    }
]
