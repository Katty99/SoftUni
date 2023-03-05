messages_sent = int(input())
for current_message in range(messages_sent):
    message = int(input())
    if message == 88:
        print('Hello')
    elif message == 86:
        print('How are you?')
    elif message > 88:
        print('Bye.')
    else:
        print('GREAT!')