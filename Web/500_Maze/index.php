<?php
session_start();
$pdo = new PDO('sqlite:./auth.db');
$id = session_id();
$sql = "SELECT COUNT(*) FROM ninsho WHERE id=?";
$stmt = $pdo->prepare($sql);
if($stmt->execute([$id])) {
	$result = $stmt->fetchColumn();
	if ($result == 0) {
		$sql = "INSERT INTO ninsho(id,word) VALUES(?, 'nooooo')";
		$stmt = $pdo->prepare($sql);
		$stmt->execute([$id]);

	}
}
?>

<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>Maze</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<style type="text/css">
.box{
  animation: flash 1s linear infinite;
  background:#F00;
}

@keyframes flash {
  0%,100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}
</style>
</head>
<body>
<div class="container">
	<div class="page-header" id="banner">
		<div class="row my-2">
			<div class="col-12">
				<h2 class="text-center mx-1 mt-5">Maze</h2>
				<font size="5rem">
					<p id="error"><font color="#F00">javascriptを有効にしてください</font></p>
					<script type="text/javascript"> error.style.display = "none"; </script>
				</font>
			</div>
		</div>
	</div>

	<section class="bs-docs-section clearfix">
		<div class="row">
			<div class="col-12 text-center">
				<div id="canvas"></div>
				<button onclick="return makeMaze();" class="w-25 py-2" value="https://aokakes.sakura.ne.jp/aokakes/CTF/MaidakeCTF2019/Maze/hoge.csv" id="loadbutton">迷路を読み込む</button>
			</div>
		</div>
	</section>

	<footer class="footer">
		<div class="container mt-5">
			<p class="text-muted text-center">Copyright © aokakes All Rights Reserved.</p>
		</div>
	</footer>
</div>
<script type="text/javascript">
	var size = 33;
	var y = 21;
	var x = 0;

	function load() {
		var html = '<table border="1" class="mx-auto my-5" style="font-size: 0.5rem;">';
		for(var row=0; row<size; row++) {
			html += '<tr>';
			for(var col=0; col<size; col++) {
				var id = ('00'+row).slice(-2)+('00'+col).slice(-2);
				html += '<td align="center" valign="center" height="20" width="20" id="'+id+'"><p id="p'+id+'"></p></td>';
			}
			html += '</tr>';
		}

		html += '</table>';
		document.getElementById("canvas").innerHTML = html;

		
	}
	load();

	function makeMaze() {
		document.getElementById('loadbutton').style.display ="none";
		var req = new XMLHttpRequest();
		req.open("get", document.getElementById('loadbutton').value, true);
		req.send(null);
		
		req.onload = function(){
			var maze = [];
			var tmp = req.responseText.split("\n");
		 
			for(var i=0;i<tmp.length;++i){
				maze[i] = tmp[i].split(',');
			}
			draw(maze);
			start();
		}
	}

	function draw(maze) {
		for (var y = 0; y < 33; y++) {
			for (var x = 0; x < 33; x++) {
				id = ('00'+y).slice(-2)+('00'+x).slice(-2);
				if (maze[y][x] == 1) {
					document.getElementById('p'+id).innerHTML = "1";
					document.getElementById('p'+id).style.display ="none";
					document.getElementById(id).style.backgroundColor = getColor(1);
				} else if (maze[y][x] == 0) {
					document.getElementById('p'+id).innerHTML = "0";
					document.getElementById('p'+id).style.display ="none";
					document.getElementById(id).style.backgroundColor = getColor(0);
				} else if (maze[y][x] == 2) {
					document.getElementById('p'+id).innerHTML = "2";
					document.getElementById('p'+id).style.display ="none";
					document.getElementById(id).style.backgroundColor = getColor(2);
				} else if (maze[y][x] == 3) {
					document.getElementById('p'+id).innerHTML = "3";
					document.getElementById('p'+id).style.display ="none";
					document.getElementById(id).style.backgroundColor = getColor(3);
				}
			}
		}
	}

	function start() {
		document.getElementById('p2100').innerHTML = "9";
		document.getElementById('p2100').style.display ="none";
		document.getElementById('2100').style.backgroundColor = getColor(9);
		document.getElementById('2100').classList.add('box');
	}

	function sg() {
		if (x != 0) {
			document.getElementById('p2100').innerHTML = "2";
			document.getElementById('p2100').style.display ="none";
			document.getElementById('2100').style.backgroundColor = getColor(2);
		}
		if (x != 32) {
			document.getElementById('p2932').innerHTML = "3";
			document.getElementById('p2932').style.display ="none";
			document.getElementById('2932').style.backgroundColor = getColor(3);
		}
	}

	function getColor(val) {
		var color = "#ffffff";
		switch(val) {
			case 0:		color = "#FFF"; break;
			case 1:		color = "#000"; break;
			case 2:		color = "#00F"; break;
			case 3: 	color = "#0F0"; break;
			case 9: 	color = "#F00"; break;
		}
		return color;
	}

	function goal() {
		sg();
		if (x == 32 && y == 29) {
			$.post('result.php').done(function(data) {
				alert(data);
			});
		}
	}


	$(function(){
		$(document).keydown(function(event){
			var keyCode = event.keyCode;
			console.log('x: '+x+'  y: '+y);

			if (keyCode == 37) {
				if (x-1 >= 0 && document.getElementById('p'+('00'+y).slice(-2)+('00'+(x-1)).slice(-2)).textContent != 1) {
					document.getElementById('p'+('00'+y).slice(-2)+('00'+(x-1)).slice(-2)).innerHTML = 9;
					document.getElementById(('00'+y).slice(-2)+('00'+(x-1)).slice(-2)).style.backgroundColor = getColor(9);
					document.getElementById(('00'+y).slice(-2)+('00'+(x-1)).slice(-2)).classList.add('box');
					document.getElementById('p'+('00'+y).slice(-2)+('00'+x).slice(-2)).innerHTML = 0;
					document.getElementById(('00'+y).slice(-2)+('00'+x).slice(-2)).style.backgroundColor = getColor(0);
					document.getElementById(('00'+y).slice(-2)+('00'+x).slice(-2)).classList.remove('box');
					x--;
				}
				goal();
				return false;
			} else if (keyCode == 38) {
				if (y-1 >= 0 && document.getElementById('p'+('00'+(y-1)).slice(-2)+('00'+x).slice(-2)).textContent != 1) {
					document.getElementById('p'+('00'+(y-1)).slice(-2)+('00'+x).slice(-2)).innerHTML = 9;
					document.getElementById(('00'+(y-1)).slice(-2)+('00'+x).slice(-2)).style.backgroundColor = getColor(9);
					document.getElementById(('00'+(y-1)).slice(-2)+('00'+x).slice(-2)).classList.add('box');
					document.getElementById('p'+('00'+y).slice(-2)+('00'+x).slice(-2)).innerHTML = 0;
					document.getElementById(('00'+y).slice(-2)+('00'+x).slice(-2)).style.backgroundColor = getColor(0);
					document.getElementById(('00'+y).slice(-2)+('00'+x).slice(-2)).classList.remove('box');
					y--;
				}
				goal();
				return false;
			} else if (keyCode == 39) {
				if (x+1 < 33 && document.getElementById('p'+('00'+y).slice(-2)+('00'+(x+1)).slice(-2)).textContent != 1) {
					document.getElementById('p'+('00'+y).slice(-2)+('00'+(x+1)).slice(-2)).innerHTML = 9;
					document.getElementById(('00'+y).slice(-2)+('00'+(x+1)).slice(-2)).style.backgroundColor = getColor(9);
					document.getElementById(('00'+y).slice(-2)+('00'+(x+1)).slice(-2)).classList.add('box');
					document.getElementById('p'+('00'+y).slice(-2)+('00'+x).slice(-2)).innerHTML = 0;
					document.getElementById(('00'+y).slice(-2)+('00'+x).slice(-2)).style.backgroundColor = getColor(0);
					document.getElementById(('00'+y).slice(-2)+('00'+x).slice(-2)).classList.remove('box');
					x++;
				}
				goal();
				return false;
			} else if (keyCode == 40) {
				if (y+1 < 33 && document.getElementById('p'+('00'+(y+1)).slice(-2)+('00'+x).slice(-2)).textContent != 1) {
					document.getElementById('p'+('00'+(y+1)).slice(-2)+('00'+x).slice(-2)).innerHTML = 9;
					document.getElementById(('00'+(y+1)).slice(-2)+('00'+x).slice(-2)).style.backgroundColor = getColor(9);
					document.getElementById(('00'+(y+1)).slice(-2)+('00'+x).slice(-2)).classList.add('box');
					document.getElementById('p'+('00'+y).slice(-2)+('00'+x).slice(-2)).innerHTML = 0;
					document.getElementById(('00'+y).slice(-2)+('00'+x).slice(-2)).style.backgroundColor = getColor(0);
					document.getElementById(('00'+y).slice(-2)+('00'+x).slice(-2)).classList.remove('box');
					y++;
				}
				goal();
				return false;
			}
		});
	});

	//makeMaze();
</script>
</body>
</html>
