import csv

def check(n):
  with open('score.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      
      for s in row:
        if str(s) == str(n):
          return True
    return False
        
  
def register(n):

  fields=[n,0,0]

  with open(r'score.csv', 'a',newline = '') as f:
      writer = csv.writer(f)
      writer.writerow(fields)
    
  
   
def increase_score(i,msg):
  
  exist = check(i)
  i = int(i)
  if exist:
    msg_len = len(msg)
    
    lines = list()
    with open('score.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                
                if str(field) == str(i):
                  
                  copy = row.copy()
                  
                  lines.remove(row)

    with open('score.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
  
    
    
    copy[2] = int(copy[2])+msg_len 
    copy[1] = change_lvl(copy[2])
    with open(r'score.csv', 'a',newline = '') as f:
      writer = csv.writer(f)
      writer.writerow(copy)

def final_score(id):
  with open('score.csv','r') as read:
    reader = csv.reader(read)
    for row in reader:
      for f in row:
        if str(f) == str(id):
          result = "your final scre is lvl {} , exp {}".format(row[1],row[2])
          return result
    return("Register first by typing .register")


def change_lvl(exp):
    a , d = 100,100
    for i in range(1,21):
      lvl = i/2*((2*a)+((i-1)*d))
      if exp <lvl:
        return i
