while(1):
    var = raw_input('Type a command: ')
    if var.startswith('!'):
        print 'That was a command'
    else:
        print 'Not a command'