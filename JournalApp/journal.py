import os

def load(name):
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                # print('would load: '+entry.rstrip())
                data.append(entry.rstrip())
    return data

def save(name, journal_data):
    # filename = './journals/'+name+'.jrl'
    filename = get_full_pathname(name)
     
    print('.......saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry+'\n')

def get_full_pathname(name):
    filename = os.path.join(
        '/Users/asherif844/p_v_e/100DaysOfCode/JournalApp/journals/', name+'.jrl')
    return filename
    # fout.close()

def add_entry(text, journal_data):
    journal_data.append(text)
