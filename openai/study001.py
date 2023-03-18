import openai
openai.api_key = "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"

response = openai.Completion.create(
  engine="davinci",
  prompt="Hello, my name is",
  max_tokens=5,
  n=1,
  stop=None,
  temperature=0.5,
)

print(response.choices[0].text)
