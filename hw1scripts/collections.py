# 1-)COLLECTIONS.COUNTER()
# create counter which includes evey shoes and how many of them we have.
# if the unit of shoes are not 0 the nwe can sold them and added to money.Also lower the unit of shoes by one

from collections import Counter

nofshoes = int(input())
listofshoes = (input().split())
listofshoes = [int(i) for i in listofshoes]
counter = Counter(listofshoes)
money = 0
for i in range(int(input())):
    s, m = input().split()
    if counter[int(s)] != 0:
        money += int(m)
        counter[int(s)] -= 1

print(money)

# 2-)DEFAULTDICT TUTORIAL

# add each input as a key and their values are lists and append the index of them into this list.
# if the searched elemnt not in dict return -1 then print the indexes.
from collections import defaultdict

n, m = input().split()
dic = defaultdict(list)
for i in range(int(n)):
    dic[input()].append(str(i + 1))

for i in range(int(m)):
    x = input()
    if len(dic[x]) == 0:
        print(-1)
    else:
        print(" ".join(dic[x]))

# 3-)COLLECTIONS.NAMEDTUPLE()
# take the columnames and find it index number. then every input choose this index and find average
s = int(input())
columnames = input().split()
index = 0
for i in range(len(columnames)):
    if columnames[i] == "MARKS":
        index = i
        break
average = 0
for i in range(s):
    datas = input().split()
    average += int(datas[index])
print(average / s)

# 4-)COLLECTIONS.ORDEREDDICT()

# take the inputs and some time they are space sperated.So that use *args and then find key : value pair.
# use dictionary get method so that it does not return error
from collections import OrderedDict

ordereddict = OrderedDict()
nofevents = int(input())
for i in range(nofevents):
    x, *args = input().split()
    if len(args) > 1:
        x += " "
        x += args[0]
    ordereddict[x] = str(int(ordereddict.get(x, 0)) + int(args[-1]))
for i in ordereddict.items():
    print(" ".join(i))

# 5-)WORD ORDER
# it takes input into orddict and if there are same key value it adds +1 to its value.
from collections import OrderedDict

nofnumber = int(input())
orddict = OrderedDict()
for i in range(nofnumber):
    words = input()
    orddict[words] = orddict.get(words, 0) + 1

print(len(orddict.keys()))
for i in orddict.values():
    print(i, end=" ")

# 6-)COLLECTIONS.DEQUE()

# by using getattr function implement each method and their parameter  to deque class.
from collections import deque

d = deque()
for _ in range(int(input())):
    x, *args = input().split()
    getattr(d, x)(*(int(i) for i in args))
print(*d)

# 7-)COMPANY LOGO

##thanks to sorted function it remmebers input list posstion. So that first sort by alphabet and then number of occurences by reversed order.
# !/bin/python3
from collections import Counter
from operator import itemgetter

if __name__ == '__main__':
    s = [i for i in input()]
    counter = Counter(s)
    liste = []
    for i in counter:
        liste.append((i, counter[i]))
    liste = sorted(liste, key=itemgetter(0))
    liste = sorted(liste, key=itemgetter(1), reverse=True)[:3]
    for i in liste:
        print(*i)
