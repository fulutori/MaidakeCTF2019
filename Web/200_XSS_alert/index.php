<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>XSS alert</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<script type="text/javascript">
function getParam(name, url) {
	if (!url) url = window.location.href;
	name = name.replace(/[\[\]]/g, "\\$&");
	var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
			results = regex.exec(url);
	if (!results) return null;
	if (!results[2]) return '';
	return decodeURIComponent(results[2].replace(/\+/g, " "));
}
</script>

</head>
<body>
<div class="container">
	<div class="page-header" id="banner">
		<div class="row my-2">
			<div class="col-12">
				<h2 class="text-center mx-1 mt-5">XSS alert</h2>
				<div class="mt-5">
					<font size="5rem">
						<p id="error"><font color="#F00">javascriptを有効にしてください</font></p>
						<script type="text/javascript"> error.style.display = "none"; </script>
					</font>
				</div>
			</div>
		</div>
	</div>

	<section class="bs-docs-section clearfix">
		<div class="row">
			<div class="col-12">
				<p class="text-center mb-5">なんでもいいのでXSSしてください。</p>
				<form method="get">
					<input type="text" class="form-control mb-2 w-75 mx-auto" name="attack" placeholder="" required />
					<p class="text-center"><button type="submit" class="w-50 py-2 mt-2">攻撃</button></p>
				</form>
				<p class="text-center">攻撃内容：
					<span id="a_text">
						<?php
							$param = $_GET['attack'];
							echo $param;
							if (strpos($param, '<script>')!==false && strpos($param, '</script>')!==false) {
								echo '<script>alert("Congratulations!\n\nMaidakeCTF{Escape_is_a_simple_but_important_process}\n\n")</script>';
							}
						?>
					</span>
				</p>
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
