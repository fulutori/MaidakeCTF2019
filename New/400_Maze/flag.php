<?php
$flag = "MaidakeCTF{If_you_implement_it_poorly_another_file_may_be_screwed_in}";

session_start();
$pdo = new PDO('sqlite:./auth.db');
$id = session_id();

$sql = "SELECT word FROM ninsho WHERE id=?";
$stmt = $pdo->prepare($sql);
if($stmt->execute([$id])) {
	$result = $stmt->fetch(PDO::FETCH_ASSOC);
	if ($result['word'] == 'okkkkkk') {
		print_r($flag);
	}
}

?>