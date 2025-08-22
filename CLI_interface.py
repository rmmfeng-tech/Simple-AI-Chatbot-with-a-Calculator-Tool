from tools import handle_tool_call,tools

from ollama import chat,ChatResponse

# puts the prompt str in the system prompt variable
with open('prompt.txt','r+',encoding='utf-8') as file:
    system_prompt = file.read()

# the variable that indicates the selected model
model = 'gpt-oss:20b'

# the history of messages that the user said so far
history = ''

# the question to start the dialog with the user
user_prompt = input('How can i help you today? \n')

# the loop to make the chat alive
while True:
    # List of messages that will be sent to the LLM
    messages = [
        {
            'role': 'system',
            'content': system_prompt
        },
        {
            'role': 'system',
            'content': history + user_prompt
        }
    ]

    # the chat function beeing activated to make the answer to the question
    response: ChatResponse = chat(
        model= model,
        messages = messages,
        stream = True,
        tools = tools
    )

    # add user question to history
    history += user_prompt + "\n"

    for chunk in response:
        # if there is a toolcall this part of the code will peak it and solve it
        if chunk.message.tool_calls:
            print(chunk.message.tool_calls)
            message = chunk.message.tool_calls
            response = handle_tool_call(message)
            messages.append(response)
            response = chat(model= 'gpt-oss:20b',messages = messages,stream = True,)
            for chunk in response:
                print(chunk['message']['content'], end='', flush=True)
                history += chunk['message']['content']

        # else the code will run without the toolcall and the answer will be 
        # streamed to the user
        else:
            print(chunk['message']['content'], end='', flush=True)
            history += chunk['message']['content']

    history += "\n"

    # let's the user make a new question and restart the process aftwards
    user_prompt = input('\nnew question: \n')