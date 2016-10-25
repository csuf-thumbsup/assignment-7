def run_parser(parsing_table, input_str, terminals, starting_non_terminal):
    str_list = list(input_str)
    stack = ['$', starting_non_terminal] # initialize stack to $ and the starting non-terminal

    i = 0
    read_char = str_list[i] # init read_char to first char

    while(True):

        # pop the stack on every iteration and store into popped_char
        popped_char = stack.pop()

        # immediate check if the popped_char is a terminal
        if popped_char in terminals:
            # we found a match
            print('match: ' + popped_char + '\tstack: '+ stack.__str__())
            i = i + 1
            read_char = str_list[i]
            continue
        elif popped_char == '$':
            # check for end of string. If we got here then you're good to go!
            print('\nYour string IS valid:', input_str)
            exit(0)

        # find [popped_char, read_char] in our parsing_table
        temp_parsed_value = parsing_table[popped_char][read_char]

        # our checks and balances
        if temp_parsed_value == 'undef':
            print('Your string is NOT valid for the given language!:', input_str)
            exit(1)
        elif temp_parsed_value == 'λ':
            # skip and loop back to top
            continue
        else:
            # we found a valid value
            # just put back on the stack even if its a terminal
            reversed_value = temp_parsed_value[::-1]
            for x in reversed_value:
                # push the values in reverse order
                stack.append(x)

if __name__ == '__main__':
    '''
    Data for Problem #1

    parsing_table = {
        'E': {'i': 'TQ',
              '+': 'undef',
              '-': 'undef',
              '*': 'undef',
              '/': 'undef',
              '(': 'TQ',
              ')': 'undef',
              '$': 'undef'
              },
        'Q': {'i': 'undef',
              '+': '+TQ',
              '-': '-TQ',
              '*': 'undef',
              '/': 'undef',
              '(': 'undef',
              ')': 'λ',
              '$': 'λ'
              },
        'T': {'i': 'FR',
              '+': 'undef',
              '-': 'undef',
              '*': 'undef',
              '/': 'undef',
              '(': 'FR',
              ')': 'undef',
              '$': 'undef'
              },
        'R': {'i': 'undef',
              '+': 'λ',
              '-': 'λ',
              '*': '*FR',
              '/': '/FR',
              '(': 'undef',
              ')': 'λ',
              '$': 'λ'
              },
        'F': {'i': 'i',
              '+': 'undef',
              '-': 'undef',
              '*': 'undef',
              '/': 'undef',
              '(': '(E)',
              ')': 'undef',
              '$': 'undef'
              }
    }

    # don't include $ since it's the Ending Terminal
    terminals = ['i', '+', '-', '*', '/', '(', ')']
    input_str = '(i+i)*i$'
    starting_non_terminal = 'E'
    '''

    # Data for Problem #2
    parsing_table = {
        'S': {'a': 'F=E',
              'b': 'F=E',
              '(': 'F=E',
              ')': 'undef',
              '+': 'undef',
              '*': 'undef',
              '$': 'undef',
              '=': 'undef'
              },
        'E': {'a': 'TQ',
              'b': 'TQ',
              '(': 'TQ',
              ')': 'undef',
              '+': 'undef',
              '*': 'TQ',
              '$': 'undef',
              '=': 'undef'
              },
        'Q': {'a': 'undef',
              'b': 'undef',
              '(': 'undef',
              ')': 'λ',
              '+': '+TQ',
              '*': 'undef',
              '$': 'λ',
              '=': 'undef'
              },
        'T': {'a': 'FR',
              'b': 'FR',
              '(': 'FR',
              ')': 'undef',
              '+': 'undef',
              '*': 'undef',
              '$': 'undef',
              '=': 'undef'
              },
        'R': {'a': 'λ',
              'b': 'λ',
              '(': 'λ',
              ')': 'undef',
              '+': 'λ',
              '*': '*FR',
              '$': 'λ',
              '=': 'undef'
              },
        'F': {'a': 'a',
              'b': 'b',
              '(': '(E)',
              ')': 'undef',
              '+': 'undef',
              '*': 'undef',
              '$': 'undef',
              '=': 'undef'
              }
    }
    terminals = ['a', 'b', '(', ')', '+', '=', '*']
    input_str = 'a=(a+a)*b$'
    starting_non_terminal = 'S'

    run_parser(parsing_table, input_str, terminals, starting_non_terminal)
