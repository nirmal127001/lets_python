Evaluate Arithmetic Expressions

with open('file.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        expression = line.strip()
        expression = expression.replace("=",'')
        expression = expression.replace("^",'**')
        expression = expression.replace(") (",') * (')
        result = eval(expression)
        output_file.write(f"{expression}= {result}\n")
