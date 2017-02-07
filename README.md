# json_validator
-----------

Decorator for validation of parameters sent to Flask and loaded by request.get_json()

Uses [jsonschema](https://pypi.python.org/pypi/jsonschema) for validating data.


    Args:
        params_variable: name of the argument which contains json parameters
        schema_filename: name of json file or path to the json file in which json schema is stored
        message: message returned in case of validation errors
        debug: if set to True, will raise detailed exception in case of validation errors
        
    Returns:
    	In case of validation errors returns 'message'
    	In case that validation passes it just calls wrapped function

## Instalation
Decorator can be installed using pip directly from github repository by using following command:
```
pip install git+https://github.com/sliwinski-milosz/json_validator.git@master
```

You can add it to requirements.txt file as well by adding following line:
```
git+https://github.com/sliwinski-milosz/json_validator.git@master
```

## Examples

Example 1:

```python
from json_validator import validate_params

@validate_params
def some_function(params):
    result = some_another_function(params)
    return result
```


Example 2:
```python
from json_validator import validate_params

@validate_params(schema_filename="schema1.json",
                 params_variable="params_dict",
                 message="DENIED!",
                 debug=True)
def some_function(params_dict):
    result = some_another_function(params_dict)
    return result
```

## Tests
1. To test json_validator with default system python:

  ```
  py.test
  ```

2. To test multiple python versions os iOS use [pyenv](http://www.holger-peters.de/using-pyenv-and-tox.html) and tox:

  a) prepare environment:

    ```
    brew install pyenv
    pyenv install -s 2.7.13
    pyenv install -s 3.5.3
    pyenv install -s 3.6.0
    pyenv local 2.7.13 3.5.3 3.6.0
    ```

  b) run tests:

    ```
    tox
    ```

