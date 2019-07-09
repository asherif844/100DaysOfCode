import journal


def main():
    print_header()
    run_event_loop()

def print_header():
    print('-------------------')
    print('    Journal App    ')
    print('-------------------')

def run_event_loop():
    print('What do you want to do with your journal?')
    
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)
    while cmd !='x':

        cmd = input('[L]ist Entry, [A]dd Entry, or E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entry(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print('Sorry, {} is not a valuable option, please try again!'.format(cmd))
            continue
    print('Done, goodbye!')
    journal.save(journal_name, journal_data)

def list_entry(data):
    print('Your Journal Entries so far: ')
    reverse_entries = reversed(data)
    for idx, entry in enumerate(reverse_entries):
        print('* [{}], {}'.format(idx+1, entry))

def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text)

main()
