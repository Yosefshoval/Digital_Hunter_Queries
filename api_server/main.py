from fastapi import FastAPI
from routes import router
app = FastAPI()

app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app="main:app",
        port=8085,
        host="0.0.0.0",
        reload=True
    )