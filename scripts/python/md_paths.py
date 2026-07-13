"""Paths used by the Python reference-card browser."""

from pathlib import Path


PYTHON_DOCS = Path(__file__).resolve().parents[2] / "docs" / "python"


def doc_path(*parts: str) -> Path:
    """Build an absolute path to a Python reference card."""
    return PYTHON_DOCS.joinpath(*parts)


lists_methods_paths = {
    "append": doc_path("lists", "methods", "append_method.md"),
    "extend": doc_path("lists", "methods", "extend_method.md"),
    "sort": doc_path("lists", "methods", "sort_method.md"),
    "split": doc_path("lists", "methods", "split_method.md"),
    "insert": doc_path("lists", "methods", "insert_method.md"),
    "index": doc_path("lists", "methods", "index_method.md"),
    "pop": doc_path("lists", "methods", "pop_method.md"),
    "remove": doc_path("lists", "methods", "remove_method.md"),
    "count": doc_path("lists", "methods", "count_method.md"),
    "reverse": doc_path("lists", "methods", "reverse_method.md"),
}

datatypes_paths = {
    "list": doc_path("data-types", "list_datatype.md"),
    "bool": doc_path("data-types", "bool_datatype.md"),
    "dict": doc_path("data-types", "dict_datatype.md"),
    "float": doc_path("data-types", "float_datatype.md"),
    "int": doc_path("data-types", "int_datatype.md"),
    "set": doc_path("data-types", "set_datatype.md"),
    "str": doc_path("data-types", "str_datatype.md"),
    "tuple": doc_path("data-types", "tuple_datatype.md"),
}

lists_function_paths = {
    "sorted": doc_path("lists", "functions", "sorted_function.md"),
}

dict_methods_paths = {
    "get": doc_path("dictionaries", "methods", "get_method.md"),
}

string_methods = {
    "upper": doc_path("strings", "methods", "upper_method.md"),
    "lower": doc_path("strings", "methods", "lower_method.md"),
    "title": doc_path("strings", "methods", "title_method.md"),
    "lstrip": doc_path("strings", "methods", "lstrip_method.md"),
    "rstrip": doc_path("strings", "methods", "rstrip_method.md"),
    "strip": doc_path("strings", "methods", "strip_method.md"),
    "removeprefix": doc_path("strings", "methods", "removeprefix_method.md"),
    "removesuffix": doc_path("strings", "methods", "removesuffix_method.md"),
    "replace": doc_path("strings", "methods", "replace_method.md"),
    "capitalize": doc_path("strings", "methods", "capitalize_method.md"),
    "join": doc_path("strings", "methods", "join_method.md"),
    "find": doc_path("strings", "methods", "find_method.md"),
    "partition": doc_path("strings", "methods", "partition_method.md"),
    "endswith": doc_path("strings", "methods", "endswith_method.md"),
    "format": doc_path("strings", "methods", "format_method.md"),
}

built_in = {
    "min": doc_path("builtins", "min_function.md"),
    "max": doc_path("builtins", "max_function.md"),
    "len": doc_path("builtins", "len_function.md"),
    "sum": doc_path("builtins", "sum_function.md"),
    "range": doc_path("builtins", "range_function.md"),
    "reversed": doc_path("builtins", "reversed_function.md"),
    "round": doc_path("builtins", "round_function.md"),
    "enumerate": doc_path("builtins", "enumerate_function.md"),
    "print": doc_path("builtins", "print_function.md"),
    "type": doc_path("builtins", "type_function.md"),
    "input": doc_path("builtins", "input_function.md"),
    "zip": doc_path("builtins", "zip_function.md"),
    "map": doc_path("builtins", "map_function.md"),
    "filter": doc_path("builtins", "filter_function.md"),
}

set_method = {
    "add": doc_path("sets", "method", "add_method.md"),
    "union": doc_path("sets", "method", "union_method.md"),
}

modules = {
    "functools module": {
        "reduce": doc_path("modules", "functools", "reduce_functools.md"),
        "functools": doc_path("modules", "functools", "functools_module.md"),
    },
}

all_paths = [
    lists_methods_paths,
    datatypes_paths,
    lists_function_paths,
    dict_methods_paths,
    string_methods,
    built_in,
    set_method,
    modules,
]


if __name__ == "__main__":
    print(f"Python documentation root: {PYTHON_DOCS}")
