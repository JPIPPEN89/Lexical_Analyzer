
code = []
comment = False

symbols = ['(', ')', '[', ']', '{', '}', ',', ';', '=', '.']

keywords = ['class','function','if','else','return',
            'constructor','int','method', 'boolean', 'char', 'void',
            'var', 'static','field','let','do','while','true','false','null','this']

operators = ['+','-','*','/','&','|', '~','<','>']
found = False

def check_keyword(identifier):
    is_found = False
    for check in keywords:
        if identifier.lower() == check:

            print( f'<keyword>{identifier}</keyword>')
            is_found = True
            break
    if identifier != "" and not is_found:
        print( f'<identifier>{identifier}</identifier>')



bool_stgLit = False
stgLit = ''
is_symbol = False

ident = ''

with open('Main.jack.txt') as file:

    for line in file:
        if line[0:2] == '//':
            continue
        elif line[0:3] == '/**':
            comment = True
        elif not comment:
            for i in range(len(line)):
                if line[i] == '*' and line[i+1] == '/':
                    comment = False

        else:
            code.append(line)


for c in code:
    #print(c)
    sent = c
    #sent = sent.split()
    for word in sent:
        if found:
            found = False


        if word == '"' and not stgLit:
            bool_stgLit = True
            found = True
            continue
        if bool_stgLit and word != '"' and not found:
            stgLit += word
            continue
        elif bool_stgLit and word == '"' and not found:
            print(f'<literal>{stgLit}</literal>')
            stgLit =''
            bool_stgLit = False
            found = True
            continue


        if not word.isalpha() and not found:
            for check in symbols:
                #checking for symbols
                if check == word and not found:
                    found = True
                    if ident:
                        check_keyword(ident)
                        ident = ''

                    print(f'<symbol>{word}</symbol>')



                    #checking for operators
            for check in operators:
                if check == word and not found:
                    found = True
                    if ident:
                        check_keyword(ident)
                        ident = ''

                    print(f'<operator>{word}</operator>')



        if not word.isspace() and not found:
            ident += word
        elif word.isspace() and not found:
            check_keyword(ident)
            ident = ''







