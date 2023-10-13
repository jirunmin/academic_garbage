from Run import Run
from Call import *

# TCP: '127.0.0.1' 9998
# UDP: '127.0.0.1' 9997
# HTTP: http://localhost:8080
# WebService: http://localhost:8079/similarity

o = Run("Code", 0, LocalCall())
o.run()

# o.setType(TCPCall('127.0.0.1', 9998))
# o.run()