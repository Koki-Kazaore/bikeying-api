from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import List, Union

app = FastAPI()

# スキーマ定義
class Error(BaseModel):
    detail: Union[str, List[str]]

class ReserveBikeSchema(BaseModel):
    userId: str = Field(..., example="123456", description="User ID making the reservation")
    bikeId: str = Field(..., example="bike_123456", description="Bike ID to reserve")

    class Config:
        extra = 'forbid'

class RequestBikeSchema(BaseModel):
    userId: str = Field(..., example="123456", description="User ID making the reservation")
    location: List[float] = Field(
        ...,
        description="Array of latitude and longitude",
        example=[35.681236, 139.767125],
        min_items=2,
        max_items=2
    )

    class Config:
        extra = 'forbid'

class GetBikeSchema(BaseModel):
    bikeId: str = Field(..., example="bike_123456")
    status: str = Field(..., example="available")
    location: List[float] = Field(
        ...,
        example=[35.681236, 139.767125],
        min_items=2,
        max_items=2
    )

    class Config:
        extra = 'forbid'

# エンドポイントの実装
@app.get("/bikes", response_model=List[GetBikeSchema])
def get_bike():
    # ダミーデータを返す
    return [
        GetBikeSchema(
            bikeId="bike_123456",
            status="available",
            location=[35.681236, 139.767125]
        )
    ]

@app.post("/bikes/request", status_code=202)
def stock_request(request: RequestBikeSchema = Body(...)):
    # リクエストを受け付け、ダミーのレスポンスを返す
    return {
        "requestId": "req_123456",
        "message": "Request successfully accepted and stocked"
    }

@app.post("/bikes/reserve", response_model=GetBikeSchema)
def reserve_bike(reservation: ReserveBikeSchema = Body(...)):
    # 自転車を予約し、ダミーのデータを返す
    return GetBikeSchema(
        bikeId=reservation.bikeId,
        status="reserved",
        location=[35.681236, 139.767125]
    )

# エラーハンドリング
@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
