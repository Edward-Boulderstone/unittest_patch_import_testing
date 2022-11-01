from unittest.mock import Mock
import namespace_testing.method_holder
import namespace_testing.import_namespace
import namespace_testing.from_import

def test_from_import():
    namespace_testing.method_holder.original_method = Mock(return_value='B')
    assert namespace_testing.import_namespace.run_method() == "B"


def test_import_namespace():
    namespace_testing.method_holder.original_method = Mock(return_value='B')
    assert namespace_testing.from_import.run_method() == "B"
