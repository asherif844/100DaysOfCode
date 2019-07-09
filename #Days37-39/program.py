import research


def main():
    research.init()
    print('Weather Research for Seattle 2014-2015')
    print()
    # todo: initialize the data
    print('The average mean temperature is: ')
    print(research.init()[0])
    print()
    print('The five hottest days of the year are (descending): ')
    print(f'{research.init()[1]} with a temperature of {research.init()[2]}')
    days = research.hot_days()
    for idx, d in enumerate(days[:5]):
        print("{}. {} F on {}".format(idx+1, d.actual_max_temp, d.date))


if __name__ == '__main__':
    main()
