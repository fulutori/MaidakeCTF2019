<?php
$flag = "MaidakeCTF{We_can_output_javascript_variables_with_the_developer_tool_even_if_it_is_not_output_to_the_browser}";
if (empty($_SERVER["HTTP_REFERER"])) {
	echo 'Access denied';
	header('Location: ./');
} else {
	echo $flag;
}
?>