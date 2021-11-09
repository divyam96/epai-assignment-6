import pytest
import session6
import inspect
import os
import re
import math

README_CONTENT_CHECK_FOR = [
    'check_docstring',
    'get_fibonacci_number',
    'track_arth_count',
    'new_input_dictionary'
]


def test_session6_readme_exists():
    """Test to check if the README.md file has been created and stored in close vicinity"""
    assert os.path.isfile("README.md"), "Found README.md file!"


def test_session6_readme_500_words():
    """Test to check if the README.md file has equal to or greater than 500 words"""
    readme_words = [word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session6_readme_proper_description():
    """Test to check if description has been provided for each of the functions declared within the code"""
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session6_readme_file_for_more_than_10_hashes():
    """Test to check if the number of topics and subtopics described within the README.md file is equal to or greater
    than 10 """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "You have not described all the functions/classes well in your README.md file"


def test_session6_indentations():
    """Test to check if the indentation in the session6.py file follows the PEP8 guidelines"""
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session6_function_name_had_cap_letter():
    """PEP8 gudelines state that function names cannnot have capital letters in them. This test checks if there are any \
    capital lettes within function names and throws error if there are."""
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


####################### Validation for check_docstring #################################

def test_func_no_docstring():
    """This is a test function."""
    pass


def test_func_docstring_less_than_50_characters():
    """
    This is a small docstring.
    """
    pass


def test_func_docstring_greater_than_50_characters():
    """
    This is a test docstring containing less than fifty characters which will help us determine if the function
    is working correctly.
    """
    pass


def test_session_6_check_docstring_no_function():
    """Test to check if the code raises an error when a non-integer value is passed."""
    with pytest.raises(TypeError, match=r".*Please enter a valid function*"):
        session6.check_docstring()(7)
    with pytest.raises(TypeError, match=r".*Please enter a valid function*"):
        session6.check_docstring()("this is a string")


def test_session_6_check_docstring_no_docstring():
    """Test to check if the code raises an error when no docstring is passed."""
    assert session6.check_docstring()(test_func_no_docstring) == False, "The function is not working for no docstring"


def test_session_6_check_docstring_less_than_50_characters():
    """Test to check if the code raises an error if a docstring containing less than 50 characters is passed."""
    assert session6.check_docstring()(
        test_func_docstring_less_than_50_characters) == False, "The function is not working for docstring with less than fifty characters"


def test_session_6_check_docstring_greater_than_50_characters():
    """Test to check if the code throws any execution error when an actual docstring containing more \
    than fifty characters is passed"""
    assert session6.check_docstring()(
        test_func_docstring_greater_than_50_characters) == True, "The function is not working for docstring with more than fifty characters"


####################### Validation for get_fibonacci_number #######################################

def test_session_6_get_fibonacci_number_type_check():
    """Test to ensure sanity of type and values in get_fibonacci_number function"""
    with pytest.raises(ValueError, match=r".*Enter a number equal to or greater than 1*"):
        session6.get_fibonacci_number()(-4)
    with pytest.raises(TypeError, match=r".*Please enter an integer only*"):
        session6.get_fibonacci_number()("test")
    with pytest.raises(ValueError, match=r".*The input is not a Fibonacci number*"):
        session6.get_fibonacci_number()(4)


def test_session_6_get_fibonacci_number_execution_check():
    """Test to check if the next Fibonacci number generated is correct."""
    assert session6.get_fibonacci_number()(8) == 13, "The logic is not working properly"


####################### Validation for track_arth_count #######################################

def test_session_6_track_arth_count_dict_check():
    """Test to check if the output is being stored in a dictionary"""
    assert (type(session6.dictionary_of_functions) is dict) == True, "Dictionary is not available"


def test_session_6_track_arth_count_no_fn():
    """Test to check if mandatory positional argument exists in the function track_arth_count"""
    with pytest.raises(TypeError, match=r".*required positional argument*"):
        session6.track_arth_count()


def test_session_6_track_arth_count_no_args():
    """Test to check if the required positional arguments have been passed to the track_arth_count \
    inner function"""
    with pytest.raises(TypeError, match=r".*required positional argument*"):
        session6.track_arth_count(session6.add)()


def test_session_6_track_arth_count_invalid_arg():
    """Test to check if the input is a valid function"""
    with pytest.raises(TypeError, match=r".*Please enter a valid function*"):
        session6.track_arth_count(7)
    with pytest.raises(TypeError, match=r".*Please enter a valid function*"):
        session6.track_arth_count("This is a string")


def test_session_6_track_arth_count_undefined_function():
    """Test to check if an error is raised when a disallowed function is passed as an argument """

    def subtract(a, b):
        return a - b

    with pytest.raises(ValueError, match=r".*Only the count of add, mul, div are being monitored*"):
        session6.track_arth_count(subtract)


def test_session_6_track_arth_count_function_execution_test():
    """Test to check if the functions are giving appropriate results after execution"""
    add_fn = session6.track_arth_count(session6.add)
    mul_fn = session6.track_arth_count(session6.mul)
    div_fn = session6.track_arth_count(session6.div)
    for i in range(3):
        add_fn(2, 10)
    for j in range(5):
        mul_fn(3, 5)
    for k in range(8):
        div_fn(10, 8)
    assert (session6.dictionary_of_functions['add'] == 3) and (session6.dictionary_of_functions['mul'] == 5) and (
            session6.dictionary_of_functions['div'] == 8), "Function not working correctly"


####################### Validation for new_input_dictionary #######################################

def test_session_6_new_input_dictionary_dict_check():
    """Test to check if the output is being stored in a dictionary"""
    a = [1, 2, 3, 4]
    with pytest.raises(TypeError, match=r".*Please input only a dictionary*"):
        session6.new_input_dictionary(session6.add, a)


def test_session_6_new_input_dictionary_invalid_arg():
    """Test to check if the input is a valid function"""
    test_dict = {}
    with pytest.raises(TypeError, match=r".*Please enter a valid function*"):
        session6.new_input_dictionary(7, test_dict)
    with pytest.raises(TypeError, match=r".*Please enter a valid function*"):
        session6.new_input_dictionary("This is a string", test_dict)


def test_session_6_new_input_dictionary_no_args():
    """Test to check if the mandatory positional arguments have been passed in function new_input_dictionary"""
    with pytest.raises(TypeError, match=r".*required positional arguments*"):
        session6.new_input_dictionary()


def test_session_6_new_input_dictionary_inner_no_args():
    """Test to check if the mandatory positional arguments have been passed in the inner function of
    new_input_dictionary """
    with pytest.raises(TypeError, match=r".*required positional arguments*"):
        session6.new_input_dictionary()()


def test_session_6_new_input_dictionary_undefined_function():
    """Test to check if an error is raised when a disallowed function is passed as an argument"""
    test_dict = {}

    def subtract(a, b):
        return a - b

    with pytest.raises(ValueError, match=r".*Only add, mul, div are allowed*"):
        session6.new_input_dictionary(subtract, test_dict)


def test_session_6_new_input_dictionary_function_execution_test():
    """Test to check if the functions are giving appropriate results after execution"""
    test_dict = {}
    add_fn = session6.new_input_dictionary(session6.add, test_dict)
    mul_fn = session6.new_input_dictionary(session6.mul, test_dict)
    div_fn = session6.new_input_dictionary(session6.div, test_dict)
    for i in range(3):
        add_fn(2, 10)
    for j in range(5):
        mul_fn(3, 5)
    for k in range(8):
        div_fn(10, 8)
    assert (test_dict['add'] == 3) and (test_dict['mul'] == 5) and (
            test_dict['div'] == 8), "Function not working correctly"
