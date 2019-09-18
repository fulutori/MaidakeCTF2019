<?php
session_start();
if(isset($_GET['logout'])) {
  session_destroy();
  unset($_SESSION['user']);
  header("Location: login.php");
} else {
  header("Location: login.php");
}
?>