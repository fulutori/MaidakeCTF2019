<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>Teleport</title>
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
				<h2 class="text-center mx-1 mt-5">Teleport</h2>
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
				<p class="text-center">latitude : 32.7526235<br>longitude : 129.8495163</p>
				<p class="text-center mx-1 mt-1" id="result"></p>
			</div>
		</div>
	</section>

	<footer class="footer">
		<div class="container mt-5">
			<p class="text-muted text-center">Copyright © aokakes All Rights Reserved.</p>
		</div>
	</footer>
</div>


<script>
function get_location() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(success, error, option);
		function success(position){
			if ((Math.abs(position.coords.latitude-32.7526235) <= 0.003) && (Math.abs(position.coords.longitude-129.8495163) <= 0.003)) {
				$.post('flag.php').done(function(data) {
					document.getElementById('result').innerHTML = data;
				});
			} else {
				document.getElementById('result').innerHTML = 'Access denied';
			}
		}
		function error(error){
			var errorMessage = {
				0: "原因不明のエラーが発生しました。",
				1: "位置情報が許可されませんでした。",
				2: "位置情報が取得できませんでした。",
				3: "タイムアウトしました。",
			};
			document.getElementById('result').innerHTML = errorMessage[error.code];
		}
		var option = {"enableHighAccuracy": true, "timeout": 1000, "maximumAge": 1000,};
	} else {
		alert("現在地を取得できませんでした");
	}
}
get_location();
</script>
</body>
</html>