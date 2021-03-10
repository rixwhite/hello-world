import subprocess
from time import sleep

try:
  while True:
    sleep(1)
    subprocess.run(["xset", "-display", ":0.0", "dpms", "force", "off"])
except KeyboardInterrupt:
  pass
