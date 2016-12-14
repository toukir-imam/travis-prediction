
import pickle
f = open("travistorrent.csv")
head =-10000
titles = f.readline()
titles = titles.strip().split(",")
titles = [i.strip("\"") for i in titles]
project_names ={}
print(titles)
for i in f :
	i = i.strip().split(",")
	i = [z.strip("\"") for z in i]
	if i[2] not in project_names :#and i[3]=="TRUE":
		project_names[i[2]] = 0
	else:
	#elif i[3] == "TRUE":
		project_names[i[2]]+=1
	head -=1
	if head == 0:
		break
		
for key in project_names:
	print(key)
print(len(project_names.keys()))
total = 0

for key ,value in project_names.iteritems():
	total+=value

print(total/len(project_names.keys()))
