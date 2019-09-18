<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>Haiku contest</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
<div class="container">
	<div class="page-header" id="banner">
		<div class="row my-2">
			<div class="col-12">
				<h2 class="text-center mx-1 mt-5">Haiku contest</h2>
				<p class="text-center mx-1">- 登録ページ -</p>
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
				<form method="post">
					<div class="form-group">
					<input type="text" class="form-control mb-2 w-75 mx-auto" name="id" placeholder="ID" required />
					<input type="password" class="form-control mb-2 w-75 mx-auto" name="pass1" placeholder="パスワード" required />
					<input type="password" class="form-control mb-2 w-75 mx-auto" name="pass2" placeholder="もう一度パスワードを入力してください" required />
					</div>
					<?php
						if(isset($_POST['regist'])) {
							$id = htmlspecialchars($_POST['id']);
							$pass1 = htmlspecialchars($_POST['pass1']);
							$pass2 = htmlspecialchars($_POST['pass2']);
							if (strcmp($pass1, $pass2) != 0) {
								?><div class="alert alert-danger w-75 text-center mx-auto" role="alert">1つ目と2つ目のパスワードが一致しません。</div><?php
							} else {
								$pdo = new PDO('sqlite:./sqlite/user.db');

								$sql = "SELECT COUNT(*) FROM users WHERE id=?";
								$stmt = $pdo->prepare($sql);
								if($stmt->execute([$id])) {
									$result = $stmt->fetchColumn();
									if ($result != 0) {
										?><div class="alert alert-danger w-75 text-center mx-auto" role="alert">このユーザー名は既に登録されています</div><?php
									} else {
										$sql = "INSERT INTO users(id,pass) VALUES(?, ?)";
										$stmt = $pdo->prepare($sql);
										$pass = password_hash($pass1, PASSWORD_DEFAULT);
										if($stmt->execute([$id, $pass])) {
											?><div class="alert alert-success w-75 text-center mx-auto" role="alert">登録しました</div><?php
										} else {
											?><div class="alert alert-danger w-75 text-center mx-auto" role="alert">エラーが発生しました</div><?php
										}
									}
								}
							}
						}
					?>
					<p class="text-center"><button type="submit" class="w-50 py-2 mt-2" name="regist">登録</button></p>
				</form>
				<p class="text-center mt-5">ログインは<a href="./login.php">こちら</a></p>
			</div>
		</div>
	</section>

	<footer class="footer">
		<div class="container mt-5">
			<p class="text-muted text-center">Copyright © aokakes All Rights Reserved.</p>
		</div>
	</footer>
</div>
</body>
</html>
