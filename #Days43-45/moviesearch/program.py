import api


def main():
    keyword = input('Keyword of Title Search: ')
    results = api.find_movie_by_title(keyword)
    print(f"There are {len(results)} movies found:")
    for r in results:

        print(f"{r.title}")


if __name__ == '__main__':
    main()
