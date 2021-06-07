
<!DOCTYPE html>
<html>
<head>
<title>ARTICLES</title>
</head>
<body>

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

$sql = "SELECT ID,TITLE,NEWS,SENTI,CODE FROM sentinews";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo $row['TITLE'];
} else {
    echo "0 results";
}

$conn->close();
?>

</body>
</html>
