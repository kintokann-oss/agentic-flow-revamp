CREATE TABLE IF NOT EXISTS app_state (
    key TEXT PRIMARY KEY,
    value INTEGER NOT NULL CHECK (value IN (0, 1))
);

INSERT OR IGNORE INTO app_state (key, value) VALUES ('toggle', 0);
