from limitlessled.bridge import Bridge
from limitlessled.pipeline import Pipeline

from limitlessled.group.rgb import RGB
from limitlessled.group.rgbw import RGBW
from limitlessled.group.rgbww import RGBWW
from limitlessled.group.white import WHITE

import limitlessled
import time
import logging

terminate = False

def my_function():
    global terminate
    terminate = True
    pass

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger()

logger.info("Setup group")
bridge = Bridge('192.168.178.232')
gartenhaus = bridge.add_group(1, 'gartenhaus', RGB)

pipeline = Pipeline().on().wait(4).off()
pipeline.callback(my_function)

gartenhaus.enqueue(pipeline)
logger.info("Switch on group %s" , gartenhaus)

while terminate == False:
    time.sleep(1)

