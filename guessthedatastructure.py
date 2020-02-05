# Link to Problem:  https://open.kattis.com/problems/guessthedatastructure
import sys


# check if 2 lists are the same
def compare(list_1, list2):
    if list_1 == list2:
        return True
    else:
        return False


# figure out which one is the command for 2
def figure_it_out(reference, stack, queue, p_queue):
    r_1 = compare(reference, stack)
    r_2 = compare(reference, queue)
    r_3 = compare(reference, p_queue)

    if r_1 or r_2 or r_3:  # at least 1 is correct
        if (r_1 and r_2) or (r_1 and r_3) or (r_2 and r_3):
            # at least 2 are correct
            return "not sure"

        # only 1 is correct
        elif r_1:
            return "stack"
        elif r_2:
            return "queue"
        else:
            return "priority queue"
    else:  # none is correct
        return "impossible"


def execute_commands(start, finish, commands):
    stack_list = []
    queue_list = []
    p_queue_list = []
    truth_list = []

    stack_pop = []
    queue_pop = []
    p_queue_pop = []
    truth_pop = []

    # execute commands line by line
    for j in range(start, finish+1):
        command = int(commands[j].split()[0])
        element = int(commands[j].split()[1])

        # throw to list
        if command == 1:
            stack_list.append(element)
            queue_list.append(element)
            p_queue_list.append(element)
            truth_list.append(element)

        else:  # take one element out
            if element in truth_list:
                stack_pop.append(stack_list.pop())  # Last-In, First-Out
                queue_pop.append(queue_list.pop(0))  # First-In, First-Out

                # Remove largest
                what_to_remove = max(p_queue_list)
                p_queue_list.remove(what_to_remove)
                p_queue_pop.append(what_to_remove)

                # Truth
                truth_list.remove(element)
                truth_pop.append(element)
            else:
                return "impossible"
    return figure_it_out(truth_pop, stack_pop, queue_pop, p_queue_pop)


if __name__ == '__main__':

    lines = sys.stdin.readlines()
    number_of_lines = len(lines)

    # store the line number whose length is 1
    line_mark = []
    for i in range(number_of_lines):
        if len(lines[i].split()) == 1:
            line_mark.append(i)

    for number in line_mark:
        # Line number where we start to execute for this iteration
        begin_index = number + 1
        # Line number  where we finish
        end_index = number + int(lines[number].split()[0])
        result = execute_commands(begin_index, end_index, lines)
        print(result)

