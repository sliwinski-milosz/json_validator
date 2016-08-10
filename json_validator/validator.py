"""
Decorator for validation of json parameters sent to Flask
"""

from jsonschema import validate, ValidationError
from functools import wraps
import json
import inspect
import os

__author__ = "sliwinski.milosz@gmail.com"
__version__ = "0.2"


def validate_params(message="Wrong params!",
                    params_variable="params",
                    schema_filename="schema.json",
                    debug=False):
    """
    Decorator for validation of parameters sent to Flask and loaded by request.get_json()

    Args:
        params_variable: name of the argument which contains json parameters
        schema_filename: name of json file or path to the json file in which json schema is stored
        message: message returned in case of validation errors
        debug: if set to True, will raise detailed exception in case of validation errors

    Returns:
        Returns {"status": message} in case of validation errors
        Returns function passed to decorator in case that validation passed
    """
    

    def decorator(function):
        @wraps(function)
        
        def wrapper(*args, **kwargs):
            
            if os.path.isabs(schema_filename):
                schema_filepath = schema_filename
            else:
                # as module can be call from any place
                # get absolute path to the module
                schema_dirpath = os.path.dirname(os.path.realpath(inspect.getmodule(function).__file__))
                schema_filepath = os.path.join(schema_dirpath,schema_filename)
            schema = json.load(open(schema_filepath,"r"))
            params = get_parameters(params_variable, function, args, kwargs)

            try:
                validate(params, schema)
            except ValidationError:
                if not debug:
                    return {"status": message}
                else:
                    raise

            return function(*args, **kwargs)
        
        return wrapper

    def get_parameters(params_variable,function,args,kwargs):
        '''
        Parameters can be stored inside either args or kwargs arguments
        This function looks inside kwargs for them, in case that they
        are not there, it will try to extract them from args.

        Args:
            params_variable: name of the argument which contains json parameters
            function: function which args and kwargs will be checked

        Returns:
            json_object: json parameters

        Raises:
            Exception: When provided params_variable can't be found neither
                       in args or kwargs
        '''

        if kwargs and params_variable in kwargs:
            params = kwargs.get(params_variable)
            return params
        else:
            argspec_args = inspect.getargspec(function).args
            if argspec_args  and params_variable in argspec_args:
#                 print argspec_args
#                 print params_variable
#                 print args
                params = args[argspec_args.index(params_variable)]
                return params

        raise Exception( ("Parameters can't be found inside {} argument. \n"
                          "Please check if you provided correct argument name for params_variable.").format(params_variable))
        

    if callable(message):
        # No arguments, this is the decorator
        # Set default values for the arguments
        function = message
        message = "Wrong params!"
        return decorator(function)
    else:
        return decorator

    return decorator
