import pika

# 1. 접속
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 2. 'hello'라는 이름의 Queue가 있는지 확인하고, 없으면 만들기
channel.queue_declare(queue='hello')

# 3. 메시지가 오면 뭘 할지 정하기
def callback(ch, method, properties, body):
    # -> 그냥 화면에 received {body}라고 출력
    print(f" [x] Received {body}") 

# 4. 'hello' 큐에서 정한 "할 일(callback)"을 연결
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True) # auto_ack=True는 "받으면 자동으로 잘 받았다고 서명할게"라는 뜻

# 5. 이제 'hello' 큐에서 메시지 올 때까지 '무한 대기' 시작!
print(' [*] Waiting for messages...')
channel.start_consuming()