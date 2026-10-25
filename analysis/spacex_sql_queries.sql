-- IBM SpaceX capstone: SQL exploration tasks 1–10
-- Run after importing IBM SkillsNetwork labs/module_2/data/Spacex.csv
-- into SQLite table SPACEXTABLE. Columns follow the lab's Spacex.csv.
-- 1 Unique launch sites
SELECT DISTINCT Launch_Site FROM SPACEXTABLE;
-- 2 Five sites beginning CCA
SELECT Date, Launch_Site, Booster_Version FROM SPACEXTABLE WHERE Launch_Site LIKE 'CCA%' LIMIT 5;
-- 3 NASA CRS payload
SELECT SUM(PAYLOAD_MASS__KG_) AS nasa_crs_payload_kg FROM SPACEXTABLE WHERE Customer LIKE '%NASA (CRS)%';
-- 4 F9 v1.1 mean payload
SELECT AVG(PAYLOAD_MASS__KG_) AS avg_mass_kg FROM SPACEXTABLE WHERE TRIM(Booster_Version)='F9 v1.1';
-- 5 First ground-pad success
SELECT MIN(Date) AS first_ground_landing FROM SPACEXTABLE WHERE Landing_Outcome='Success (ground pad)';
-- 6 Drone-ship successes (4000 < mass < 6000)
SELECT DISTINCT Booster_Version FROM SPACEXTABLE WHERE Landing_Outcome='Success (drone ship)' AND PAYLOAD_MASS__KG_ > 4000 AND PAYLOAD_MASS__KG_ < 6000;
-- 7 Mission outcomes
SELECT TRIM(Mission_Outcome) AS Mission_Outcome, COUNT(*) AS total FROM SPACEXTABLE GROUP BY TRIM(Mission_Outcome) ORDER BY total DESC;
-- 8 Boosters with highest payload
SELECT Booster_Version, Date, PAYLOAD_MASS__KG_ FROM SPACEXTABLE WHERE PAYLOAD_MASS__KG_=(SELECT MAX(PAYLOAD_MASS__KG_) FROM SPACEXTABLE);
-- 9 2015 failed drone-ship landings
SELECT substr(Date,6,2) AS month, Date, Booster_Version, Launch_Site FROM SPACEXTABLE WHERE substr(Date,1,4)='2015' AND Landing_Outcome='Failure (drone ship)';
-- 10 Landing outcome ranks over the specified historical window
SELECT Landing_Outcome, COUNT(*) AS total FROM SPACEXTABLE WHERE Date BETWEEN '2010-06-04' AND '2017-03-20' GROUP BY Landing_Outcome ORDER BY total DESC;
