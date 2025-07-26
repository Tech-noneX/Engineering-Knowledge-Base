from pathlib import Path


lists_methods_paths = {
    'append': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'append_method.md',
    'extend': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'extend_method.md',
    'sort': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'sort_method.md',
    'split': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'split_method.md',
    'insert': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'insert_method.md',
    'index': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'index_method.md',
    'pop': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'pop_method.md',
    'remove': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'remove_method.md',
    }


lists_function_paths = {
    'sorted': Path(__file__).parent.parent/'docs'/'lists'/'functions'/'sorted_function.md',
    }


dict_methods_paths = {
    'get': Path(__file__).parent.parent/'docs'/'dictionaries'/'methods'/'get_method.md'
}


string_methods = {
    'upper': Path(__file__).parent.parent/'docs'/'strings'/'methods'/'upper_method.md',    
    'lower': Path(__file__).parent.parent/'docs'/'strings'/'methods'/'lower_method.md',
    'title': Path(__file__).parent.parent/'docs'/'strings'/'methods'/'title_method.md',
    'lstrip': Path(__file__).parent.parent/'docs'/'strings'/'methods'/'lstrip_method.md',
    'rstrip': Path(__file__).parent.parent/'docs'/'strings'/'methods'/'rstrip_method.md',
    'strip': Path(__file__).parent.parent/'docs'/'strings'/'methods'/'strip_method.md',
    'removeprefix': Path(__file__).parent.parent/'docs'/'strings'/'methods'/'removeprefix_method.md',
    'removesuffix': Path(__file__).parent.parent/'docs'/'strings'/'methods'/'removesuffix_method.md',
    'replace': Path(__file__).parent.parent/'docs'/'strings'/'methods'/'replace_method.md',
    'capitalize': Path(__file__).parent.parent/'docs'/'strings'/'methods'/'capitalize_method.md',
}


built_in = {
    'min': Path(__file__).parent.parent/'docs'/'builtins'/'min_function.md',
    'max': Path(__file__).parent.parent/'docs'/'builtins'/'max_function.md',
    'len': Path(__file__).parent.parent/'docs'/'builtins'/'len_function.md',
    'sum': Path(__file__).parent.parent/'docs'/'builtins'/'sum_function.md',
    'range': Path(__file__).parent.parent/'docs'/'builtins'/'range_function.md',
    'reversed': Path(__file__).parent.parent/'docs'/'builtins'/'reversed_function.md',
    'round': Path(__file__).parent.parent/'docs'/'builtins'/'round_function.md',
    'enumerate': Path(__file__).parent.parent/'docs'/'builtins'/'enumerate_function.md',
    'print': Path(__file__).parent.parent/'docs'/'builtins'/'print_function.md',
    'type': Path(__file__).parent.parent/'docs'/'builtins'/'type_function.md',
    'input': Path(__file__).parent.parent/'docs'/'builtins'/'input_function.md',
    'zip': Path(__file__).parent.parent/'docs'/'builtins'/'zip_function.md',
}


modules = {'functools module':{'reduce': Path(__file__).parent.parent/'docs'/'modules'/'functools'/'reduce_functools.md',
                               'functools': Path(__file__).parent.parent/'docs'/'modules'/'functools'/'functools_module.md',
                        }}


print(len(lists_function_paths) + len(lists_methods_paths) + len(dict_methods_paths) + len(built_in) + len(string_methods))