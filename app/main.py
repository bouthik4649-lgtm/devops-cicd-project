from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI(
    title="DevOps Monitoring API",
    description="Python application deployed using AWS EKS and Jenkins CI/CD",
    version="1.0.0"
)

REQUEST_COUNT = Counter(
    "application_requests_total",
    "Total number of application requests"
)


@app.get("/")
def home():
    REQUEST_COUNT.inc()
    return {
        "message": "Welcome to DevOps Monitoring API",
        "status": "Application is running"
    }


@app.get("/health")
def health():
    REQUEST_COUNT.inc()
    return {"status": "healthy"}


@app.get("/info")
def application_info():
    REQUEST_COUNT.inc()
    return {
        "application": "DevOps Monitoring API",
        "version": "1.0.0",
        "technology": "Python FastAPI"
    }


@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )