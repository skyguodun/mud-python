/*
 Navicat Premium Data Transfer

 Source Server         : mud
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 14/05/2024 13:30:53
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for player
-- ----------------------------
DROP TABLE IF EXISTS "player";
CREATE TABLE "player" (
  "id" INTEGER,
  "name" TEXT,
  "current_townid" INTEGER,
  "current_roomid" INTEGER,
  "health" INTEGER,
  "inner_power" INTEGER,
  "attack" INTEGER,
  "defense" INTEGER,
  "stamina" INTEGER,
  "hp" integer,
  "ip" integer,
  "ap" integer,
  "dp" integer,
  "sp" integer,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Records of player
-- ----------------------------
INSERT INTO "player" VALUES (1, 'sky', 101, 9, 100, 50, 50, 50, 50, 100, 50, 50, 50, 50);

PRAGMA foreign_keys = true;
