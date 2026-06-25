from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="A5 Analytics Service",
    version="0.2.0"
)

# =====================
# IN-MEMORY STORAGE
# =====================

camera_events = []
access_events = []
iot_readings = []

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


class AccessEvent(BaseModel):
    gate_id: str
    action: str
    timestamp: str


class IoTReading(BaseModel):
    device_id: str
    metric: str
    value: float
    unit: str
    timestamp: str


# =====================
# ROOT
# =====================

@app.get("/")
def root():
    return {
        "service": "Analytics",
        "group": "A5",
        "version": "0.2.0"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


# =====================
# DASHBOARD
# =====================

@app.get(
    "/dashboard",
    response_model=DashboardResponse
)
def dashboard():

    return DashboardResponse(
        total_visitors=len(access_events),
        total_alerts=len(camera_events),
        active_cameras=len(
            set(
                [
                    event["camera_id"]
                    for event in camera_events
                ]
            )
        )
    )


# =====================
# CAMERA ANALYTICS
# =====================

@app.get(
    "/analytics/cameras",
    response_model=CameraAnalyticsResponse
)
def camera_analytics():

    motion_count = len(
        [
            e for e in camera_events
            if e["event_type"] == "motion_detected"
        ]
    )

    return CameraAnalyticsResponse(
        camera_events=len(camera_events),
        motion_detected=motion_count
    )


# =====================
# ACCESS ANALYTICS
# =====================

@app.get(
    "/analytics/access",
    response_model=AccessAnalyticsResponse
)
def access_analytics():

    entries = len(
        [
            e for e in access_events
            if e["action"] == "entry"
        ]
    )

    exits = len(
        [
            e for e in access_events
            if e["action"] == "exit"
        ]
    )

    return AccessAnalyticsResponse(
        entries=entries,
        exits=exits
    )


# =====================
# RECEIVE CAMERA EVENT
# =====================

@app.post("/analytics/camera-events")
def receive_camera_event(event: CameraEvent):

    camera_events.append(event.model_dump())

    return {
        "message": "Camera event received",
        "total_events": len(camera_events),
        "data": event
    }


# =====================
# RECEIVE ACCESS EVENT
# =====================

@app.post("/analytics/access-events")
def receive_access_event(event: AccessEvent):

    access_events.append(event.model_dump())

    return {
        "message": "Access event received",
        "total_events": len(access_events),
        "data": event
    }


# =====================
# RECEIVE IOT READING
# =====================

@app.post("/analytics/iot-readings")
def receive_iot_reading(reading: IoTReading):

    iot_readings.append(reading.model_dump())

    return {
        "message": "IoT reading received",
        "total_readings": len(iot_readings),
        "data": reading
    }


# =====================
# VIEW RAW DATA
# =====================

@app.get("/analytics/raw")
def raw_data():

    return {
        "camera_events": camera_events,
        "access_events": access_events,
        "iot_readings": iot_readings
    }