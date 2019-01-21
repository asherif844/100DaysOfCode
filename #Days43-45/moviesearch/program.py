import api


def main():
    results = api.find_movie_by_title(keyword='men')
    for r in results:
        print(f"There are {len(r)} movies found.")
        print(f"Title: {r.get('title')}")


if __name__ == '__main__':
    main()
