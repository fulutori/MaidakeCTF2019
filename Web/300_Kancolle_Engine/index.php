<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>Kancolle Engine</title>
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
				<h2 class="text-center mx-1 mt-5">Kancolle Engine</h2>
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
					<input type="text" class="form-control mb-2 w-75 mx-auto" name="md5" placeholder="ex) c82cfc524aa9a7e402d7a508b491b57b" required />
					</div>
					<p class="text-center"><button type="submit" class="w-50 py-2 my-2" name="search">検索</button></p>
					<?php
						if(isset($_POST['search'])) {
							$md5 = htmlspecialchars($_POST['md5']);

							$pdo = new PDO('sqlite:./sqlite/kancolle.db');
							$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
							$pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

							$sql = "SELECT * FROM ship WHERE md5='".$md5."'";

							$search = $pdo->prepare($sql);
							$search->execute();
							$result = $search->fetchAll(PDO::FETCH_ASSOC);

							if ($result[0]['md5'] == '') {
								?><div class="alert alert-danger w-75 text-center mx-auto" role="alert">このハッシュ値の艦娘は存在しません</div><?php 
							} else {
								echo '<table class="table table-hover table-striped">';
								echo '<thead><tr><th>Name</th><th>MD5</th></tr></thead>';
								echo '<tbody>';
								foreach ($result as $key => $value) {
									echo '<tr><td>'.$value['name'].'</td><td>'.$value['md5'].'</td></tr>';
								}
								echo '</tbody>';
								echo '</table>';
							}
						}
					?>
				</form>
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
