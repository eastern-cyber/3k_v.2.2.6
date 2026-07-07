import redis
import os

try:
    r = redis.from_url(os.environ.get('REDIS_URL'))
    print("Redis connection successful!")
    print(f"Ping response: {r.ping()}")
except Exception as e:
    print(f"Redis connection failed: {e}")
