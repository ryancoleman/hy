from hy.importer import import_file_to_module, import_buffer_to_ast, MetaLoader
import os
import ast


def test_basics():
    "Make sure the basics of the importer work"
    import_file_to_module("basic",
                          "tests/resources/importer/basic.hy")


def test_stringer():
    "Make sure the basics of the importer work"
    _ast = import_buffer_to_ast("(defn square [x] (* x x))", '')
    assert type(_ast.body[0]) == ast.FunctionDef


def test_imports():
    path = os.getcwd() + "/tests/resources/importer/a.hy"
    testLoader = MetaLoader(path)

    def _import_test():
        try:
            return testLoader.load_module("tests.resources.importer.a")
        except:
            return "Error"

    assert _import_test() == "Error"
    assert _import_test() is not None
