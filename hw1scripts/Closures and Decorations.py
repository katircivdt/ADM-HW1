#1-)STANDARDIZE MOBILE NUMBER USING DECORATORS
def wrapper(f):
    def fun(l):
        newlist=[]
#create list without this part(+91)
        for i in l:
            if len(str(i)) == 13:
                newlist.append(i[3:])
            elif len(str(i)) == 12:
                newlist.append(i[2:])
            elif len(str(i)) == 11:
                newlist.append(i[1:])
            else:
                newlist.append(i)
 #(return f function and create +91 part and divide number into parts)
        f("+91 {} {}".format(str(rows[:5]),str(rows[5:])) for rows in newlist)
    return fun

#2-)DECORATORS 2 - NAME DIRECTORY
import operator
def person_lister(f):
    def inner(people):
        people=[[i[0],i[1],int(i[2]),i[3]] for i in people]
        x=sorted(people,key=operator.itemgetter(2))

        holder=[]
        for i in x:
#here i append function output to the holder list so that below code, because of * symbol,gives true output
            holder.append(f(i))
        return holder
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')