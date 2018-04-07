<?php
if(isset($_POST['str'])){
	$str=$_POST['str'];
	$file = fopen("post.txt", "w");    
    fwrite($file, $str);
    fclose($file);
    header("Location: /project.py");
}else{
?>
<form action="form.php" method="post">
	<input type="text" name="str" value="journey2taste" placeholder="ProfileName">
	<input type="submit" >
</form>
<?php } ?>