CREATE TABLE Players (
    PlayerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL,
    Email TEXT,
    RegisterDate DATE NOT NULL
);
CREATE TABLE Characters (
    CharID INTEGER PRIMARY KEY AUTOINCREMENT,
    PlayerID INTEGER NOT NULL,
    CharName TEXT NOT NULL,
    Gender TEXT,
    Age INTEGER,
    Profession TEXT,
    Level INTEGER NOT NULL,
    Exp INTEGER NOT NULL,
    FOREIGN KEY (PlayerID) REFERENCES Players (PlayerID)
);
CREATE TABLE Skills (
    SkillID INTEGER PRIMARY KEY AUTOINCREMENT,
    SkillName TEXT NOT NULL,
    Description TEXT,
    Damage INTEGER,
    ManaCost INTEGER
);
CREATE TABLE Equipments (
    EquipID INTEGER PRIMARY KEY AUTOINCREMENT,
    EquipName TEXT NOT NULL,
    Type TEXT,
    Level INTEGER,
    Effect TEXT
);
CREATE TABLE Quests (
    QuestID INTEGER PRIMARY KEY AUTOINCREMENT,
    QuestName TEXT NOT NULL,
    Description TEXT,
    Reward TEXT,
    Requirement TEXT
);
CREATE TABLE Maps (
    MapID INTEGER PRIMARY KEY AUTOINCREMENT,
    MapName TEXT NOT NULL,
    Description TEXT,
    Monsters TEXT,
    NPCs TEXT
);
CREATE TABLE PlayerEquipments (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PlayerID INTEGER NOT NULL,
    EquipID INTEGER NOT NULL,
    FOREIGN KEY (PlayerID) REFERENCES Players (PlayerID),
    FOREIGN KEY (EquipID) REFERENCES Equipments (EquipID)
);
CREATE TABLE PlayerSkills (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PlayerID INTEGER NOT NULL,
    SkillID INTEGER NOT NULL,
    FOREIGN KEY (PlayerID) REFERENCES Players (PlayerID),
    FOREIGN KEY (SkillID) REFERENCES Skills (SkillID)
);