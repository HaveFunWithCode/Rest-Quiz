# Profiles REST API

REST API providing basic functionality for managing user profiles 

****Insert Question in database****

aftre migration first of all run 'insert_questions_into_database.py' script to load myquestions.csv into pages_questions table


-------------------------------------------------------------------------

**Post format**
(14 is exam id)

`{
	"examid":"14",
	"1":"2",
	"2":"1",
	"5":"4"	
}`
or 

`{
	"examid":"14",
	"1":"2",
	"2":"1",
	"3":"4",
	"4":"1",
	"5":"1"
}
`
