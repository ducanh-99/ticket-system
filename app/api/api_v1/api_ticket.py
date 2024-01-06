import logging
from typing import Any

import aioredis
import redis
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_redis

logger = logging.getLogger(__name__)
router = APIRouter()
router_lead = APIRouter()


class TicketPaymentPayload(BaseModel):
    user_id: int
    ticket_id: int


class AutoIncrement:
    def __init__(self, r: aioredis.Redis = Depends(get_redis)):
        self.r = r

    async def getTrx(self):
        await self.r.incr("test")
        res = await self.r.get("test")
        return res


@router.post("", response_model=Any)
async def order_ticket(autoIncrement: AutoIncrement = Depends()):
    test = await autoIncrement.getTrx()
    print(test)

    return


@router.post("/payment")
async def payment_ticket(user_id: int):
    pass


@router.get("")
def get_ticket(r: redis.Redis = Depends(get_redis)):
    r.get("test")
    return
