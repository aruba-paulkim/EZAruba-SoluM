CREATE TABLE admin (
 seq integer PRIMARY KEY AUTOINCREMENT,
 admin_id text NOT NULL DEFAULT ',
 admin_pw text NOT NULL DEFAULT '
);
INSERT INTO admin ('seq', 'admin_id', 'admin_pw') VALUES (1,'admin','goaruba!');

CREATE TABLE allowed_device (
 seq integer PRIMARY KEY AUTOINCREMENT,
 device_id text NOT NULL DEFAULT ',
 user_name text NOT NULL DEFAULT ',
 enable_YN text NOT NULL DEFAULT '
);
INSERT INTO allowed_device ('seq','device_id','user_name','enable_YN') VALUES (1,'C912B707-ED3D-490C-A154-B0C2A5E46189','김민혁','Y');
INSERT INTO allowed_device ('seq','device_id','user_name','enable_YN') VALUES (2,'769C0EF4-06D0-4FF4-BFAE-A5E104B88F1C','조용운','Y');
INSERT INTO allowed_device ('seq','device_id','user_name','enable_YN') VALUES (3,'1460EBD8-1670-44C6-B639-4B09F97CC7E2','한창훈','Y');
INSERT INTO allowed_device ('seq','device_id','user_name','enable_YN') VALUES (4,'569FC749-1265-4E14-9632-B290A65AD76E','이한민','Y');
INSERT INTO allowed_device ('seq','device_id','user_name','enable_YN') VALUES (5,'A39D4F62-5BCE-4885-BF09-69DAD18B4EB3??','홍진표','Y');
INSERT INTO allowed_device ('seq','device_id','user_name','enable_YN') VALUES (6,'034C4B3C-A41E-4606-9F92-4B898DF41F65','이동현','Y');
INSERT INTO allowed_device ('seq','device_id','user_name','enable_YN') VALUES (7,'D9B9F9A4-1CF5-4871-8945-B749E50D95D7','갤럭시텝A','Y');
INSERT INTO allowed_device ('seq','device_id','user_name','enable_YN') VALUES (8,'B312HB12','정우성','Y');