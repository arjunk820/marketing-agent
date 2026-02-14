# In-memory campaign store
# Maps campaign_id -> { thread_id, status, state }
# In production, swap this for a database

campaign_store: dict[str, dict] = {}
