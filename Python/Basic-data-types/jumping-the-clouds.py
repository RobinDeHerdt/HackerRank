# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
if __name__ == '__main__':

    # 0: cumulus cloud
    # 1: thunderhead
    def jumping_on_clouds(clouds):
        return jump(clouds)

    def jump(clouds, current_cloud = 0, total_jumps = 0):

        # Big jump, if possible.
        if current_cloud + 2 < len(clouds) and clouds[current_cloud + 2] == 0:
            total_jumps += 1
            current_cloud += 2
            return jump(clouds, current_cloud, total_jumps)

        # Small jump, if possible.
        elif current_cloud + 1 < len(clouds) and clouds[current_cloud + 1] == 0:
            total_jumps += 1
            current_cloud += 1
            return jump(clouds, current_cloud, total_jumps)

        else:
            # We're at the end of the cloud sequence here.
            return total_jumps

    def assert_equals(expected, actual):
        assert expected == actual, "Expected {0} but got {1}".format(expected, actual)
        print("\033[94m [SUCCESS] {0} equals {1}".format(expected, actual))

    assert_equals(3, jumping_on_clouds([0, 1, 0, 0, 0, 1, 0]))
    assert_equals(4, jumping_on_clouds([0, 0, 1, 0, 0, 1, 0]))
    assert_equals(3, jumping_on_clouds([0, 0, 0, 0, 1, 0]))


