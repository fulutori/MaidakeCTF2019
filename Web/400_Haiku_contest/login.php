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
				<p class="text-center mx-1">- ログインページ -</p>
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
					<input type="password" class="form-control mb-2 w-75 mx-auto" name="pass" placeholder="パスワード" required />
					</div>
					<?php
						if(isset($_POST['login'])) {
							session_start();
							$id = htmlspecialchars($_POST['id']);
							$pass = htmlspecialchars($_POST['pass']);

							$pdo = new PDO('sqlite:./sqlite/user.db');
							$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
							$pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

							$sql = "SELECT * FROM users WHERE id=?";
							$stmt = $pdo->prepare($sql);
							$stmt->execute([$id]);
							$result = $stmt->fetch(PDO::FETCH_ASSOC);
							if ($result['id']=="") {
								?><div class="alert alert-danger w-75 text-center mx-auto" role="alert">このユーザーは登録されていません</div><?php 
							} else {
								$db_hashed_pwd = $result['pass'];
								$user_id = $result['id'];
								if (password_verify($pass, $db_hashed_pwd)) {
									$_SESSION['user'] = $user_id;
									header("Location: ./index.php?id=$user_id");
								} else { 
									?><div class="alert alert-danger w-75 text-center mx-auto" role="alert">パスワードが一致しません</div><?php 
								}								
							}
						}
					?>
					<p class="text-center"><button type="submit" class="w-50 py-2 mt-2" name="login">ログイン</button></p>
				</form>
				<p class="text-center mt-5">登録は<a href="./register.php">こちら</a></p>
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
