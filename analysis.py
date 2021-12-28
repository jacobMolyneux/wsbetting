test_cases = ['FGR','a','TEST', 'ME', 'Me', '', 'we', 'socwhat', 'F', 's', '7', '9']

def checker(word):
    if len(word) < 2:
        return False
    else:
        return word.isupper()




mentioned = []
def parse_comment(comment, stock_list):
    for i in comment.split():
        if checker(i) == True:
            stock_list.append(i)
        else:
            pass
    print(stock_list)

parse_comment(test_string, mentioned)