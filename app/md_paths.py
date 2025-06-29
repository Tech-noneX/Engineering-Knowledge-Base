from pathlib import Path


lists_methods_paths = {
    'append': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'append_method.md',
    'extend': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'extend_method.md',
    'sort': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'sort_method.md',
    'split': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'split_method.md',
    'insert': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'insert_method.md',
    'index': Path(__file__).parent.parent/'docs'/'lists'/'methods'/'index_method.md'
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
    'min': Path(__file__).parent.parent/'docs'/'builtins'/'min_function.md'
}