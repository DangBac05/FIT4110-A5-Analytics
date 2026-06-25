# FIT4110 A5 Analytics Service

## Smart Campus Operations Platform

Analytics Service của nhóm A5.

### Chức năng

* Tổng hợp dữ liệu từ Camera Service
* Thống kê dữ liệu truy cập
* Dashboard tổng quan hệ thống
* Phân tích dữ liệu Smart Campus

### API Endpoints

#### Health Check

GET /health

#### Dashboard

GET /dashboard

#### Camera Analytics

GET /analytics/cameras

#### Access Analytics

GET /analytics/access

#### Receive Camera Event

POST /analytics/camera-events

### Công nghệ sử dụng

* FastAPI
* Python 3.14
* OpenAPI 3.1
* GitHub

### Thành viên nhóm

* DANG VAN BAC, NGUYEN DUY HUNG, VU SON HAI

### Chạy project

```bash
uvicorn analytics_app.main:app --app-dir src --reload
```

Swagger:

```text
http://localhost:8000/docs
```
