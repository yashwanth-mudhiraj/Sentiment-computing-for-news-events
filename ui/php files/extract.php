
<!DOCTYPE html>
<html>
<head>
<title>NEWS</title>
  <link rel="stylesheet" href="css/popup.css">


	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
	<link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/cardstyle.css">
	
	<link rel="stylesheet" href="css/stylescroll.css">
	<link rel="stylesheet" type="text/css" href="mystyle.css">
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
	<div class="container">
		<h1 style="font-size: 45px;">NEWS REVAMPED</h1>
	</div>
</div>

<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "news";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$temp = 'id01';
$sql = "SELECT ID,TITLE,NEWS,IMAGE,SENTI,CODE FROM sentinews";
$result = $conn->query($sql);
$i=0;
if ($result->num_rows > 0) {
    
    // output data of each row
    while($row = $result->fetch_assoc()) {
    	
    	echo '<figure class="snip1579"><img src="'.$row["IMAGE"].'">';
    	echo "<figcaption><h3>".$row["TITLE"]."</h3><blockquote><p>Sentiment :".$row["CODE"]."<br>Confidence :".$row["SENTI"]."</p>";
    	echo '</blockquote>';
    	

    	echo '</figcaption><button data-toggle="modal" href="#normalModal'.$i.'" class="btn btn-default mybutton">Read More	</button></figure>';
		  echo '<div id="normalModal'.$i.'" class="modal fade">
		  <div class="modal-dialog">
		    <div class="modal-content">
		      <div class="modal-header">
		        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
		        <h4 class="modal-title">'.$row["TITLE"].'</h4>
		      </div>
		      <div class="modal-body">
		        <p>'.$row["NEWS"].'</p>
		      </div>
		    </div><!-- /.modal-content -->
		  </div><!-- /.modal-dialog -->
		</div><!-- /.modal -->';
    $i=$i+1;	
    }
  
} else {
    echo "0 results";
}

$conn->close();
?>


<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js'></script>
    <script  src="js/scroll.js"></script>
    <script  src="js/cardindex.js"></script>
    <script  src="js/popup.js"></script>

</body>
</html>
