------------------------------------------------------------
--          Program: System Monitor SystemMonitor.sql             
--              All rights reserved 2025                   
------------------------------------------------------------
--    From: Ekobots Innovation Ltda - www.ekobots.com      
--      by: Juan Sirgado y Antico - www.jsya.com.br        
------------------------------------------------------------
-- Date         : 2025-06-04
-- Version      : 1.0
-- Description  : System Monitor DDL file for PostgreSQL      
------------------------------------------------------------

------------------------------------------------------------
CREATE DATABASE db_sysmon OWNER = postgres 
       TABLESPACE = pg_default CONNECTION LIMIT = 32;
CREATE USER postgres WITH ENCRYPTED PASSWORD 'sirgadoa';
GRANT ALL PRIVILEGES ON DATABASE db_sysmon TO postgres;
USE db_sysmon;

-- DROP DATABASE db_sysmon;
------------------------------------------------------------

------------------------------------------------------------
CREATE TABLE tb_facility
      (fcl_sq_facility          DECIMAL(15)   NOT NULL,
       fcl_ts_facility          TIMESTAMPTZ   NOT NULL,
       fcl_nm_machine           VARCHAR(32)   NOT NULL,
       fcl_tp_facility          VARCHAR(16)   NOT NULL,
       fcl_id_facility          VARCHAR(64)   NOT NULL,
       fcl_vl_facility          DECIMAL(17,5) NOT NULL,
       fcl_tp_unit              VARCHAR(32)   NOT NULL,
       fcl_ds_alias             VARCHAR(16)   NOT NULL,
       fcl_ds_facility          VARCHAR(64)   NOT NULL);

-- DROP TABLE tb_facility;
------------------------------------------------------------

------------------------------------------------------------
CREATE SEQUENCE sq_tb_facility AS BIGINT START WITH 1 INCREMENT BY 1 
                OWNED BY tb_facility.fcl_sq_facility;

-- DROP SEQUENCE sq_tb_facility;
------------------------------------------------------------

------------------------------------------------------------
ALTER TABLE tb_facility 
            ADD CONSTRAINT pk_tb_facility
            PRIMARY KEY (fcl_sq_facility);

-- ALTER TABLE tb_facility 
--             DROP CONSTRAINT pk_tb_facility;
------------------------------------------------------------

------------------------------------------------------------
CREATE INDEX id_tb_facility 
             ON tb_facility (fcl_ts_facility ASC, 
                             fcl_nm_machine  ASC,
                             fcl_tp_facility ASC,
                             fcl_id_facility ASC);

-- DROP INDEX uk_tb_facility;
------------------------------------------------------------

------------------------------------------------------------
