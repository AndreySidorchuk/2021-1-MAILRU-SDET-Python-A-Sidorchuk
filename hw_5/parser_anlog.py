import argparse
import json

file = open('access.log', 'r')
requests = file.readlines()
for i in range(len(requests)):
    requests[i] = requests[i].split()
file.close()

parser = argparse.ArgumentParser()
parser.add_argument('--json', action='store_true')
args = parser.parse_args()


def all_requests():
    return len(requests)


def count_by_type(req_type):
    count = 0
    for req in requests:
        if req[5][1:] == req_type:
            count += 1
    return count


def requests_type_count():
    types = set()
    for req in requests:
        types.add(req[5][1:])
    result = dict()
    for type in types:
        result[type] = count_by_type(type)
    return result


def top_requests_by_size():
    sorted_req = sorted(requests,
                        key=lambda req: int(req[9].replace('-', '0')),
                        reverse=True)
    top_requests = []
    for i in range(5):
        new_req = ' '.join([sorted_req[i][6], sorted_req[i][8], sorted_req[i][9]])
        top_requests.append(new_req)
    return top_requests


def top_5_requests_with_client_error():
    url_to_count = dict()
    error_req = []
    result = []
    for req in requests:
        if (400 <= int(req[8]) < 500):
            error_req.append(req)
            if req[6] in url_to_count:
                url_to_count[req[6]] += 1
            else:
                url_to_count[req[6]] = 1
    url_to_count = {k: v for k, v in sorted(url_to_count.items(), key=lambda item: item[1], reverse=True)}

    urls = list(url_to_count.keys())[:5]
    for url in urls:
        for req in error_req:
            if req[6] == url:
                new_req = ' '.join([req[0], req[8], req[6]])
                result.append(new_req)
                break
    return result


def top_5_requests_with_server_error():
    error_req = []
    result = []
    for req in requests:
        if (500 <= int(req[8]) < 600):
            error_req.append(req)
    top_req = sorted(error_req, key=lambda req: int(req[9].replace("-", "0")), reverse=True)[:10]
    for i in range(5):
        new_req = " ".join([top_req[i][0], top_req[i][6], top_req[i][8]])
        result.append(new_req)
    return result


def write_in_file():
    result = open("result_parser.txt", 'w')
    print("Count all requests  ", all_requests(), "\n", file=result)
    print("Requests   count", file=result)

    for req, count in requests_type_count().items():
        print(req, count, sep="  ", file=result)
    print("", file=result)

    print("Top requests by size", file=result)
    print(*top_requests_by_size(), sep="\n", file=result)
    print("", file=result)

    print("Top 5 requests with client error", file=result)
    print(*top_5_requests_with_client_error(), sep="\n", file=result)
    print("", file=result)

    print("Top 5 requests with server error", file=result)
    print(*top_5_requests_with_server_error(), sep="\n", file=result)

    if args.json:
        json_file = open('result.json', 'w')
        json.dump([all_requests(), requests_type_count(), top_requests_by_size(),
                   top_5_requests_with_client_error(), top_5_requests_with_server_error()], json_file,
                  indent=4)
        json_file.close()

    result.close()

write_in_file()