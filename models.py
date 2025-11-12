from datetime import datetime, timezone

from lnbits.db import FilterModel
from pydantic import BaseModel, Field


########################### Wallets ############################
class CreateWallets(BaseModel):
    wallet: str
    pull_payments: bool
    push_payments: bool
    reconcile_name: str | None
    reconcile_mode: str | None = "sat"
    xero_bank_account_id: str | None
    tax_rate: str | None = "sat"
    fee_handling: bool | None
    last_synced: datetime | None
    status: str | None
    notes: str | None


class Wallets(BaseModel):
    id: str
    user_id: str
    wallet: str
    pull_payments: bool
    push_payments: bool
    reconcile_name: str | None
    reconcile_mode: str | None = "sat"
    xero_bank_account_id: str | None
    tax_rate: str | None = "sat"
    fee_handling: bool | None
    last_synced: datetime | None
    status: str | None
    notes: str | None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class WalletsFilters(FilterModel):
    __search_fields__ = [
        "wallet",
        "pull_payments",
        "push_payments",
        "reconcile_name",
        "reconcile_mode",
        "xero_bank_account_id",
        "tax_rate",
        "fee_handling",
        "last_synced",
        "status",
        "notes",
    ]

    __sort_fields__ = [
        "wallet",
        "pull_payments",
        "push_payments",
        "reconcile_name",
        "reconcile_mode",
        "xero_bank_account_id",
        "tax_rate",
        "fee_handling",
        "last_synced",
        "status",
        "notes",
        "created_at",
        "updated_at",
    ]

    created_at: datetime | None
    updated_at: datetime | None


############################ Settings #############################
class ExtensionSettings(BaseModel):
    zero_client_id: str | None
    zero_client_secret: str | None

    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @classmethod
    def is_admin_only(cls) -> bool:
        return bool("False" == "True")


class UserExtensionSettings(ExtensionSettings):
    id: str
