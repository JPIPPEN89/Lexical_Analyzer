
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

            append_text( f'<keyword> {identifier} </keyword>\n')
            is_found = True
            break
    if identifier != "" and not is_found:
        append_text( f'<identifier> {identifier} </identifier>\n')

def append_text(txt):
    with open("analyzer_output.txt", "a") as f:
        f.write(txt)

def compare_files():
    j=0
    my_output = []
    txt_out = []
    with open('analyzer_output.txt') as file:
        for lines in file:
            my_output.append(lines)
    with open('main_xml.txt') as f:
        for line in f:
            txt_out.append(line)

    for i in range(len(my_output)):
        j+=1
        if my_output[i] != txt_out[i]:
            print(f'Error on line {j}')


bool_stgLit = False
stgLit = ''
is_symbol = False

ident = ''
with open("analyzer_output.txt", "a") as f:
    f.write('<tokens>\n')

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
            append_text(f'<literal> {stgLit} </literal>\n')
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

                    append_text(f'<symbol> {word} </symbol>\n')



                    #checking for operators
            for check in operators:
                if check == word and not found:
                    found = True
                    if ident:
                        check_keyword(ident)
                        ident = ''

                    append_text(f'<operator> {word} </operator>\n')



        if not word.isspace() and not found:
            ident += word
        elif word.isspace() and not found:
            check_keyword(ident)
            ident = ''


with open("analyzer_output.txt", "a") as f:
    f.write('</tokens>\n')


compare_files()

