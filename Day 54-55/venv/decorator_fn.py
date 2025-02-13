def hi(name ='mark'):
    print('you are now in the hi function')

    def greet():
        return "hello my great devs"
    
    def welcome():
        return 'you are now in the welcome function'
    
    print(greet())
    print(welcome())

hi()

def bold_text(text):
    def bold():
        return '<b>' + text() + '</b>'
    return bold
    
    
def emphasize_text(text):
    def emp():
        return '<em>' +text()+'</em>'
    return emp

def underline(text):
    def underline_text():
        return '<u>' + text() + '</u>'
    return underline_text