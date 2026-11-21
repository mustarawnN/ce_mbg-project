-- DaphniaVision veritabanı şeması
-- Sorumlu: Ali

CREATE TABLE IF NOT EXISTS series (
    id          TEXT PRIMARY KEY,           -- ör. "kafein-2026-12-01"
    name        TEXT NOT NULL,
    substance   TEXT,
    created_at  TEXT DEFAULT CURRENT_TIMESTAMP,
    notes       TEXT
);

CREATE TABLE IF NOT EXISTS videos (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    series_id        TEXT REFERENCES series(id),
    file_path        TEXT NOT NULL,
    substance        TEXT NOT NULL,
    dose             REAL NOT NULL,
    dose_unit        TEXT DEFAULT 'mg/L',
    is_control       INTEGER DEFAULT 0,
    temperature_c    REAL,
    age_hours        REAL,
    body_length_mm   REAL,
    immobilization   TEXT,
    acclimation_min  REAL,
    exposure_min     REAL,
    magnification    TEXT,
    fps              REAL,
    duration_s       REAL,
    notes            TEXT,
    uploaded_at      TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS results (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id      INTEGER NOT NULL REFERENCES videos(id) ON DELETE CASCADE,
    method        TEXT,
    roi_auto      INTEGER,
    bpm           REAL,
    beat_count    INTEGER,
    ibi_mean_s    REAL,
    ibi_sd_s      REAL,
    ibi_cv        REAL,
    rmssd_s       REAL,
    pauses        INTEGER,
    reliability   REAL,
    warnings      TEXT,                     -- JSON listesi
    arrays_path   TEXT,                     -- sinyal/spektrum/atım zamanları .npz dosyası
    created_at    TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Elle sayım (doğrulama için)
CREATE TABLE IF NOT EXISTS manual_counts (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id     INTEGER NOT NULL REFERENCES videos(id) ON DELETE CASCADE,
    counter      TEXT,                      -- sayan kişi
    beat_count   INTEGER,
    duration_s   REAL,
    bpm          REAL
);
