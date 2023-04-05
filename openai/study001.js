const axios = require('axios');
const OPENAI_API_KEY = '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';

const instance = axios.create({
  baseURL: 'https://api.openai.com/v1',
  headers: {'Authorization': `Bearer ${OPENAI_API_KEY}`}
});

const prompt = "Hello, my name is";
const maxTokens = 5;
const temperature = 0.5;

const request = {
  engine: 'davinci',
  prompt: prompt,
  max_tokens: maxTokens,
  temperature: temperature
};

instance.post('/engines/davinci/completions', request)
  .then(response => {
    console.log(response.data.choices[0].text);
  })
  .catch(error => {
    console.error(error);
  });