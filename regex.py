input1 = input()
list_input = list(input1)
print(list_input)
final_list = []
if list_input[0:4] == ['h', 't', 't', 'p']:
    for i in range(4):
        final_list.append(list_input[i])
    for i in range(4):
        list_input.pop(0)
    final_list.append("://")
    for i in range(len(list_input)):
        if list_input[i] == "r" and list_input[i + 1] == "u":
            index = i

            for j in range(index):
                final_list.append(list_input[j])
            final_list.append(".ru/")
    for i in range(index + 2):
        list_input.pop(0)
    for element in range(len(list_input)):
        final_list.append(list_input[element])
    ira="".join(final_list)
    print(ira)

elif list_input[0:3] == ['f', 't', 'p']:
    for i in range(3):
        final_list.append(list_input[i])
    for i in range(3):
        list_input.pop(0)
    final_list.append("://")
    for i in range(len(list_input)):
        if list_input[i] == "r" and list_input[i + 1] == "u":
            index = i
            print(index)
            for j in range(index):
                final_list.append(list_input[i])
            final_list.append(".ru/")
    for i in range(index + 2):
        list_input.pop(0)
    for element in range(len(list_input)):
        final_list.append(list_input[element])

    print(final_list)
    print(list_input)