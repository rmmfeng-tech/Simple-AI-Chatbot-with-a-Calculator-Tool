# Simple AI Chatbot with a Calculator Tool

## pre-requirements

### 0 - python

You must have Python installed in you machine and some previous knowledge on Python
to make this code work

my Python version is 3.12.4

---
### 1 - ollama installed

to make this script work you have to install the ollama on your machine:

the steps are :
* Go to https://ollama.com/download
* Choose the windows download option
* Open the installer and finish the installation process

**important:**
Every time you run this scripts, Ollama must be running
---
### 2 - download the model you want to use

after you have ollama fully installed you must download a model:

the steps are :
* Open ollama
* Open the PowerShell/CMD in windows
* Type `ollama` in PowerShell/CMD, that will show you the main comands FOR ollama
* The command we need to use is `ollama run [name of the model]`
    * this will run the mode. If you don't have it, it will download it first 
    and them run it.
    * the model we will be using is gpt-oss:20b, you can use any model that has 
    the tool-using capabilities for this script, however i didn't test how well 
    they work with this script
    * if you decide to use another model instead of gpt-oss:20b for this script 
    remember to change the model variable in the script to the name of the model
    you're gonna use

**important:**
make sure you have enough space in you diretory to download the model, and the
right amont of RAM to run it

**small tip**
if you have multiple directories and don't want to flood your main one with the
really heavy LLM's you can use the following youtube guide to change the 
download path
https://www.youtube.com/watch?v=uj1VnDPR9xo
---
### 3 - virtual environment

create a virtual environment to download the main libraries to run this code

the steps are :
* clone this repo
* create the virtual environment with the `command python3.12.4 -m venv [name of the virtual environment]`
    * you can do this in any code editor you want by opening a new terminal tab 
    or you could create directly from PowerShell/CMD if you are already in the 
    right path
    * some versions of python ask for `py` instead of `python` in the command 
* with the venv active type the following command `pip install -r requirements.txt`
    *to activate the venv `[name of the venv]\Scripts\activate` but you must be in
    the venv path
---
## running the code

After completing these steps, running the code is straightforward. With the 
virtual environment active, run the script.

There are two options for running it, with gradio interface and without gradio 
interface.

### 1 gradio interface
when using this option the script will generate an URL, copy it and past it into
any browser to start talking to the model.
---
### 2 CLI interface
when using this option as soon as the script starts you will be able to talk to
the model
---

**important**
since this model is running localy in your machine the results will be slower 
than if you run a frontier model from their service directly. this is specially
true the first time you are using the model that day.

## prompts modification

if you wanna check the system prompt that the code is running go in the 
prompt.txt file and make sure everything is how you would want it.
---

# what was, my implementation logic

I mainly used the knowled from a course i took, and my knowled of prompt 
engineering to create a straightfoward solution.

## for the prompt

I focused on a simple, direct, and easy-to-read prompt. I like to use XML tags
since they help visualize the prompt and also is a good way to separate content,
I also saw that the cursor team (AI powerd coding editor tool) uses tags XML, 
and Cursor is considered one of the best AI-powered coding tools.

reference to my cursor claim
https://byteatatime.dev/posts/cursor-prompt-analysis/?utm_source=tldrnewsletter

## For the script itself

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

# what did i learn and what i would make diferent with extra time

## what i learned

I learn a little better how to use streaming and how to make the tool usage on ollama 
to work. I used the docummentation of ollama,I used the documentation for Ollama,
ChatGPT, and the knowledge from the course I took to guide me on this task.

## What would i make diferent?

* The main thing I would change is to make the calculator more precise. As is 
the calculator is pretty simple, it can only calculate operations with 2 numbers.
* I would consider trying to implement MCP (model context protocol) to this project
I tried once but i couldn't make it work with ollama yet. with that i could add
tools to it pretty fast.
