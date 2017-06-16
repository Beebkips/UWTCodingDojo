while(1):
    var = raw_input('Type a command: ')
    if var.startswith('!'):
        var = var.split('!')[1].strip()
        print 'Your command was: ' + var