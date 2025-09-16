import pika

# 1. 접속
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 2. 'hello' 큐있는지 확인
#    (혹시 받는 쪽이 실행 안 됐을까 봐, 보내는 쪽도 확인하는 게 안전)
channel.queue_declare(queue='hello')

# 3. **중요**
# 'hello'라는 routing_key로 'Hello World!'라는 body 전송!
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# 4. 연결 종료
connection.close()

# ### 
# python send.py 6번보내기
# c1 c2에 각각 3개씩 1,3,5/2,4,6으로 알아서 로드밸런싱됨