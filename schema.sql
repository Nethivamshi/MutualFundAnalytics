CREATE TABLE 01_fund_master (
    amfi_code INTEGER,
    fund_house TEXT,
    scheme_name TEXT
);

CREATE TABLE 02_nav_history (
    amfi_code INTEGER,
    date TEXT,
    nav REAL
);