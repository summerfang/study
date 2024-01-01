curl https://api.openai.com/v1/chat/completions \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gpt-3.5-turbo", 
    "temperature": 0.7, 
    "messages": [{"role":"user", "content":"Give me a json format object."}]
    }' 

openai api chat_completions.create -m gpt-3.5-turbo -g user "Hello world"