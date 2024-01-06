from fastapi import APIRouter

from app.api.api_v1 import (api_healthcheck, api_user, api_ticket)

router_v1 = APIRouter()

router_v1.include_router(api_healthcheck.router, tags=["healthcheck"], prefix="/healthcheck")
router_v1.include_router(api_user.router, tags=["User"], prefix="/users")
router_v1.include_router(api_ticket.router, tags=["Ticket"], prefix="/tickets")
