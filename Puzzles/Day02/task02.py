from Inputs.Reader import Reader

name: str = "input02.1.txt"
length: int
width: int
height: int

max_site: int
ribbon: list[str] = Reader(name).read_txt_to_list()

res: int = 0

for line in ribbon:
    lst: list[str] = line.strip().split('x')
    length = int(lst[0])
    width = int(lst[1])
    height = int(lst[2])
    lst_int = list(map(int, lst))
    max_site = lst_int.index(max(lst_int))
    lst_int.pop(max_site)
    res += 2*sum(lst_int)
    res += (length*width*height)

print(res)



