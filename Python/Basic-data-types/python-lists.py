# https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    n = int(input())

    ar = []
    for i in range(n):
        full_cmd = input().split()

        cmd_base = full_cmd[0]
        if cmd_base == "print":
            print(ar)
            continue

        cmd_params = full_cmd[1:]

        if cmd_params:
            params = ",".join(cmd_params)
            command = "{}({})".format(cmd_base, params)
            eval("ar." + command)
        else:
            eval("ar." + cmd_base + "()")

