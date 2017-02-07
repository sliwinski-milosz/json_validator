"""
Decorator for validation of json function attribute
"""

import inspect
import json
import os
from functools import wraps

from jsonschema import ValidationError, validate

from json_validator.extractor import ParamsExtractor


def validate_params(message="Wrong params!",
                    params_variable="params",
                    schema_filename="schema.json",
                    debug=False):
    """
    Decorator for validating json parameters passed to function.
    Can be used for validation of parameters sent to Flask and loaded by request.get_json().

    Args:
        message: message returned in case of validation errors
        params_variable: name of the argument which contains json parameters
        schema_filename: name of json file or path to the json file in which
                         json schema is stored
        debug: if set to True, will raise detailed exception in case of validation errors

    Returns:
        Returns {"status": message} in case of validation errors
        Returns function passed to decorator in case that validation passed
    """

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            schema = get_schema(schema_filename, function)

            params_extractor = ParamsExtractor(function, args, kwargs)
            params = params_extractor.get_parameters(params_variable)

            try:
                validate(params, schema)
            except ValidationError:
                if debug:
                    raise
                else:
                    return {"status": message}

            return function(*args, **kwargs)

        return wrapper

    if decorator_called_without_args(message):
        function, message = fix_variables(message)
        return decorator(function)

    return decorator


def get_schema(schema_filename, wrapped_function):
    abs_schema_path = get_absolute_schema_filepath(schema_filename, wrapped_function)
    with open(abs_schema_path, "r") as json_data:
        schema = json.load(json_data)
    return schema


def get_absolute_schema_filepath(schema_filename, wrapped_function):
    if os.path.isabs(schema_filename):
        schema_filepath = schema_filename
    else:
        schema_dirpath = os.path.dirname(get_module_path(wrapped_function))
        schema_filepath = os.path.join(schema_dirpath, schema_filename)
    return schema_filepath


def get_module_path(module):
    return os.path.realpath(inspect.getmodule(module).__file__)


def decorator_called_without_args(message):
    return callable(message)


def fix_variables(message):
    function = message
    message = "Wrong params!"
    return function, message
