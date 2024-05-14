/*
 Navicat Premium Data Transfer

 Source Server         : mud
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 13/05/2024 19:07:18
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for towns
-- ----------------------------
DROP TABLE IF EXISTS "towns";
CREATE TABLE "towns" (
  "town_id" INTEGER,
  "town_name" TEXT NOT NULL,
  "town_description" TEXT,
  PRIMARY KEY ("town_id")
);

-- ----------------------------
-- Records of towns
-- ----------------------------
INSERT INTO "towns" VALUES (1, '新手村', '所有冒险开始的地方，一个宁静的小村庄。');
INSERT INTO "towns" VALUES (2, '待建', '待建');

PRAGMA foreign_keys = true;
