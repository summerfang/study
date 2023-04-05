const openai = require('openai');
openai.api_key = "byKUnbqPglocp5Tvu7xZT3BlbkFJTU5FvpfazqAzm5oKhBwY";

const prompt = "Hello, my name is";
const maxTokens = 5;
const temperature = 0.5;

const completionRequest = {
  engine: 'davinci',
  prompt: prompt,
  max_tokens: maxTokens,
  temperature: temperature
};

openai.completions.create(completionRequest)
  .then(response => {
    console.log(response.choices[0].text);
  })
  .catch(error => {
    console.error(error);
  });