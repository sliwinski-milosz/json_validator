from json_validator import validate_params


@validate_params(schema_filename="my_schema.json",
                 params_variable="my_params",
                 debug=True)
def some_function(my_params):
    return my_params["param1"]


def try_valid():
    valid_params = {"param1": "some string"}
    result = some_function(valid_params)
    print(result)  # prints "some string"


def try_invalid():
    not_valid_params = {"param_name": "some string"}
    result = some_function(not_valid_params)  # raises validation exception
    print(result)


if __name__ == "__main__":
    try_valid()
    try_invalid()
