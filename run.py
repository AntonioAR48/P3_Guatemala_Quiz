questions = [
{
   "prompt": "What is the meaning of the word Guatemala?",
   "options": ["A. Place of many trees", "B. Place of many rivers ", "C. Place of many mountains", "D. Place of many rocks"],
   "answer": "A"
},
{
   "prompt": "How many volcanoes there are in Guatemala?",
   "options": ["A. 35", "B. 36 ", "C. 37", "D. 38"],
   "answer": "C"
},
{
   "prompt": "What is Guatemala's national bird?",
   "options": ["A. Vireonidae", "B. Antbird", "C. Gnatcatcher", "D. Quetzal"],
   "answer": "D"
},
{
   "prompt": "What is the name of Guatemala's president?",
   "options": ["A. Juan José Arévalo", "B. Bernardo Arévalo ", "C. Alejandro Giammattei", "D. Alejandro Maldonado"],
   "answer": "B"
},
{
   "prompt": "When did Guatemala declare its independence from the Spanish Empire?",
   "options": ["A. 1 July 1823", "B. 17 April 1839", "C. 31 May 1985", "D. 15 September 1821"],
   "answer": "D"
},
{
   "prompt": "How many states does Guatemala have?",
   "options": ["A. 22", "B. 23", "C. 24", "D. 25"],
   "answer": "A"
},
]

def run_game(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option) 

run_game(questions)
      