curl https://api.openai.com/v1/embeddings \
-H 'Content-Type: application/json' \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
    "input": "Unit test is very important.",
    "model": "text-embedding-ada-002"
    }'