import inspect


class ParamsExtractor(object):

    def __init__(self, function, args, kwargs):
        '''
        Args:
            function: function from which params will be extracted
            args: args passed to above function
            kwargs: kwargs passed to above function
        '''
        self.args = args
        self.kwargs = kwargs
        self.function = function

    def get_parameters(self, params_variable):
        '''
        Extracts json parameters passed to provided function either from kwargs or args

        Args:
            params_variable: name of the argument which contains json parameters

        Returns:
            json parameters

        Raises:
            LookupError: When provided params_variable can't be found neither
                         in args or kwargs
        '''

        args_names = self.get_args_names()
        if self.params_in_kwargs(params_variable):
            return self.extract_params_from_kwarg(params_variable)
        elif self.params_in_args(args_names, params_variable):
            return self.extract_params_from_arg(args_names, params_variable)
        else:
            raise LookupError(("Parameters can't be found inside {} argument. \n"
                               "Please check if you provided correct argument name"
                               "for params_variable.").format(params_variable))

    def get_args_names(self):
        return inspect.getargspec(self.function).args

    def params_in_kwargs(self, params_variable):
        return self.kwargs and (params_variable in self.kwargs)

    def extract_params_from_kwarg(self, params_variable):
        return self.kwargs.get(params_variable)

    def params_in_args(self, args_names, params_variable):
        return args_names and params_variable in args_names

    def extract_params_from_arg(self, args_names, params_variable):
        return self.args[args_names.index(params_variable)]
