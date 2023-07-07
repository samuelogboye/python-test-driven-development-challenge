# Challenge -1
Implement a function called reverse_string(string) that takes a string as input and returns the reverse of that string.

Your task is to write the implementation code for the reverse_string() function using Test-Driven Development (TDD) principles. Start by writing test cases to cover different scenarios, and then write the code to make those tests pass.

Here are a few test cases to get you started:

Test Case 1: assert reverse_string("Hello") == "olleH" Test Case 2: assert reverse_string("") == "" Remember, follow the TDD process:

1️⃣ Think: Define the requirements and expectations for the reverse_string() function.

2️⃣ Test: Write test cases that validate the expected behavior of the function.

3️⃣ Code: Implement the reverse_string() function using the simplest code possible to pass the tests.

4️⃣ Refactor: If needed, optimize and improve your code while ensuring the tests remain green.

## TEST
python3 -m doctest -v ./tests/reverse_string.txt | tail -2

# Challenge - 2:
Implement a function called count_vowels(string) that takes a string as input and returns the count of vowels (a, e, i, o, u) in the given string. Consider both lowercase and uppercase vowels.

Your task is to write the implementation code for the count_vowels() function using Test-Driven Development (TDD) principles. Begin by writing test cases to cover various scenarios, and then write the code to make those tests pass.

Here are a few test cases to get you started:

Test Case 1:
assert count_vowels("Hello") == 2

Test Case 2:
assert count_vowels("") == 0

Take on this challenge and follow the TDD process:

:one: Think: Define the requirements and expectations for the count_vowels() function.

:two: Test: Write test cases that validate the expected behavior of the function.

:three: Code: Implement the count_vowels() function using the simplest code possible to pass the tests.

:four: Refactor: If necessary, optimize and improve your code while ensuring the tests remain green.

## TEST
python3 -m doctest -v ./tests/vowel.txt | tail -2