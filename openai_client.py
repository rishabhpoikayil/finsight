from openai import OpenAI

def get_openai_client(api_key_path='API_KEY'):
    with open(api_key_path, 'r') as f:
        api_key = f.read().strip()
    return OpenAI(api_key=api_key)
