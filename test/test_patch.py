from unittest.mock import patch
import namespace_testing.method_holder
import namespace_testing.import_namespace
import namespace_testing.from_import


def patch_method():
    return "B"


@patch("namespace_testing.method_holder.original_method", test_method)
def test_from_import():
    assert namespace_testing.import_namespace.run_method() == "B"


@patch("namespace_testing.method_holder.original_method", test_method)
def test_import_namespace():
    assert namespace_testing.from_import.run_method() == "B"
