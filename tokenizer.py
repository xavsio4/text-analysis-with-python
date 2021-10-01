from nltk.tokenize import sent_tokenize, \
    word_tokenize, WordPunctTokenizer
from nltk.corpus import stopwords
import mysql.connector as connector
import csv


# establishing the connection
conn = connector.connect(
    user='test', password='test', host='localhost', port=8809, database='python')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# test connection
# Executing an MYSQL function using the execute() method
cursor.execute("SELECT DATABASE()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ", data)

# Preparing SQL query to INSERT a record into the database.
sql = """ insert into wordtoken (word,item,question, type) values ( %s, %s, %s, %s ) """
question = 4
type = 'P'
file = 'expPQ4.csv'

# show default stopwords
print(stopwords.words('english'))

# this is an array with stop words or punctuation not in the initial list
add_stop_words = ["It", "Do", "?", "!", "'s", ".", " ''", "..", ":", "-", "*", "``", "''", "\\r\\n", "n't",
                  ",", "Let", "[", "]", "'", "(", ")", "...", "don\x92t", "The", "Us",
                  "I", "A", "%", "\"", ";", "if", "by", "'By", "would"]
add_stop_words_fr = ["n\'est", "si", "la",
                     "etc", "c'est", "très", "si", "Je", "je", "par", "Par", "'Par", "'by", "'PAR", "très", "'par", "'Je", "n'ai"]
# initial stopwords list by default
stop_words = stopwords.words(
    'english') + stopwords.words('french') + stopwords.words('german')
# merge initial list and custom list
stop_words = stop_words + add_stop_words + add_stop_words_fr

# open file for reading
with open(file, 'r', newline='', encoding='latin-1') as csvDataFile:
    # read file as csv file
    csvReader = csv.reader(csvDataFile)
    item = 0
    # for every row, print the row
    for row in csvReader:

        if str(row) != '' and str(row) != '[]':

            # Define input text
            input_text = str(row)
            print(input_text)
            # Sentence tokenizer
            print("\nSentence tokenizer out:")
            print(sent_tokenize(input_text))

            # Word tokenizer
            print("\nWord tokenizer:")
            result = word_tokenize(input_text)
            print(result)

            filtered_result = []
            print('\nsql insert:')
            for w in result:
                if w not in stop_words:
                    filtered_result.append(w)
                    print(w)
                    # and now let's insert into the database
                    try:
                        cursor.execute(sql, (w, item, question, type))
                    except connector.Error as error:
                        print("This is sql #6", format(error))

            conn.commit()

            print("\nFiltered tokenizer:")
            print(filtered_result)

            # WordPunct tokenizer
            print("\nWord punct tokenizer:")
            print(WordPunctTokenizer().tokenize(input_text))
            item = item + 1

# Closing the connection
conn.close()
