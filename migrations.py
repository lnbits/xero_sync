# the migration file is where you build your database tables
# If you create a new release for your extension ,
# remember the migration file is like a blockchain, never edit only add!

empty_dict: dict[str, str] = {}


async def m001_extension_settings(db):
    """
    Initial settings table.
    """

    await db.execute(
        f"""
        CREATE TABLE xero_sync.extension_settings (
            id TEXT NOT NULL,
            zero_client_id TEXT,
            zero_client_secret TEXT,
            updated_at TIMESTAMP NOT NULL DEFAULT {db.timestamp_now}
        );
    """
    )


async def m002_wallets(db):
    """
    Initial wallets table.
    """

    await db.execute(
        f"""
        CREATE TABLE xero_sync.wallets (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            wallet TEXT NOT NULL,
            pull_payments BOOLEAN NOT NULL,
            push_payments BOOLEAN NOT NULL,
            reconcile_name TEXT,
            reconcile_mode TEXT,
            xero_bank_account_id TEXT,
            tax_rate TEXT,
            fee_handling BOOLEAN,
            last_synced TIMESTAMP,
            status TEXT,
            notes TEXT,
            created_at TIMESTAMP NOT NULL DEFAULT {db.timestamp_now},
            updated_at TIMESTAMP NOT NULL DEFAULT {db.timestamp_now}
        );
    """
    )
