#Mutations
# s = list(input())
# posichar =input().split()
# posi,char=int(posichar[0]),str(posichar[1])
# def mutate_string(s, posi, char):
#     #1st version
#     s[posi]= char
#     return "".join(s)
def mutate_string(s, posi, char):
    #shorter way:
    return s[:posi]+char+s[posi+1:]

#Text Wrap
def wrap(s, m):
    return "\n".join([s[i:i+m] for i in range(0, len(s), m)])