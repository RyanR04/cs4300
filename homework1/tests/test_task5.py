from src.task5 import Book_List, First_Three_Books, Students

#Print out first 3 books
def test_first_three_books():

    #Store the first 3 books
    result = First_Three_Books(Book_List)

    #Check is result is 3 string
    assert len(result) == 3
    #Check the contents
    assert result == Book_List[:3]

#Check to see if we can use the dictionary to find id values
def test_student_id():
    assert Students["Virgil"] == "1004"
