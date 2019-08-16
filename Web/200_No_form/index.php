<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>No form</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
<div class="container">
	<div class="page-header" id="banner">
		<div class="row my-2">
			<div class="col-12">
				<h2 class="text-center mx-1 mt-5">No form</h2>
			</div>
		</div>
	</div>

	<section class="bs-docs-section clearfix">
		<div class="row">
			<div class="col-12">
				<p class="text-center mt-5">
				<?php
					if (isset($_POST['oluri'])) {
						if ($_POST['oluri'] === 'so_cute') {
							echo 'MaidakeCTF{If_the_configuration_of_the_website_is_bad_you_can_POST_without_the_form}';
						} else {
							echo 'Do you know Oluri?';
						}
					} else {
						echo 'Access Denied';
					}
				?>
				</p>
				<div class="card border-info w-75 mx-auto mt-5">
					<div class="card-body">
					<pre><code class="prettyprint lang-php">
	if (isset($_POST['oluri'])) {
		if ($_POST['oluri'] === 'so_cute') {
			echo 'Flag is here';
		} else {
			echo 'Do you know Oluri?';
		}
	} else {
		echo 'Access Denied';
	}
					</code></pre>
					</div>
				</div>
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
