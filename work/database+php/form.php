<?php

// servername => localhost
// username => root
// password => empty
// database name => staff
$conn = mysqli_connect("sql8.endora.cz:3313", "samsemodaorbis", "Semoda2008@", "samuelsemoda");
        
// Check connection
if($conn === false){
    die("ERROR: Could not connect. " 
        . mysqli_connect_error());
    }

if ($_SERVER["REQUEST_METHOD"] == "POST"): 

    $name = $_POST['name'];
    $age = $_POST['age'];
    $email = $_POST['email'];

    // Kontrola, zda jméno obsahuje pouze písmena (včetně diakritiky)
    if (!preg_match("/^[a-zA-Zá-žÁ-Ž]+$/", $name)) {
        echo "<p>Jméno může obsahovat pouze písmena. Žádné číslice!</p>";
    }
    elseif (!ctype_digit($age)) {
        echo "<p>Prosím, zadejte platný věk (pouze číslice).</p>";
    } else {
        echo "<div class='response'>";
        echo "<h4><strong>Vaše jméno je {$name} a je vám {$age} let.</strong></h4>";
        echo "</div>";
    }
endif;

// Performing insert query execution
// here our table name is college
$sql = "INSERT INTO student (name, age, email) VALUES ('$name', '$age', '$email');";
        
if(mysqli_query($conn, $sql)){
    echo "<h3>Vaše indetita byla úspěšně zaevidována. Děkujeme! :D</h3>"; 

    echo nl2br("\n$name\n $age\n $email");
} else{
    echo "ERROR: Hush! Sorry $sql. " 
        . mysqli_error($conn);
}
        
// Close connection
mysqli_close($conn);
?>