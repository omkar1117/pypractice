# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def write_to_file(data):
    fp = open("test.txt", "w")
    for k, v in data.items():
        fp.write(f"{k} : {v}\n")
    fp.close()


def input_collect(data):
    var = input(f"Enter your {data} :")
    return var


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    data = {}
    for row in ["first_name", "last_name", "email"]:
        data[row] = input_collect(row)
    print("Final Data:", data)
    write_to_file(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
