def assert_equals(expected, actual):
    assert expected == actual, "Expected {0} but got {1}".format(expected, actual)
    print("\033[94m [SUCCESS] {0} equals {1}".format(expected, actual))