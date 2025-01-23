<?php
// Define arrays for odd/even numbers and male/female names
$odd_numbers = [1, 3, 5, 7, 9];
$even_numbers = [2, 4, 6, 8, 10];
$male_names = ["Wade", "Zack", "Arthur", "Sullivan", "Gordon"];
$female_names = ["Lilliane", "Jessica", "Emily", "Beatrix", "Diane"];

// Merge the numbers and names arrays
$numbers = array_merge($odd_numbers, $even_numbers);
$names = array_merge($male_names, $female_names);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Čísla a Písmena</title>
    <link rel="stylesheet" href="array.css">
</head>
<body>
    <header>
        <h1>Arrays</h1>
    </header>

    <section class="content">
        <div class="container flex -justify-content -align-items">
            <div class="numbers">
                <h2>Čísla</h2>
                <?php
                foreach ($numbers as $item) {
                    echo "<span class='number'>$item</span>\n";
                }
                ?>
            </div>

            <div class="names">
                <h2>Jména</h2>
                <?php
                foreach ($names as $item) {
                    echo "<span class='name'>$item</span>\n";
                }
                ?>
            </div>
        </div>
    </section>

    <footer>
    </footer>
</body>
</html>