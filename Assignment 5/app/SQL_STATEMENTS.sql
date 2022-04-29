BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);


-- FUEL QUOTE AND PRICING MODULE 
CREATE TABLE IF NOT EXISTS "web_app_fuel_quote" (
	"id"	integer NOT NULL,
	"gallons_requested"	integer NOT NULL,
	"delivery_address"	varchar(100) NOT NULL,
	"delivery_date"	date NOT NULL,
	"suggested_price"	integer NOT NULL,
	"total_due"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "web_app_pricing_module" (
	"id"	integer NOT NULL,
	"suggested_price"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);


CREATE TABLE IF NOT EXISTS "web_app_usercredentials_groups" (
	"id"	integer NOT NULL,
	"usercredentials_id"	bigint NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("usercredentials_id") REFERENCES "web_app_usercredentials"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "web_app_usercredentials_user_permissions" (
	"id"	integer NOT NULL,
	"usercredentials_id"	bigint NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("usercredentials_id") REFERENCES "web_app_usercredentials"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	bigint NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "web_app_usercredentials"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);

-- CLIENT INFORMATION AND USER CREDENTIALS
CREATE TABLE IF NOT EXISTS "web_app_clientinformation" (
	"id"	integer NOT NULL,
	"fullname"	varchar(50) NOT NULL,
	"address1"	varchar(100) NOT NULL,
	"address2"	varchar(100) NOT NULL,
	"city"	varchar(100) NOT NULL,
	"state"	varchar(2) NOT NULL,
	"zipcode"	varchar(9) NOT NULL,
	"user_id"	bigint UNIQUE,
	FOREIGN KEY("user_id") REFERENCES "web_app_usercredentials"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "web_app_usercredentials" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(50) NOT NULL UNIQUE,
	"first_name"	varchar(150) NOT NULL,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"is_admin"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2022-03-30 17:16:28.912744');
INSERT INTO "django_migrations" VALUES (2,'contenttypes','0002_remove_content_type_name','2022-03-30 17:16:28.981560');
INSERT INTO "django_migrations" VALUES (3,'auth','0001_initial','2022-03-30 17:16:29.054549');
INSERT INTO "django_migrations" VALUES (4,'auth','0002_alter_permission_name_max_length','2022-03-30 17:16:29.104107');
INSERT INTO "django_migrations" VALUES (5,'auth','0003_alter_user_email_max_length','2022-03-30 17:16:29.138144');
INSERT INTO "django_migrations" VALUES (6,'auth','0004_alter_user_username_opts','2022-03-30 17:16:29.179638');
INSERT INTO "django_migrations" VALUES (7,'auth','0005_alter_user_last_login_null','2022-03-30 17:16:29.220949');
INSERT INTO "django_migrations" VALUES (8,'auth','0006_require_contenttypes_0002','2022-03-30 17:16:29.246759');
INSERT INTO "django_migrations" VALUES (9,'auth','0007_alter_validators_add_error_messages','2022-03-30 17:16:29.287862');
INSERT INTO "django_migrations" VALUES (10,'auth','0008_alter_user_username_max_length','2022-03-30 17:16:29.323978');
INSERT INTO "django_migrations" VALUES (11,'auth','0009_alter_user_last_name_max_length','2022-03-30 17:16:29.354575');
INSERT INTO "django_migrations" VALUES (12,'auth','0010_alter_group_name_max_length','2022-03-30 17:16:29.387649');
INSERT INTO "django_migrations" VALUES (13,'auth','0011_update_proxy_permissions','2022-03-30 17:16:29.412586');
INSERT INTO "django_migrations" VALUES (14,'auth','0012_alter_user_first_name_max_length','2022-03-30 17:16:29.438255');
INSERT INTO "django_migrations" VALUES (15,'web_app','0001_initial','2022-03-30 17:16:29.498836');
INSERT INTO "django_migrations" VALUES (16,'admin','0001_initial','2022-03-30 17:16:29.554868');
INSERT INTO "django_migrations" VALUES (17,'admin','0002_logentry_remove_auto_add','2022-03-30 17:16:29.604607');
INSERT INTO "django_migrations" VALUES (18,'admin','0003_logentry_add_action_flag_choices','2022-03-30 17:16:29.646857');
INSERT INTO "django_migrations" VALUES (19,'sessions','0001_initial','2022-03-30 17:16:29.679934');
INSERT INTO "django_migrations" VALUES (20,'web_app','0002_clientinformation_user','2022-03-30 17:51:27.838795');
INSERT INTO "django_migrations" VALUES (21,'web_app','0003_alter_usercredentials_managers_and_more','2022-04-01 06:30:44.251640');
INSERT INTO "django_migrations" VALUES (22,'web_app','0004_usercredentials_is_admin','2022-04-01 15:49:24.438134');
INSERT INTO "django_migrations" VALUES (23,'web_app','0005_alter_usercredentials_is_superuser','2022-04-01 16:18:49.638532');
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','permission');
INSERT INTO "django_content_type" VALUES (3,'auth','group');
INSERT INTO "django_content_type" VALUES (4,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (5,'sessions','session');
INSERT INTO "django_content_type" VALUES (6,'web_app','clientinformation');
INSERT INTO "django_content_type" VALUES (7,'web_app','fuel_quote');
INSERT INTO "django_content_type" VALUES (8,'web_app','pricing_module');
INSERT INTO "django_content_type" VALUES (9,'web_app','usercredentials');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (14,4,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (15,4,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (16,4,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (17,5,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (18,5,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (19,5,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (20,5,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (21,6,'add_clientinformation','Can add client information');
INSERT INTO "auth_permission" VALUES (22,6,'change_clientinformation','Can change client information');
INSERT INTO "auth_permission" VALUES (23,6,'delete_clientinformation','Can delete client information');
INSERT INTO "auth_permission" VALUES (24,6,'view_clientinformation','Can view client information');
INSERT INTO "auth_permission" VALUES (25,7,'add_fuel_quote','Can add fuel_ quote');
INSERT INTO "auth_permission" VALUES (26,7,'change_fuel_quote','Can change fuel_ quote');
INSERT INTO "auth_permission" VALUES (27,7,'delete_fuel_quote','Can delete fuel_ quote');
INSERT INTO "auth_permission" VALUES (28,7,'view_fuel_quote','Can view fuel_ quote');
INSERT INTO "auth_permission" VALUES (29,8,'add_pricing_module','Can add pricing_ module');
INSERT INTO "auth_permission" VALUES (30,8,'change_pricing_module','Can change pricing_ module');
INSERT INTO "auth_permission" VALUES (31,8,'delete_pricing_module','Can delete pricing_ module');
INSERT INTO "auth_permission" VALUES (32,8,'view_pricing_module','Can view pricing_ module');
INSERT INTO "auth_permission" VALUES (33,9,'add_usercredentials','Can add user');
INSERT INTO "auth_permission" VALUES (34,9,'change_usercredentials','Can change user');
INSERT INTO "auth_permission" VALUES (35,9,'delete_usercredentials','Can delete user');
INSERT INTO "auth_permission" VALUES (36,9,'view_usercredentials','Can view user');
INSERT INTO "django_admin_log" VALUES (1,'2022-04-01 15:59:33.418421','2','Test_User','',9,1,3);
INSERT INTO "django_admin_log" VALUES (2,'2022-04-01 16:45:23.260065','3','Test_User','',9,1,3);
INSERT INTO "django_session" VALUES ('8qhdzkc8vypukiyw8jtpftf49xv0sxex','.eJxVjEEOwiAQRe_C2pCplAFcuu8ZyAwDUjVtUtqV8e7apAvd_vfef6lI21rj1vISR1EX1avT78aUHnnagdxpus06zdO6jKx3RR-06WGW_Lwe7t9BpVa_NUIx0lkTAAXIJOEQzmxdQPDIFooHESTXU2JJgdCTKeCJ2HVowan3B9oXN88:1naKQo:ugeZ8Cxfffmt8SJalmAeMhRsrIHBjVSomedtIUMJkTg','2022-04-15 16:47:26.802270');
INSERT INTO "web_app_clientinformation" VALUES (3,'','','','','','',4);
INSERT INTO "web_app_usercredentials" VALUES (1,'pbkdf2_sha256$320000$K2DrCxUwVnNPAfb7bEISS2$ivUKArExB2v+uQMgwjloctYbI9zYSi2/Y9SFW8ktpXo=','2022-04-01 16:03:44.229107',1,'elect','','','koberunnels@gmail.com',1,1,'2022-03-30 21:29:32.596446',0);
INSERT INTO "web_app_usercredentials" VALUES (4,'pbkdf2_sha256$320000$n8ZhXqmhT5py2gbDx4I7VG$YvFvCPSBPm22yP3eFT9wjSfr6OCsO9v7M9ThjDsE0DQ=','2022-04-01 16:47:26.777474',0,'Test_User','','','',0,1,'2022-04-01 16:45:31.571494',0);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "web_app_usercredentials_groups_usercredentials_id_group_id_f8f20a4c_uniq" ON "web_app_usercredentials_groups" (
	"usercredentials_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "web_app_usercredentials_groups_usercredentials_id_5fbbd446" ON "web_app_usercredentials_groups" (
	"usercredentials_id"
);
CREATE INDEX IF NOT EXISTS "web_app_usercredentials_groups_group_id_d95dde3f" ON "web_app_usercredentials_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "web_app_usercredentials_user_permissions_usercredentials_id_permission_id_41b3a459_uniq" ON "web_app_usercredentials_user_permissions" (
	"usercredentials_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "web_app_usercredentials_user_permissions_usercredentials_id_dc643f9b" ON "web_app_usercredentials_user_permissions" (
	"usercredentials_id"
);
CREATE INDEX IF NOT EXISTS "web_app_usercredentials_user_permissions_permission_id_637a5770" ON "web_app_usercredentials_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
COMMIT;

