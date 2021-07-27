""" Syntax :
compile(source, filename, mode, flag, dont_inherit, optimize) """

# Compile text as code, and the execute it:

x = compile('print(55)', 'test', 'eval')
exec(x)

# Compile more than one statement, and the execute it:

x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)