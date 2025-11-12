from lnbits.db import Database, Filters, Page
from lnbits.helpers import urlsafe_short_hash

from .models import (
    CreateWallets,
    ExtensionSettings,  #
    UserExtensionSettings,  #
    Wallets,
    WalletsFilters,
)

db = Database("ext_xero_sync")


########################### Wallets ############################
async def create_wallets(user_id: str, data: CreateWallets) -> Wallets:
    wallets = Wallets(**data.dict(), id=urlsafe_short_hash(), user_id=user_id)
    await db.insert("xero_sync.wallets", wallets)
    return wallets


async def get_wallets(
    user_id: str,
    wallets_id: str,
) -> Wallets | None:
    return await db.fetchone(
        """
            SELECT * FROM xero_sync.wallets
            WHERE id = :id AND user_id = :user_id
        """,
        {"id": wallets_id, "user_id": user_id},
        Wallets,
    )


async def get_wallets_by_id(
    wallets_id: str,
) -> Wallets | None:
    return await db.fetchone(
        """
            SELECT * FROM xero_sync.wallets
            WHERE id = :id
        """,
        {"id": wallets_id},
        Wallets,
    )


async def get_wallets_ids_by_user(
    user_id: str,
) -> list[str]:
    rows: list[dict] = await db.fetchall(
        """
            SELECT DISTINCT id FROM xero_sync.wallets
            WHERE user_id = :user_id
        """,
        {"user_id": user_id},
    )

    return [row["id"] for row in rows]


async def get_wallets_paginated(
    user_id: str | None = None,
    filters: Filters[WalletsFilters] | None = None,
) -> Page[Wallets]:
    where = []
    values = {}
    if user_id:
        where.append("user_id = :user_id")
        values["user_id"] = user_id

    return await db.fetch_page(
        "SELECT * FROM xero_sync.wallets",
        where=where,
        values=values,
        filters=filters,
        model=Wallets,
    )


async def update_wallets(data: Wallets) -> Wallets:
    await db.update("xero_sync.wallets", data)
    return data


async def delete_wallets(user_id: str, wallets_id: str) -> None:
    await db.execute(
        """
            DELETE FROM xero_sync.wallets
            WHERE id = :id AND user_id = :user_id
        """,
        {"id": wallets_id, "user_id": user_id},
    )


############################ Settings #############################
async def create_extension_settings(user_id: str, data: ExtensionSettings) -> ExtensionSettings:
    settings = UserExtensionSettings(**data.dict(), id=user_id)
    await db.insert("xero_sync.extension_settings", settings)
    return settings


async def get_extension_settings(
    user_id: str,
) -> ExtensionSettings | None:
    return await db.fetchone(
        """
            SELECT * FROM xero_sync.extension_settings
            WHERE id = :user_id
        """,
        {"user_id": user_id},
        ExtensionSettings,
    )


async def update_extension_settings(user_id: str, data: ExtensionSettings) -> ExtensionSettings:
    settings = UserExtensionSettings(**data.dict(), id=user_id)
    await db.update("xero_sync.extension_settings", settings)
    return settings
