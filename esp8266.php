<?php

$Temp=$_POST["temperature"];
$Humidity=$_POST["humidity"];
$Write="<p>Temperature : " . $Temp . " Celcius </p>" . "<p>Humidity : " . $Humidity . " % </p>";

file_put_contents('index1.html',$Write);




?>