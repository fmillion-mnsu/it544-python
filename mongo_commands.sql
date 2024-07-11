CREATE DATABASE SCOPED CREDENTIAL mongo_cred WITH 
    IDENTITY = 'admin', 
    SECRET = '<your password>'

CREATE EXTERNAL DATA SOURCE mongo_source WITH ( 
    LOCATION = 'mongodb://campus-quest.com:<mongo port>',
    CONNECTION_OPTIONS = 'tls=false; ssl=false',
    CREDENTIAL = mongo_cred
)
