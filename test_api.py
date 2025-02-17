import openai
import config

client = openai.OpenAI(
    api_key = config.xmcp_api_key,
    # LiteLLM Proxy is OpenAI compatible, Read More: https://docs.litellm.ai/docs/proxy/user_keys
    base_url = config.xmcp_base_url
)

response = client.chat.completions.create(
    # model to send to the proxy
    model = config.xmcp_model,
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "this is a test request, write a short poem"
        }
    ],
    temperature = 0.3,
    max_tokens = 1024
)

print(response, "\n\n")

print(response.choices[0].message.content)