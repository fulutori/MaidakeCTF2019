<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>Agent</title>
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
				<h2 class="text-center mx-1 mt-5">Agent</h2>
			</div>
		</div>
	</div>

	<section class="bs-docs-section clearfix">
		<div class="row">
			<div class="col-12">
				<p class="text-center mt-5">
				<?php
					$agent = $_SERVER['HTTP_USER_AGENT'];
					if (strpos($agent, 'Milvas') !== false) {
						echo 'MaidakeCTF{Impersonating_user_agents_is_so_easy}';
					} else {
						echo 'Access Denied';
					}
				?>
				</p>
				<div class="card border-info w-75 mx-auto mt-5">
					<div class="card-body">
					<pre><code class="prettyprint lang-php">
	$agent = $_SERVER['HTTP_USER_AGENT'];

	if (strpos($agent, 'Milvas') !== false) {
		echo 'FLAG is here';
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
