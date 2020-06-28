import csv
#for reading a file
with open("scores.txt", "r") as scoreFile:
    scoreFileReader =csv.reader (scoreFile)
    scoreList = []
    
    for row in scoreFileReader:
        if len (row) != 0:
            scoreList = scoreList + [row]

scoreFile.close()

print(scoreList)
#for writing a file it will be stored on entercontent file 
name = input("Enter name: ")
age = input("Enter age: ")
score = input("score: ")
gender = input("gender: ")

with open("entercontent.txt", "w") as scoreFile:
    scoreFileWriter = csv.writer (scoreFile)
    scoreFileWriter.writerow([name,age,score,gender])

scoreFile.close()

#for searching content based on title like name,age,gender (it will search contents from scores file)

with open("scores.txt", "r") as scoreFile:
    gender = input("Enter Gender to be searched: ")
    scoreFileReader =csv.reader(scoreFile)
    for row in scoreFileReader:
        for field in row:
            if field == gender:
               print(row)
                
scoreFile.close()

