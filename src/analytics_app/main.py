from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="A5 Analytics Service",
    version="0.1.0"
)

# =====================
# MODELS
# =====================

class DashboardResponse(BaseModel):
    total_visitors: int
    total_alerts: int
    active_cameras: int


class CameraAnalyticsResponse(BaseModel):
    camera_events: int
    motion_detected: int


class AccessAnalyticsResponse(BaseModel):
    entries: int
    exits: int


class CameraEvent(BaseModel):
    camera_id: str
    event_type: str
    timestamp: str


# =====================
# API
# =====================

@app.get("/")
def root():
    return {
        "service": "Analytics",
        "group": "A5"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.get(
    "/dashboard",
    response_model=DashboardResponse
)
def dashboard():
    return DashboardResponse(
        total_visitors=1250,
        total_alerts=12,
        active_cameras=18
    )


@app.get(
    "/analytics/cameras",
    response_model=CameraAnalyticsResponse
)
def camera_analytics():
    return CameraAnalyticsResponse(
        camera_events=340,
        motion_detected=95
    )


@app.get(
    "/analytics/access",
    response_model=AccessAnalyticsResponse
)
def access_analytics():
    return AccessAnalyticsResponse(
        entries=520,
        exits=498
    )


@app.post("/analytics/camera-events")
def receive_camera_event(event: CameraEvent):
    return {
        "message": "Camera event received",
        "data": event
    }