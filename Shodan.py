import time

import shodan


def save_data(result):
    with open('results.txt', 'w') as fp:
        for item in result:
            for tt in item[2]:
                fp.write(item[0][0] + ", " + item[1] + ", " + str(tt) + "\n")

        print('Done')


def load_data(file_path):
    f = open(file_path, "r")
    e = f.read().split()
    print(e)
    search_list = []
    for i in range(len(e)):
        listt = [e[i]]
        search_list.append(listt)
    return search_list


def main():
    search_list = load_data("file.txt")
    api = shodan.Shodan("OFlmGFr75bhWQiulF8OBKNrKvZOUPTCA")
    sec_waits = 2
    timestart = time.time_ns()
    print('Expected Remaining Time: ', (sec_waits+2) * len(search_list), "seconds.")
    print(timestart / (10 ** 9))
    full_list = []
    for i in range(len(search_list)):
        if (i + 1) % 10 == 0:
            print('Expected Remaining Time: ', sec_waits * (len(search_list) - i + 1), "seconds. At", str(i + 1), "/",
                  len(search_list))
        try:
            result = api.host(search_list[i], minify=True)

            print(str(i + 1), search_list[i], result['last_update'], result['ports'])
            full_list.append([search_list[i], result['last_update'], result['ports']])
            time.sleep(sec_waits)
        except:
            time.sleep(1)
            continue

    print(full_list)
    save_data(full_list)
    print((time.time_ns() - timestart) / (10 ** 9))


if __name__ == '__main__':
    main()
