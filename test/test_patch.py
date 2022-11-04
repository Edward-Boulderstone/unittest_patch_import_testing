from unittest.mock import patch
import namespace_testing.method_holder
import namespace_testing.import_namespace
import namespace_testing.from_import


def patch_method():
    return "B"


@patch("namespace_testing.method_holder.original_method", patch_method)
def test_import_namespace():
    assert namespace_testing.import_namespace.run_method() == "B"

@patch("namespace_testing.from_import.original_method", patch_method)
def test_from_import():
    # Comment out top level import and uncomment this import for some funky behaviour
    assert namespace_testing.from_import.run_method() == "B"
