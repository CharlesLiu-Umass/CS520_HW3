# %%
#Import pytest
import pytest
#Import GEMINI generated response to problem 1
import GEMINI_generated_code.CoT.gen_code_1 as GemCot1

#Import GPT generated response to problem 8
import GPT_generated_code.SCoT.gen_code_8 as GPTSCot8
#Import all unit tests for problem 1 and 8
import tests_unit.test_cases.test_1 as test_1
import tests_unit.test_cases.test_8 as test_8

# Evaluate function to check generated code passes unit test
def evaluate(fn, test_cases):
    @pytest.mark.parametrize("args, expected", test_cases)
    def test_fn(args, expected):
        result = fn(*args)
        assert result == expected or list(result) == expected, f"{args}, Expected: {expected} got: {result}"
    test_fn.__name__ = f"test_{fn.__name__}"
    return test_fn

def evaluate(fn, test_cases):
    for args, expected in test_cases:
        result = fn(*args)
        assert result == expected or list(result) == expected, f"{fn.__name__}{args} = {result}, expected {expected}"

# #Problem 1
#test_problem_1 = evaluate(GemCot1.has_close_elements, test_1.TEST_CASES)
def test_problem_1():
    evaluate(GemCot1.has_close_elements, test_1.TEST_CASES)

#Problem 8
#test_problem_8 = evaluate(GPTSCot8.is_s_palindrome,test_8.TEST_CASES)
def test_probme_8():
    evaluate(GPTSCot8.is_s_palindrome,test_8.TEST_CASES)