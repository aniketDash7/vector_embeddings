from openai import OpenAI
client = OpenAI(api_key="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")

response = client.embeddings.create(
    model = 'text-embedding-ada-002',
    input = 'The best part of my day was the result',
    encoding_format = "float"
)

print(response)