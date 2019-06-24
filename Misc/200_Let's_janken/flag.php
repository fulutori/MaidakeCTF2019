<?php
$flag = "MaidakeCTF{button_mashing_is_not_the_right_solution}";
if(!isset($_COOKIE['victory'])){
	echo "おや、cookieをお持ちでない？それではFlagはあげられませんねぇ。\n";
} else {
	if ($_COOKIE['victory'] >= 1000) {
		echo $flag;
	} else {
		echo "残念！直接見に来ても無駄ですよ～\n";
	}
}
?>