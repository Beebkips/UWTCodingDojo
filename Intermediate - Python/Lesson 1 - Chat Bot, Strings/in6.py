import requests, json

while(1):
    var = raw_input('Type a command: ')
    if var.startswith('!'):
        if var.startswith('!say'):
            var = var.split('!say')[1].strip()
            print var    
        elif var.startswith('!catfact'):
            call = requests.get('http://catfacts-api.appspot.com/api/facts?number=1')
            fact = json.loads(call.text)
            print fact['facts'][0]