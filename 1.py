from Run import Run
from Call import *

o = Run("Code", 50, TCPCall("127.0.0.1", 9998))
o.run()