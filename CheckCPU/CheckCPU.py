import psutil
import os
from influxdb import InfluxDBClient
import time,math,random

#get current pid
p1 = psutil.Process(os.getpid())

while True:
    a = psutil.virtual_memory().percent

    b = psutil.cpu_percent(interval=1.0)

    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "fields": {
                "cpu": b,
                "mem": a
            }
        }
    ]

    client = InfluxDBClient('localhost', 8086, 'root', 'root', "xxyyxx")
    client.create_database('xxyyxx')
    client.write_points(json_body)

    result = client.query('select value from cpu_load_short;')
    print("Result: {0}".format(result))
    time.sleep(2)

