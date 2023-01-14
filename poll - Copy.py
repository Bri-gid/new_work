favourite_language={
    'brigid':'python',
    'erica':'c++',
    'jamie':'ruby',
    'phyte':'java',
    }
polls=['pius','aubrey','brigid','jamie']
for poll in polls:
    if poll not in favourite_language.keys():
        print('Please,'+" "+poll.title()+" "+"take the poll.")
    else:
        print( poll.title()+","+"thank you for taking the poll.")

