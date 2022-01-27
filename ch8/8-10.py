# 8-10. Sending Messages
def send_messages(msgs, sent_messages):
    while msgs:
        current_msg = msgs.pop()
        print(current_msg)
        sent_messages.append(current_msg)

def print_all(msgs):
    for msg in msgs:
        print(msg)

msgs = ['I', 'love', 'Python']
sent_messages = []
send_messages(msgs, sent_messages)
print_all(msgs)
print_all(sent_messages)