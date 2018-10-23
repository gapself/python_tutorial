# #Mutations
# # s = list(input())
# # posichar =input().split()
# # posi,char=int(posichar[0]),str(posichar[1])
# # def mutate_string(s, posi, char):
# #     #1st version
# #     s[posi]= char
# #     return "".join(s)
# def mutate_string(s, posi, char):
#     #shorter way:
#     return s[:posi]+char+s[posi+1:]
#
# #Text Wrap
# def wrap(s, m):
#     return "\n".join([s[i:i+m] for i in range(0, len(s), m)])
#
# #Swap Case
# def swap_case(s):
#     return s.swapcase()
#
# #Find a String
# def count_substring(string, substring):
#     long=len(string)
#     short=len(substring)
#     sum=0
#     for i in range(long-short+1):
#         if string[i:i+short] == substring:
#             sum += 1
#     return sum
#
# #find the second max value
# n = int(input())
# arr = list(map(int, input().split()))
# removed=max(arr)
# while max(arr)==removed:
#     arr.remove(max(arr))
# print(max(arr))


