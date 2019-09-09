<?php
session_start();
if(!isset($_SESSION['user'])) {
	header("Location: login.php");
} else {
	$id = $_SESSION['user'];
	$pdo = new PDO('sqlite:./sqlite/user.db');
	$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	$pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
	$sql = "SELECT haiku FROM users WHERE id=?";
	$stmt = $pdo->prepare($sql);
	$stmt->execute([$_SESSION['user']]);
	$result = $stmt->fetch(PDO::FETCH_ASSOC);
	if ($result['haiku'] == '') {
		$haiku = '俳句が登録されていません';
	} else {
		$haiku = $result['haiku'];
	}
}
?>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>Haiku contest</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<style type="text/css">
.box30 {
    background: #f1f1f1;
    box-shadow: 4px 8px 8px 2px rgba(0, 0, 0, 0.22);
}
.box30 .box-title {
    font-size: 1.2em;
    background: #5fc2f5;
    padding: 4px;
    text-align: center;
    color: #FFF;
    font-weight: bold;
    letter-spacing: 0.05em;
}
</style>
</head>
<body>
<div class="container">
	<div class="page-header" id="banner">
		<div class="row my-2">
			<div class="col-12">
				<h2 class="text-center mx-1 mt-5">Haiku contest</h2>
				<div class="mt-5">
					<font size="5rem">
						<p id="error"><font color="#F00">javascriptを有効にしてください</font></p>
						<script type="text/javascript"> error.style.display = "none"; </script>
					</font>
				</div>
				<p class="lead text-center mx-1 mt-1" id="result"></p>
			</div>
		</div>
	</div>

	<section class="bs-docs-section clearfix">
		<div class="row">
			<div class="col-12">
				<div class="w-75 mx-auto mb-5">
					<div class="box30">
					<div class="box-title"><?php echo $_SESSION['user']; ?></div>
						<p class="text-center py-5"><?php echo $haiku; ?></p>
					</div>
				</div>

				<form method="post">
					<div class="form-group">
						<input type="text" class="form-control mb-2 w-75 mx-auto" name="haiku" placeholder="あなたの渾身の俳句を入力してください" required />
					</div>
					<?php
						if(isset($_POST['regist'])) {
							$haiku = $_POST['haiku'];
							$sql = "UPDATE users SET haiku=? WHERE id=?";
							$stmt = $pdo->prepare($sql);
							if ($stmt->execute([$haiku, $id])) {
								header("Location: ./index.php?id=$id");
							} else {
								?><div class="alert alert-danger w-75 text-center mx-auto" role="alert">エラーが発生しました</div><?php
							}
						}
					?>
					<p class="text-center"><button type="submit" class="w-50 py-2 mt-2" name="regist">登録</button></p>
				</form>

				<form method="post">
					<p class="text-center mt-5">あなたの渾身の俳句を採点することができます！</p>
					<p class="text-center"><button type="submit" class="w-50 py-2 btn-info" name="check">採点</button></p>
					<?php
						if(isset($_POST['check'])) {
							$cmd = "python3 check.py $id";
							#exec($cmd, $result);
							#echo $result;
						}
					?>
				</form>

				<p class="text-center mt-5"><a href="./logout.php">ログアウト</a></p>
			</div>
		</div>
	</section>

	<footer class="footer">
		<div class="container">
			<p class="text-muted text-center">Copyright © aokakes All Rights Reserved.</p>
		</div>
	</footer>
</div>
<script type="text/javascript">

</script>
</body>
</html>
