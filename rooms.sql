/*
 Navicat Premium Data Transfer

 Source Server         : mud
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 14/05/2024 13:31:06
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for rooms
-- ----------------------------
DROP TABLE IF EXISTS "rooms";
CREATE TABLE "rooms" (
  "room_id" INTEGER,
  "town_id" INTEGER NOT NULL,
  "room_name" TEXT NOT NULL,
  "room_description" TEXT,
  "direction_e" integer,
  "direction_s" integer,
  "direction_w" integer,
  "direction_n" integer,
  PRIMARY KEY ("room_id"),
  FOREIGN KEY ("town_id") REFERENCES "towns" ("town_id") ON DELETE NO ACTION ON UPDATE NO ACTION
)
WITHOUT ROWID;

-- ----------------------------
-- Records of rooms
-- ----------------------------
INSERT INTO "rooms" VALUES (1, 101, '村长家', '村长家内灯火通明，村长正在用餐。', 9, 4, 0, 0);
INSERT INTO "rooms" VALUES (4, 101, '客栈', '客栈位于村中南北交汇处，店内几位疲惫的旅人正在用餐。', 0, 12, 0, 1);
INSERT INTO "rooms" VALUES (5, 101, '铁匠铺', '火炉旁，铁匠正敲打着一块烧红的铁块，火星四溅。', 0, 13, 9, 8);
INSERT INTO "rooms" VALUES (6, 101, '药铺', '药铺里摆满了各种草药和丹药，一位大夫正在研磨药材。', 7, 0, 0, 11);
INSERT INTO "rooms" VALUES (7, 101, '茶馆', '茶馆内弥漫着淡淡的茶香，几位老者正在悠闲地下棋。', 9, 0, 6, 10);
INSERT INTO "rooms" VALUES (8, 101, '武馆', '武馆内弟子们正在练习武术，拳风阵阵，气势如虹。', 0, 0, 4, 14);
INSERT INTO "rooms" VALUES (9, 101, '村口', '一条蜿蜒的小路，往北通向一个宁静的小村，两旁是郁郁葱葱的竹林。西边好像有人声。', 0, 0, 7, 11);
INSERT INTO "rooms" VALUES (10, 101, '市集', '这是在村西的市集。热闹的市集上摆满了各种摊位，叫卖声此起彼伏。', 11, 7, 1, 13);
INSERT INTO "rooms" VALUES (11, 101, '村中小道', ' 一条普普通的村间小路，往北走是一个客栈，南边是村口，西边很得热闹。', 6, 9, 10, 12);
INSERT INTO "rooms" VALUES (12, 101, '村中小道', '一条蜿蜒的小路，两旁是郁郁葱葱的竹林。往南走是通往村口，往北走是一个客栈。', 0, 11, 13, 4);
INSERT INTO "rooms" VALUES (13, 101, '村中小道', '一条笔直的小路，南边很是热闹，东边是一条村中小路，北边传来打铁的声音。', 12, 10, 11, 5);
INSERT INTO "rooms" VALUES (14, 101, '无名小山', '村北边的无名小山', 0, 8, 0, 15);
INSERT INTO "rooms" VALUES (15, 101, '山洞', '无名小山的山洞', 0, 14, 0, 0);

PRAGMA foreign_keys = true;
