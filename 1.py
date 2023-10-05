from Run import Run
from Call import *

o = Run("Code", 75, HTTPCall('http://localhost:8080'))
o.run()