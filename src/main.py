from fastapi import FastAPI
import redis
import pandas as pd
# import asyncio

# import aioredis

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    global redis
    redis = redis.Redis(
        host="mle-redis-cache.redis.cache.windows.net",
        port="6379",
        password="53m41YdvLc37o3YMxnAGp0t03g38tUvX4AzCaGL3PbI=",
    )

@app.post("/get_cache")
async def root():
    start_time = pd.Timestamp.now()
    value_ = redis.hget("tsc_test", "1")
    print(f"Time taken for preprocessing: {pd.Timestamp.now() - start_time}")
    return {"message": str(value_)}
