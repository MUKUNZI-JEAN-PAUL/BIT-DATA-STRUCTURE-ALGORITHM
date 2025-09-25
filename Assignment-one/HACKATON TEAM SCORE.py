
marks=[60,65,70,75,80,85,90]
total = sum(marks)
average =  total/len(marks)
minimum = min(marks)
maximum = max(marks)
print("=====integers=====")
print(f"Total",total)
print(f"Average",average)
print(f"Minimum",minimum)
print(f"Maximum",maximum)
print("====string=====")
print("Hackaton team marks REPORT")
report = (
    f"Hackaton has {len(marks)} team."

    f"the total marks is  {total} ,with an average of  {average}"
)
print(report+"\n")
print("====boolean====")
print("Hackaton check")
threshold = 65
if average> threshold :
    print("above the standard")
else:
    print("below the standard")
    print("======list=====")
    print("Hackaton list")
    print(f"original marks list:",marks)
marks.append (78)
print(f"after adding new marks",marks)
marks=[b for b in marks if b>70]
print(f"after removing marks",marks)
marks.sort()
print(f"sorted marks:{marks}\n")
print("=====arrray====")
import array
array=array.array('i',[75, 78, 80, 85, 90])
print(f"Array: {array}")
array_sum = sum(array)
print(f"Sum of array: {array_sum}")
print(f"Compare with list total ({total}): {array_sum ==
total}\n")

print("=====dictionary====")
teams = [
 {"id": 1, "Paul": "Team white", "value": 78},
 {"id": 2, "Peter": "Team green", "value": 85},
 {"id": 3, "Thomas": "Team yellow", "value": 92},
]

print("teams dictionary:",teams)
teams [0]["value"]=80
print(f"Updated teams: {teams}")
teams=[t for t in teams if t["id"]!=2]
print(f"update teams after removing:{teams}")
dict_total= sum (teams['value']for teams in teams)

print(f"update teams after sum:{dict_total}")