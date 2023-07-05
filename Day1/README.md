Challenge -1 : Implement a function called reverse_string(string) that takes a string as input and returns the reverse of that string.

Your task is to write the implementation code for the reverse_string() function using Test-Driven Development (TDD) principles. Start by writing test cases to cover different scenarios, and then write the code to make those tests pass.

Here are a few test cases to get you started:

Test Case 1:
 assert reverse_string("Hello") == "olleH"
Test Case 2:
 assert reverse_string("") == ""
Remember, follow the TDD process:

:one: Think: Define the requirements and expectations for the reverse_string() function.

:two: Test: Write test cases that validate the expected behavior of the function.

:three: Code: Implement the reverse_string() function using the simplest code possible to pass the tests.

:four: Refactor: If needed, optimize and improve your code while ensuring the tests remain green.

# TEST
python3 -m doctest -v ./tests/reverse_string.txt | tail -2