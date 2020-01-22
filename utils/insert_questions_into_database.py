import psycopg2
import csv
conn = psycopg2.connect(host="localhost",
                        database="restq",
                        user="quizuser",
                        password="123")
curs = conn.cursor()

reader=csv.reader(open("myquestions.csv"))
firstline = True
with open("myquestions.csv") as f:
    next(f)
    for l in f:
        text,c1,c2,c3,c4,correct_choice_Id=l.split(',')
        correct=int(correct_choice_Id.replace('\n',''))
        curs.execute("""INSERT INTO quizservice_questions ( text , c1 , c2 , c3 , c4 , correct_choice_id) VALUES (%s, %s, %s, %s, %s, %s); """,(text,c1,c2,c3,c4,correct))


        # data = [('text', text), ('c1', c1), ('c2', c2), ('c3', c3), ('C4', c4),('correct_choice_Id', correct)]
        # data = dict(data)
        # cols = ",".join(data.keys())
        # values = ",".join("'" + v + "'" if type(v) is str else str(v) for v in data.values())
        # curs.execute("INSERT INTO pages_questions (%s) VALUES (%s)" % (cols, values))
        conn.commit()

