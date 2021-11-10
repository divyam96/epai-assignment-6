# Session 6 Assignment of EPAi4.0
### Submitted by Divyam Malay Shah
### E-mail id: divyam096@gmail.com


# Scopes and Closures

The assignment demonstrates the application of scopes, which is applicable with respect to a variable name, and closures (also known as nested functions) in Python codes.


## Description of functions implemented in the current code

### check_docstring

This closure has been written to check if the docstring of an input function has greater than fifty characters.

#### Definition of the function:
 check_docstring()

Brief description of all the test cases that have been employed to check the efficacy of the algorithms written within the function “check_docstring” are as follows:

| Name of the test                                                  | Brief description of the test                                                                                                     | Status (Passed/ Failed) |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| test\_session\_6\_check\_docstring\_no\_function                  | This test checks if the code raises an error when a non-integer value is passed.                                                  | Passed                  |
| test\_session\_6\_check\_docstring\_no\_docstring                 | This test checks if the code raises an error when no docstring is passed.                                                         | Passed                  |
| test\_session\_6\_check\_docstring\_less\_than\_50\_characters    | This test checks if the code raises an error if  a docstring containing less than fifty characters has been passed.               | Passed                  |
| test\_session\_6\_check\_docstring\_greater\_than\_50\_characters | This test checks if the code throws any execution error when an actual docstring containing more than fifty characters is passed. | Passed                  |

### get_fibonacci_number

This closure has been written to check if an input number is a Fibonacci one and to generate the next Fibonacci number.

#### Definition of the function:
 get_fibonacci_number()

Brief description of all the test cases that have been employed to check the efficacy of the algorithms written within the function “get_fibonacci_number” are as follows:

| Name of the test                                           | Brief description of the test                                                                                                                                       | Status (Passed/ Failed) |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| test\_session\_6\_get\_fibonacci\_number\_type\_check      | This test checks if the input number is greater than zero; the test also checks if the number is an integer; the test also checks if the number is a Fibonacci one. | Passed                  |
| test\_session\_6\_get\_fibonacci\_number\_execution\_check | This test checks if the next Fibonacci number generated is correct.                                                                                                 | Passed                  |
### track_arth_count

This closure has been written in order to count how many times a few allowed functions - 'add', 'mul' and 'div' - have been called, and the respective counts are stored as values in a dictionary, with the corresponding function names acting as the keys.

#### Definition of the function:
 track_arth_count(fn),
where, fn = a function that needs to be passed as a mandatory positional argument.

Brief description of all the test cases that have been employed to check the efficacy of the algorithms written within the function “track_arth_count” are as follows:
| Name of the test                                                  | Brief description of the test                                                                                    | Status (Passed/ Failed) |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------- |
| test\_session\_6\_track\_arth\_count\_dict\_check                 | This test checks if the output is being stored in a dictionary.                                                  | Passed                  |
| test\_session\_6\_track\_arth\_count\_no\_fn                      | This test checks if positional argument exists in the function track\_arth\_count.                               | Passed                  |
| test\_session\_6\_track\_arth\_count\_no\_args                    | This test checks if the required positional arguments have been passed to the track\_arth\_count inner function. | Passed                  |
| test\_session\_6\_track\_arth\_count\_invalid\_arg                | This test checks if the input is a valid function.                                                               | Passed                  |
| test\_session\_6\_track\_arth\_count\_undefined\_function         | This test checks if an error is raised when a disallowed function is passed as an argument.                      | Passed                  |
| test\_session\_6\_track\_arth\_count\_function\_execution\_test | This test checks if the functions are giving appropriate results after execution.                                | Passed                  |

### new_input_dictionary

This closure has been written to take a dictionary - similar to the one created in the function track_arth_count - as input, and counting the number of times 'add', 'mul' and 'div' have been called.

#### Definition of the function:
new_input_dictionary(fn, custom_dict)
where, fn = a function that needs to be passed as a mandatory positional argument,
	custom_dict = dictionary input by the user.

Brief description of all the test cases that have been employed to check the efficacy of the algorithms written within the function “new_input_dictionary” are as follows:
| Name of the test                                                    | Brief description of the test                                                                                            | Status (Passed/ Failed) |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| test\_session\_6\_new\_input\_dictionary\_dict\_check               | This test checks if the output is being stored in a dictionary.                                                          | Passed                  |
| test\_session\_6\_new\_input\_dictionary\_invalid\_arg              | This test checks if the input is a valid function.                                                                       | Passed                  |
| test\_session\_6\_new\_input\_dictionary\_no\_args                  | This test checks if the mandatory positional arguments have been passed in function new\_input\_dictionary.              | Passed                  |
| test\_session\_6\_new\_input\_dictionary\_inner\_no\_args           | This test checks if the mandatory positional arguments have been passed in the inner function of new\_input\_dictionary. | Passed                  |
| test\_session\_6\_new\_input\_dictionary\_undefined\_function       | This test checks if an error is raised when a disallowed function is passed as an argument.                              | Passed                  |
| test\_session\_6\_new\_input\_dictionary\_function\_execution\_test | This test checks if the functions are giving appropriate results after execution.                                        | Passed                  |

The following table illustrates the test cases that have been employed to check the various aspects of document formatting of the README.md and the session6.py files.

| Name of the test case                                     | Brief description of the test case                                                                                                                                                                                             | Function/File being tested | Status(Passed/Failed) |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- | ----------------------- |
| test\_session5\_readme\_exists                            | This test checks if the README.md file has been created.                                                                                                                                                                       | README.md                  | Passed                  |
| test\_session5\_readme\_500\_words                        | This test checks if the README.md file contains at least 500 words.                                                                                                                                                            | README.md                  | Passed                  |
| test\_session5\_readme\_proper\_description               | This test checks if the functions have been described well in the README.md file.                                                                                                                                              | README.md                  | Passed                  |
| test\_session5\_readme\_file\_for\_more\_than\_10\_hashes | This test checks if a minimum of ten topics have been mentioned in the README.md file.                                                                                                                                         | README.md                  | Passed                  |
| test\_session5\_indentations                            | The PEP8 guidelines state that the number of spaces left should be a multiple of four, for defining proper indentation within a code. This test checks if the code has been written adhering to the aforementioned guideline. | session5.py                | Passed                  |
| test\_session5\_function\_name\_had\_cap\_letter          | According to PEP8 guidelines, the names of functions cannot have any capital letters in them. This test ensures that there are no such capital letters in the names of functions.                                              | session6.py                | Passed                  |




