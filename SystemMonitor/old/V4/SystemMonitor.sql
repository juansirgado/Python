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
CREATE TABLE tb_processor
      (prc_ts_facility          TIMESTAMP     NOT NULL,
       prc_nm_machine           VARCHAR(32)   NOT NULL,
       prc_vl_facility          DECIMAL(17,5) NOT NULL,
       prc_tp_unit              VARCHAR(32)   NOT NULL,
       prc_ds_facility          VARCHAR(64)   NOT NULL);

CREATE TABLE tb_memory
      (mem_ts_facility          TIMESTAMP     NOT NULL,
       mem_nm_machine           VARCHAR(32)   NOT NULL,
       mem_vl_facility          DECIMAL(17,5) NOT NULL,
       mem_tp_unit              VARCHAR(32)   NOT NULL,
       mem_ds_facility          VARCHAR(64)   NOT NULL);

CREATE TABLE tb_storage
      (str_ts_facility          TIMESTAMP     NOT NULL,
       str_nm_machine           VARCHAR(32)   NOT NULL,
       str_vl_facility          DECIMAL(17,5) NOT NULL,
       str_tp_unit              VARCHAR(32)   NOT NULL,
       str_ds_facility          VARCHAR(64)   NOT NULL);

CREATE TABLE tb_network
      (net_ts_facility          TIMESTAMP     NOT NULL,
       net_nm_machine           VARCHAR(32)   NOT NULL,
       net_vl_facility          DECIMAL(17,5) NOT NULL,
       net_tp_unit              VARCHAR(32)   NOT NULL,
       net_ds_facility          VARCHAR(64)   NOT NULL);

CREATE TABLE tb_task
      (tsk_ts_facility          TIMESTAMP     NOT NULL,
       tsk_nm_machine           VARCHAR(32)   NOT NULL,
       tsk_vl_facility          DECIMAL(17,5) NOT NULL,
       tsk_tp_unit              VARCHAR(32)   NOT NULL,
       tsk_ds_facility          VARCHAR(64)   NOT NULL);

CREATE TABLE tb_machine
      (mch_ts_facility          TIMESTAMP     NOT NULL,
       mch_nm_machine           VARCHAR(32)   NOT NULL,
       mch_vl_facility          DECIMAL(17,5) NOT NULL,
       mch_tp_unit              VARCHAR(32)   NOT NULL,
       mch_ds_facility          VARCHAR(64)   NOT NULL);

-- DROP TABLE tb_processor;
-- DROP TABLE tb_memory;
-- DROP TABLE tb_storage;
-- DROP TABLE tb_network;
-- DROP TABLE tb_task;
-- DROP TABLE tb_machine;
------------------------------------------------------------

------------------------------------------------------------
CREATE UNIQUE INDEX uk_prc_ts_processor   ON tb_processor (prc_ts_processor ASC, prc_nm_machine ASC);
CREATE UNIQUE INDEX uk_mem_ts_memory      ON tb_memory    (mem_ts_memory ASC,    mem_nm_machine ASC);
CREATE UNIQUE INDEX uk_str_ts_storage     ON tb_storage   (str_ts_storage ASC,   str_nm_machine ASC);
CREATE UNIQUE INDEX uk_net_ts_network     ON tb_network   (net_ts_network ASC,   net_nm_machine ASC);
CREATE UNIQUE INDEX uk_tsk_ts_task        ON tb_task      (tsk_ts_task ASC,      tsk_nm_machine ASC);
CREATE UNIQUE INDEX uk_mch_ts_machine     ON tb_machine   (mch_ts_machine ASC,   mch_nm_machine ASC);

-- DROP INDEX uk_prc_ts_processor;
-- DROP INDEX uk_mem_ts_memory;
-- DROP INDEX uk_str_ts_storage;
-- DROP INDEX uk_net_ts_network;
-- DROP INDEX uk_tsk_ts_task;
-- DROP INDEX uk_mch_ts_machine;
------------------------------------------------------------

------------------------------------------------------------
ALTER TABLE tb_processor ADD CONSTRAINT pk_prc_ts_processor PRIMARY KEY (prc_ts_processor, prc_nm_machine);
ALTER TABLE tb_memory    ADD CONSTRAINT pk_mem_ts_memory    PRIMARY KEY (mem_ts_memory,    mem_nm_machine);
ALTER TABLE tb_storage   ADD CONSTRAINT pk_str_ts_storage   PRIMARY KEY (str_ts_storage,   str_nm_machine);
ALTER TABLE tb_network   ADD CONSTRAINT pk_net_ts_network   PRIMARY KEY (net_ts_network,   net_nm_machine);
ALTER TABLE tb_task      ADD CONSTRAINT pk_tsk_ts_task      PRIMARY KEY (tsk_ts_task,      tsk_nm_machine);
ALTER TABLE tb_machine   ADD CONSTRAINT pk_mch_ts_machine   PRIMARY KEY (mch_ts_machine,   mch_nm_machine);

-- DROP CONSTRAINT pk_prc_ts_processor;
-- DROP CONSTRAINT pk_mem_ts_memory;
-- DROP CONSTRAINT pk_str_ts_storage;
-- DROP CONSTRAINT pk_net_ts_network;
-- DROP CONSTRAINT pk_tsk_ts_task;
-- DROP CONSTRAINT pk_mch_ts_machine;
------------------------------------------------------------


------------------------------------------------------------
-- CREATE SEQUENCE sq_processor AS BIGINT INCREMENT BY 1 START WITH 1 OWNED BY tb_processor.prc_sq_processor;

-- DROP SEQUENCE  sq_processor;
------------------------------------------------------------

------------------------------------------------------------
COMMIT;
------------------------------------------------------------
