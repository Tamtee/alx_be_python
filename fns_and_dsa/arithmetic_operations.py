def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "cannot divide by zero"
        return num1 / num2
    else:
        return "return none for Invalid operation"
    from arithmetic_operations import perform_operation

print(perform_operation(5, 6, "add"))       # Should print: 11
print(perform_operation(5, 6, "subtract"))  # Should print: -1
print(perform_operation(5, 6, "multiply"))  # Should print: 30
print(perform_operation(5, 0, "divide"))    # Should print: "Cannot divide by zero"
print(perform_operation(5, 6, "divide"))    # Should print: 0.8333333333333334


