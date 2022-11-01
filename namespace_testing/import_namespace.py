import namespace_testing.method_holder

def run_method():
    return_value = namespace_testing.method_holder.original_method()
    return return_value


if __name__ == "__main__":
    run_method()
