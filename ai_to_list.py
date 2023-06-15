import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define your chat conversation
conversation = [
    {'role': 'user', 'content': 'Who won the world series in 2020?'}
]

# Send the completion request to the API
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=conversation,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7
)

# Extract the assistant's reply from the response
assistant_reply = response.choices[0].text.strip()

# Split the assistant's reply into a list of sentences
reply_list = assistant_reply.split('. ')

# Print the list of sentences
print(reply_list)
