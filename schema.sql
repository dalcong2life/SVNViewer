-- 코드 테이블
CREATE TABLE IF NOT EXISTS CODE (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  type        TEXT NOT NULL,
  name        TEXT NOT NULL,
  create_date DATETIME,
  modify_date DATETIME
);

-- 사용자 테이블
CREATE TABLE IF NOT EXISTS USER (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  email       TEXT NOT NULL UNIQUE,
  username    TEXT NOT NULL,
  pw_hash     TEXT NOT NULL,
  bugzilla_id TEXT,
  bugzilla_pw TEXT,
  create_date DATETIME,
  modify_date DATETIME
);

-- SVN 설정 정보 테이블
CREATE TABLE IF NOT EXISTS SVN_INFO (
  s_path_id        INTEGER PRIMARY KEY AUTOINCREMENT,
  s_path_url       TEXT NOT NULL,
  s_start_revision INTEGER,
  s_last_revision  INTEGER,
  active           INTEGER,
  product_id       TEXT NOT NULL,
  desc             TEXT,
  created_userid   TEXT,
  create_date      DATETIME,
  modify_date      DATETIME
);

CREATE TABLE IF NOT EXISTS SVN_HISTORY (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  s_path_id  INTEGER,
  s_revision INTEGER,
  s_id       TEXT NOT NULL,
  s_time     TEXT NOT NULL,
  s_comment  TEXT NOT NULL,
  FOREIGN KEY (s_path_id) REFERENCES SVN_INFO (s_path_id)
);

CREATE TABLE IF NOT EXISTS SVN_HISTORY_FILE (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  svn_id      INTEGER,
  file_action TEXT,
  file_path   TEXT,
  file_diff   TEXT,
  FOREIGN KEY (svn_id) REFERENCES SVN_HISTORY (id)
);
