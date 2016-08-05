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

## INSTALLATION
Decorator can be installed using pip directly from github repository by using following command:
```
pip install git+https://github.com/sliwinski-milosz/json_validator.git@master
```

You can add it to requirements.txt file as well by adding following line:
```
git+https://github.com/sliwinski-milosz/json_validator.git@master
```

## EXAMPLES

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

## TESTS
```
python -m tests.json_validator_tests
```
