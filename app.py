import json
import streamlit as st
from openai_client import get_openai_client
from functions import (
    get_stock_price, calculate_SMA, calculate_EMA, calculate_RSI, calculate_MACD, plot_stock_price
)
from tools_metadata import functions

# Initialize OpenAI client
client = get_openai_client()

available_functions = {
    'get_stock_price': get_stock_price,
    'calculate_SMA': calculate_SMA,
    'calculate_EMA': calculate_EMA,
    'calculate_RSI': calculate_RSI,
    'calculate_MACD': calculate_MACD,
    'plot_stock_price': plot_stock_price
}

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.title('📈 FinSight: Stock Analysis Assistant')

user_input = st.text_input("Ask a question about a stock:")

if user_input:
    try:
        st.session_state['messages'].append({'role': 'user', 'content': user_input})

        # Step 1: Get AI response
        response = client.chat.completions.create(
            model='gpt-4o',
            messages=st.session_state['messages'],
            tools=[{'type': 'function', 'function': f} for f in functions],
            tool_choice='auto'
        )

        message = response.choices[0].message

        if message.tool_calls:
            tool_call = message.tool_calls[0]
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            # Prepare args for function call
            if function_name in ['get_stock_price', 'calculate_RSI', 'calculate_MACD', 'plot_stock_price']:
                args_dict = {'ticker': function_args.get('ticker')}
            elif function_name in ['calculate_SMA', 'calculate_EMA']:
                args_dict = {'ticker': function_args.get('ticker'), 'window': function_args.get('window')}
            else:
                args_dict = {}

            result = available_functions[function_name](**args_dict)

            st.session_state['messages'].append({
                'role': 'assistant',
                'content': None,
                'tool_calls': [tool_call]
            })

            st.session_state['messages'].append({
                'role': 'tool',
                'tool_call_id': tool_call.id,
                'name': function_name,
                'content': result
            })

            if function_name == 'plot_stock_price':
                st.image('stock.png')
            else:
                # Step 2: Send tool result back to LLM for follow-up
                followup = client.chat.completions.create(
                    model='gpt-4o',
                    messages=st.session_state['messages']
                )
                followup_content = followup.choices[0].message.content
                st.session_state['messages'].append({'role': 'assistant', 'content': followup_content})
                st.text(followup_content)

        else:
            content = message.content
            st.session_state['messages'].append({'role': 'assistant', 'content': content})
            st.text(content)

    except Exception as e:
        st.error(f"Error occurred: {e}")
