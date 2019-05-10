from iotjokepi import JokePi

ApiKey = 'Your API Key'
Link = 'http://iot-joke-pi.herokuapp.com'

# Instance to get swtich states
getOb = JokePi('Button', ApiKey, Link + '/api/getdata/')


data1 = getOb.getSwitchState('Switch Name')
data = data1

if data == 'ON':
    print('Fan is ON')
elif data == 'OFF':
    print('Fan is OFF')
else:
    print('Invalid Device')