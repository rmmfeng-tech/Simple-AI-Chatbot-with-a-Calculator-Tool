import json

# grabs the arguments of the toolcall and activate the function
def handle_calculator_call(message):
    arguments = arguments = message[0].function.arguments
    operation,a,b = arguments.values()
    result = calculator(operation,a,b)
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

tools = [{"type": "function", "function": calculator_function}]