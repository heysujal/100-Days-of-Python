count = 0
for height  in student_heights:
  count+=1

total_sum =0
for x in range(count):
  total_sum+=student_heights[x]

average_height= total_sum/count
print(f"{round(average_height)}")
