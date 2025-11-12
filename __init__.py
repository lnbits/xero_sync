import asyncio

from fastapi import APIRouter
from lnbits.tasks import create_permanent_unique_task
from loguru import logger

from .crud import db
from .tasks import wait_for_paid_invoices
from .views import xero_sync_generic_router
from .views_api import xero_sync_api_router

xero_sync_ext: APIRouter = APIRouter(prefix="/xero_sync", tags=["XeroSync"])
xero_sync_ext.include_router(xero_sync_generic_router)
xero_sync_ext.include_router(xero_sync_api_router)


xero_sync_static_files = [
    {
        "path": "/xero_sync/static",
        "name": "xero_sync_static",
    }
]

scheduled_tasks: list[asyncio.Task] = []


def xero_sync_stop():
    for task in scheduled_tasks:
        try:
            task.cancel()
        except Exception as ex:
            logger.warning(ex)


def xero_sync_start():
    task = create_permanent_unique_task("ext_xero_sync", wait_for_paid_invoices)
    scheduled_tasks.append(task)


__all__ = [
    "db",
    "xero_sync_ext",
    "xero_sync_start",
    "xero_sync_static_files",
    "xero_sync_stop",
]
