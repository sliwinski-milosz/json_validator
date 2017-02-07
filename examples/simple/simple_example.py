from json_validator import validate_params


@validate_params
def some_function(params):
    return params["param1"]


def try_valid():
    valid_params = {"param1": "some string",
                    "param2": ["string_in_array", "string_in_array2"]}
    result = some_function(valid_params)
    print(result)  # prints "some string"


def try_invalid():
    not_valid_params = {"param1": ["string_in_array", "string_in_array2"],
                        "param2": "string"}
    result = some_function(not_valid_params)
    print(result)  # prints "{'status': 'Wrong params!'}"


if __name__ == "__main__":
    try_valid()
    try_invalid()
