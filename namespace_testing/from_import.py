from namespace_testing.method_holder import original_method


def run_method():
    return_value = original_method()
    return return_value


if __name__ == "__main__":
    run_method()
