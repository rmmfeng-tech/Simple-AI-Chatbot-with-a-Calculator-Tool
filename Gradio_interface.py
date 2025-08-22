import gradio as gr

from tools import handle_tool_call,tools

from ollama import chat,ChatResponse

# puts the prompt str in the system prompt variable
with open('prompt.txt','r+',encoding='utf-8') as file:
    system_prompt = file.read()

# the variable that indicates the selected model
model = 'gpt-oss:20b'

# the function that make the chat work in the gradio interface
def chat_box(user_prompt,history):
    # List of messages that will be sent to the LLM
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": user_prompt}]
    # the chat function beeing activated to make the answer to the question
    stream: ChatResponse = chat(
        model = model,
        messages = messages,
        stream = True,
        tools = tools
    )
    response = ''
    for chunk in stream:
        # if there is a toolcall this part of the code will peak it and solve it
        if chunk.message.tool_calls:
            message = chunk.message.tool_calls
            new_stream = handle_tool_call(message)
            messages.append(new_stream)
            new_stream = chat(model= 'gpt-oss:20b',messages = messages,stream = True,)
            for chunk in new_stream:
                response += chunk['message']['content']
                yield response
        
        # else the code will run without the toolcall and the answer will be 
        # streamed to the user
        else:
            response += chunk['message']['content']
            yield response

# this function starts the gradio interface, gradio handles the history and 
# user_prompt part by itself
gr.ChatInterface(fn=chat_box, type="messages",title="How can i help you today?").launch()

