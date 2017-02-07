# json_validator
-----------------

Decorator for validating json parameters passed to function.
Can be used for validation of parameters sent to Flask and loaded by `request.get_json()`.

Uses [jsonschema](https://pypi.python.org/pypi/jsonschema) for validating data.

## Instalation

```
pip install json_validator
```

## Parameters

    Args:
        message: message returned in case of validation errors
        params_variable: name of the argument which contains json parameters
        schema_filename: name of json file or path to the json file in which
                            json schema is stored
        debug: if set to True, will raise detailed exception in case of validation errors

    Returns:
        Returns {"status": message} in case of validation errors
        Returns function passed to decorator in case that validation passed


## Decorator defaults

```python
@validate_params(message="Wrong params!",
                 params_variable="params",
                 schema_filename="schema.json",
                 debug=False)
```

## Usage Examples

You can find examples of usage in `./examples` directory.

Below you can find simplest usage examples:

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

2. To test multiple python versions on OS X use `pyenv` and `tox`:

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

