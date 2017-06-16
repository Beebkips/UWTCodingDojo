while(1):
    var = raw_input('Type a command: ')
    if var.startswith('!'):
        if var.startswith('!say'):
            var = var.split('!say')[1].strip()
            print var