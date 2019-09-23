
<?php
session_start();
$pdo = new PDO('sqlite:./auth.db');
$id = session_id();

$sql = "UPDATE ninsho SET word='okkkkkk' WHERE id=?";
$stmt = $pdo->prepare($sql);
if($stmt->execute([$id])) {
	require('flag.php');
}

?>