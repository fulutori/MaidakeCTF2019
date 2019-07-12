<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>SHA-1 collision</title>
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
				<h2 class="text-center mx-1 mt-5">SHA-1 collision</h2>
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
				<form method="POST" enctype="multipart/form-data">
					<div class="w-100 text-center">
						<input type="file" name="file_1" class="py-2">
					</div>
					<div class="w-100 text-center mb-5">
						<input type="file" name="file_2" class="py-2">
					</div>
					<?php
						if(isset($_POST['compare'])) {
							$file_1 = $_FILES['file_1']['tmp_name'];
							$file_2 = $_FILES['file_2']['tmp_name'];
							$md5_f1 = md5_file($file_1);
							$md5_f2 = md5_file($file_2);
							$sha1_f1 = sha1_file($file_1);
							$sha1_f2 = sha1_file($file_2);

							if(is_uploaded_file($file_1) && is_uploaded_file($file_2)){

								if ($md5_f1 !== $md5_f2) {
									if ($sha1_f1 === $sha1_f2) {
										echo '<div class="card text-white bg-primary">';
										echo '<div class="card-header">';
										echo '比較結果';
										echo '</div>';
										echo '<div class="card-body">';
										echo '<h3 class="card-title">成功</h3><hr>';
										echo '<div class="card-text">';
										echo '<h5>[MD5]</h5>';
										echo $_FILES['file_1']['name'].' : '.$md5_f1.'<br>';
										echo $_FILES['file_2']['name'].' : '.$md5_f2.'<br>';
										echo '<hr><h5>[SHA-1]</h5>';
										echo $_FILES['file_1']['name'].' : '.$sha1_f1.'<br>';
										echo $_FILES['file_2']['name'].' : '.$sha1_f2.'<br>';
										echo '<hr><h5>[Flag]</h5>';
										echo 'MaidakeCTF{It_is_a_little_hard_to_create_a_file_where_SHA-1_collides}';
										echo '</div></div></div>';
									} else {
										echo '<div class="card text-white bg-danger">';
										echo '<div class="card-header">';
										echo '比較結果';
										echo '</div>';
										echo '<div class="card-body">';
										echo '<h3 class="card-title">失敗</h3><hr>';
										echo '<div class="card-text">';
										echo '<h5>[MD5]</h5>';
										echo $_FILES['file_1']['name'].' : '.$md5_f1.'<br>';
										echo $_FILES['file_2']['name'].' : '.$md5_f2.'<br>';
										echo '<hr><h5>[SHA-1]</h5>';
										echo $_FILES['file_1']['name'].' : '.$sha1_f1.'<br>';
										echo $_FILES['file_2']['name'].' : '.$sha1_f2.'<br>';
										echo '</div></div></div>';
									}
								} else if ($md5_f1 === $md5_f2) {
									echo '<div class="card text-white bg-danger">';
									echo '<div class="card-header">';
									echo '比較結果';
									echo '</div>';
									echo '<div class="card-body">';
									echo '<h3 class="card-title">失敗 ※異なるファイルを選択してください</h3><hr>';
									echo '<div class="card-text">';
									echo '<h5>[MD5]</h5>';
									echo $_FILES['file_1']['name'].' : '.$md5_f1.'<br>';
									echo $_FILES['file_2']['name'].' : '.$md5_f2.'<br>';
									echo '<hr><h5>[SHA-1]</h5>';
									echo $_FILES['file_1']['name'].' : '.$sha1_f1.'<br>';
									echo $_FILES['file_2']['name'].' : '.$sha1_f2.'<br>';
									echo '</div></div></div>';
								}
							} else {
								echo '<div class="card text-white bg-dark">';
								echo '<div class="card-header">';
								echo '比較結果';
								echo '</div>';
								echo '<div class="card-body">';
								echo '<h3 class="card-title">失敗 ※2つのファイルを選択してください</h3><hr>';
								echo '<div class="card-text">';
								echo '<h5>[MD5]</h5>';
								echo $_FILES['file_1']['name'].' : '.$md5_f1.'<br>';
								echo $_FILES['file_2']['name'].' : '.$md5_f2.'<br>';
								echo '<hr><h5>[SHA-1]</h5>';
								echo $_FILES['file_1']['name'].' : '.$sha1_f1.'<br>';
								echo $_FILES['file_2']['name'].' : '.$sha1_f2.'<br>';
								echo '</div></div></div>';
							}

						}
					?>
					<p class="text-center"><button type="submit" class="w-50 py-2 mt-5" name="compare">比較</button></p>
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