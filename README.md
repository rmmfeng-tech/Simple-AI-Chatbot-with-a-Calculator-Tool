# Simple AI Chatbot with a Calculator Tool

## 1 - Prerequisites

Before getting started, make sure you have:  
- Python 3.12+ installed  
- Ollama installed and configured: [Ollama Docs](https://github.com/ollama/ollama)
  - gpt-oss:20b model downloaded
- Project dependencies installed:  

```bash
pip install -r requirements.txt
```

## 2 - How it works

### 2.1 - Gradio interface
when using this option the script will generate an URL, copy it and past it into
any browser to start talking to the model.

### 2.2 - CLI interface
when using this option as soon as the script starts you will be able to talk to
the model

## 3 - What was, my implementation logic

### 3.1 - For the prompt

I focused on a simple, direct, and easy-to-read prompt. I like to use XML tags
since they help visualize the prompt and also is a good way to separate content,
I also saw that the cursor team (AI powerd coding editor tool) uses tags XML, 
and Cursor is considered one of the best AI-powered coding tools.

reference to my cursor claim
https://byteatatime.dev/posts/cursor-prompt-analysis/?utm_source=tldrnewsletter

### 3.2 - For the script itself

I decided to go with ollama since I use it with some regulatiry, but i could do it
with Open AI models too, actually would be a little easier since the course i made
uses Open AI models in their code. however i prefer a little challenge.

My main focus was to make the chatbot work well in a CLI , and if i could
make it work i would them go to a gradio interface, since most people prefer a
more clean interface that gradio provides.

Initially, I wasn't going to make the chatbot stream the dialogue, but if you 
consider the waiting time for a local model takes to start talking plus the 
waiting time for the full response, you would wait a lot for the answer, and I 
considered this a bad user experience and decided to use the streaming approach.

## 4 - What did I learn and what I would make diferent with extra time

### 4.1 - What I learned

I learn a little better how to use streaming and how to make the tool usage on ollama 
to work. I used the docummentation of ollama,I used the documentation for Ollama,
ChatGPT, and the knowledge from the course I took to guide me on this task.

### 4.2 - What would I make diferent?

* The main thing I would change is to make the calculator more precise. As is 
the calculator is pretty simple, it can only calculate operations with 2 numbers.
* I would consider trying to implement MCP (model context protocol) to this project
I tried once but I couldn't make it work with ollama yet. with that I could add
tools to it pretty fast.
