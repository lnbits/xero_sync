from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from lnbits.core.models import User
from lnbits.decorators import check_user_exists
from lnbits.helpers import template_renderer

xero_sync_generic_router = APIRouter()


def xero_sync_renderer():
    return template_renderer(["xero_sync/templates"])


@xero_sync_generic_router.get("/", response_class=HTMLResponse)
async def index(req: Request, user: User = Depends(check_user_exists)):
    return xero_sync_renderer().TemplateResponse("xero_sync/index.html", {"request": req, "user": user.json()})
