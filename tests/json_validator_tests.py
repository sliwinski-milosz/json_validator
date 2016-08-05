import unittest
import os
from json_validator.validator import validate_params,ValidationError

arg1 = "something"
arg2 = "something_else"

schema_dirpath = os.path.dirname(os.path.realpath(__file__))
schema_filepath = os.path.join(schema_dirpath,"schema.json")

correct_params = {"param1": "some string",
                  "param2": ["string_in_array","string_in_array2"]}

wrong_params =  {"param1": ["string_in_array","string_in_array2"],
                 "param2": "string"}

class JsonValidatorTest(unittest.TestCase):
    
    def test_default_params_parameter(self):
        
        @validate_params(schema_filename=schema_filepath)
        def test_function_default_params_arg(arg1,arg2,params):
            return "Returned by function"
        
        self.assertEqual(test_function_default_params_arg(arg1,arg2,correct_params),"Returned by function")
        self.assertEqual(test_function_default_params_arg(arg1,arg2,wrong_params),{'status': 'Wrong params!'})
        
        
    def test_non_default_params_parameter(self):
        
        @validate_params(schema_filename=schema_filepath,
                         params_variable="params_test")
        def test_function_default_params_arg(arg1,arg2,params_test):
            return "Returned by function"
        
        self.assertEqual(test_function_default_params_arg(arg1,arg2,correct_params),"Returned by function")
        self.assertEqual(test_function_default_params_arg(arg1,arg2,wrong_params),{'status': 'Wrong params!'})
        
    def test_debug(self):
        @validate_params(schema_filename=schema_filepath,
                         debug=True)
        def test_function_default_params_arg(arg1,arg2,params):
            return "Returned by function"
        
        with self.assertRaises(ValidationError):
            test_function_default_params_arg(arg1,arg2,wrong_params)
            
    def test_message(self):
        @validate_params(schema_filename=schema_filepath,
                         message="Message test!")
        def test_function_default_params_arg(arg1,arg2,params):
            return "Returned by function"
        
        self.assertEqual(test_function_default_params_arg(arg1,arg2,wrong_params),{'status': 'Message test!'})
        
    def test_decorator_without_arguments(self):
        @validate_params
        def test_function_default_params_arg(arg1,arg2,params):
            return "Returned by function"
         
        self.assertEqual(test_function_default_params_arg(arg1,arg2,correct_params),"Returned by function")
        self.assertEqual(test_function_default_params_arg(arg1,arg2,wrong_params),{'status': 'Wrong params!'})

def save_schema_to_json():
    '''
    Save some example schema to json file
    '''
    import json
    schema = {
        "required": [
            "param1"
        ],
        "type": "object",
        "properties": {
            "param1": {
                "type": "string"
            },
            "param2": {
                "type": "array"
            }
        }
    }
    with open("schema.json","w") as jsonout:
        json.dump(schema,jsonout,indent=4)
        
        
if __name__ == '__main__':
    unittest.main()