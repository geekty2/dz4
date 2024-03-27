from pprint import pprint
def get_cats_info(path: str) -> list[dict[str, str]]:
    temp = list()
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.replace("\n", ",")
            temp.append({"id": line.split(",")[0], "name": line.split(",")[1], "age": line.split(",")[2]})
    return temp


pprint(get_cats_info("qwe.txt"))
