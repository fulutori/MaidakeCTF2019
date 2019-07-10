<?php
$pdo = new PDO('sqlite:./sqlite/game2048.db');
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

if (!empty($_POST)) {
	$name = $_POST['name'];
	$score = $_POST['score'];	
	$max = $_POST['max'];
} else {
	outputRanking($pdo);
	exit(0);
}

$ranking = $pdo->prepare('SELECT * FROM ranking');
$ranking->execute();
$result = $ranking->fetchAll(PDO::FETCH_ASSOC);

# ランキングに誰も参加していないとき
if ($result == null) {
	$insert = $pdo->prepare('INSERT INTO ranking (name, score, max) VALUES (?, ?, ?)');
	$insert->execute([$name, $score, $max]);

# ランキングに1人以上いるとき
} else {
	foreach ($result as $key => $value) {

		# 既にスコアが登録されている人で自己最高点の場合はスコアを更新
		if (array_search($name, $value, true)) {
			if ($score > $value['score']) {
				$update = $pdo->prepare('UPDATE ranking SET score=?, max=? WHERE name=?');
				$update->execute([$score, $max, $name]);
			}
			break;
		}

		# スコアが登録されていない人はスコアを登録
		if ($value === end($result)) {
			$insert = $pdo->prepare('INSERT INTO ranking (name, score, max) VALUES (?, ?, ?)');
			$insert->execute([$name, $score, $max]);
		}
	}
}
outputRanking($pdo);

function outputRanking($pdo) {
	$ranking = $pdo->prepare('SELECT * FROM ranking ORDER BY score DESC');
	$ranking->execute();
	$result = $ranking->fetchAll(PDO::FETCH_ASSOC);

	# ランキング表を作成
	echo '<table class="table table-hover">';
	echo '<thead><tr><th>Rank</th><th>Name</th><th>Score</th><th>Max</th></tr></thead>';
	echo '<tbody>';
	foreach ($result as $key => $value) {
		echo '<tr><th>'.($key+1).'</th><td>'.$value['name'].'</td><td>'.$value['score'].'</td><td>'.$value['max'].'</td><tr>';
	}
	echo '</tbody>';
	echo '</table>';
}


?>