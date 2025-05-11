from datetime import datetime
import time

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"/data/log.txt", "a") as f:
        f.write(f"[{now}] App Corriendo\n")
    print(f"[{now}] escribiendo en /data/log.txt...")
    time.sleep(5)