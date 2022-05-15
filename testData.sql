INSERT INTO reading_obj (value,timestamp)
VALUES(2.5, strftime('%s','now'));

INSERT INTO reading_obj (value,timestamp)
VALUES(2.5, strftime('%s','now'));

INSERT INTO reading_obj (value,timestamp)
VALUES(3.8, strftime('%s','now'));

INSERT INTO reading_obj (value,timestamp)
VALUES(2.98, strftime('%s','now'));

INSERT INTO reading_obj (value,timestamp)
VALUES(99.54, strftime('%s','now'));

INSERT INTO reading_obj (value,timestamp)
VALUES(13.4, strftime('%s','now'));

INSERT INTO reading_obj (value,timestamp)
VALUES(22.1024, strftime('%s','now'));

--select data

SELECT value, datetime(timestamp,'unixepoch')
FROM reading_obj;