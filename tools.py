import json

def handle_tool_call(message):
    name = message[0].function.name
    if name == 'calculator':
        arguments = message[0].function.arguments
        operation,a,b = arguments.values()
        result = calculator(operation,a,b)
        response = {
            "role": "tool",
            "content": json.dumps({"result": result}),
        }
        return response
    elif name == 'word_counter':
        arguments = message[0].function.arguments
        text = arguments['text']
        words = word_counter(text)
        response = {
            "role": "tool",
            "content": json.dumps({"result": words}),
        }
        return response
    elif name == 'characters_count':
        arguments = message[0].function.arguments
        character = arguments['characters']
        result = characters_count(character)
        response = {
            "role": "tool",
            "content": json.dumps({"result": result}),
        }
        return response
        
def calculator(operation:str,a:float,b:float):
    """
    # simple calculator tool
    ----------
    ## Paramaters
    ----------
    operation : str
        this paramater defines what calculation will be done, the options are
        - 'sum'
        - 'subtraction'
        - 'multiplication'
        - 'division'
        - 'raising to power'
    
    a : float
        first value of the calculation

    b : float
        second value of the calculation

    ## Example of usage
   ----------
    **sum example**: calculator(operation ='sum',a=2,b=3)
        result = 2+3
        return result
    **subtraction example**: calculator(operation ='subtraction',a=2,b=3)
        result = 2-3
        return result
    **multiplication example**: calculator(operation ='multiplication',a=2,b=3)
        result = 2*3
        return result
    **division example**: calculator(operation ='division',a=2,b=3)
        result = a/b
        return result
    **raising to power example**: calculator(operation ='raising to power',a=2,b=3)
        result = a^b
        return result
    """
    result = 0
    if operation == 'sum':
        result = a+b
    elif operation == 'subtraction':
        result = a-b
    elif operation == 'multiplication':
        result = a*b
    elif operation == 'division':
        result = a/b
    elif operation == 'raising to power':
        result = a^b
    return result

def word_counter(text: str):
    """
    # simple word counter tool
    ----------
    ## Parameters
    ----------
    text : str
        The text whose words you want to count.

    ## Example of usage
    ----------
    word_counter('Hello world') 
        words = 2
        return len(words)
    """
    print(text)
    words = text.split()
    return len(words)

def characters_count(characters):
    """
    # simple characters counter tool
    ----------
    ## Paramaters
    ----------
    characters : str 
        The string whose characters you want to count.

    ## Example of usage
        count_characters('123456') 
        characters = 6
        return len(characters)
    """
    return len(characters)


characters_count_function = {
    "name": "characters_count",
    "description": "Counts the number of characters in a given text.",
    "parameters": {
        "type": "object",
        "properties": {
            "characters": {"type": "string", "description": "The string whose characters you want to count."}
        },
        "required": ["characters"],
    },
}
# definition of the function in a dict so the AI knows how to use it
word_counter_function = {
    "name": "word_counter",
    "description": "Counts the number of words in a given text.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {"type": "string", "description": "The text whose words you want to count."}
        },
        "required": ["text"],
    },
}
#definiton of the function in a dict so the AI know how to use it
calculator_function = {
    "name": "calculator",
    "description": """
    Simple calculator function that make the following operations :
     * sum
     * subtraction
     * multiplication
     * division
     * raising to power
    """,
    "parameters": {
        "type": "object",
        "properties": {
            'operation': {'type': 'string','description': 'the tipe of calculation you want to do'},
            'a': {'type': 'float', 'description': 'The first number in the calculation'},
            'b': {'type': 'float', 'description': 'The second number in the calculation'},
        },
        "required": ['operation','a','b'],
    }
}

tools = [
    {"type": "function", "function": calculator_function},
    {"type": "function", "function": word_counter_function},
    {"type": "function", "function": characters_count_function}
    ]