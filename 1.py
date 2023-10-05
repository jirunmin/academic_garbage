from Run import Run
from Call import *

# TCP: '127.0.0.1' 9998
# UDP: '127.0.0.1' 9997
# HTTP: http://localhost:8080
# WebService: http://localhost:8080/similarity

o = Run("Code", 75, WebServiceCall("http://localhost:8080/similarity"))
o.run()

o.setType(TCPCall('127.0.0.1', 9998))
o.run()