<?php
// Zkontrolujeme, zda byl formulář odeslán
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Přiřadíme odeslané hodnoty do proměnných a ošetříme je
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $address = htmlspecialchars($_POST['address']);
    $phone = htmlspecialchars($_POST['phone']);
    $age = htmlspecialchars($_POST['age']);
    $gender = htmlspecialchars($_POST['gender']);
    $birthdate = htmlspecialchars($_POST['birthdate']);
    $note = htmlspecialchars($_POST['note']);
}
?>

<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minimalistický formulář</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap:wrap;
            height: 100vh;
            color: #333;
        }

        .form-container {
            background-color: white;
            display: flex;
            justify-content:center;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            width: 400px;
            text-align: center;
        }

        h1 {
            color: #007BFF;
            font-size: 24px;
            margin-bottom: 20px;
        }

        label {
            font-size: 14px;
            font-weight: bold;
            color: #555;
            display: block;
            margin-bottom: 8px;
        }

        input[type="text"], input[type="email"], input[type="tel"], input[type="number"], input[type="date"], textarea, select {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
            background-color: #f9f9f9;
        }

        input[type="submit"] {
            width: 100%;
            padding: 12px;
            background-color: #007BFF;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }

        textarea {
            height: 120px;
        }

        hr {
            margin: 20px 0;
            border: 0;
            border-top: 1px solid #ddd;
        }

        .response {
            margin-top: 20px;
            padding: 20px;
            background-color: #f0f8ff;
            border-radius: 8px;
        }

        .response p {
            font-size: 14px;
            margin: 5px 0;
        }

        .response strong {
            color: #007BFF;
        }
        
        .text-container {
            height: 400px;
            padding: 200px 20px;
        }
        
    </style>
</head>
<body>

<div class="form-container">
    
    <!-- Formulář pro zadání údajů -->
    <form method="POST" action="">
        <label for="name">Jméno:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="address">Adresa:</label>
        <input type="text" id="address" name="address" required><br>

        <label for="phone">Telefon:</label>
        <input type="tel" id="phone" name="phone" required><br>

        <label for="age">Věk:</label>
        <input type="number" id="age" name="age" required><br>

        <label for="gender">Pohlaví:</label>
        <select id="gender" name="gender" required>
            <option value="male">Muž</option>
            <option value="female">Žena</option>
            <option value="other">Jiné</option>
        </select><br>

        <label for="birthdate">Datum narození:</label>
        <input type="date" id="birthdate" name="birthdate" required><br>

        <label for="note">Poznámka:</label>
        <textarea id="note" name="note" rows="4" cols="50"></textarea><br>

        <input type="submit" value="Odeslat">
    </form>

    <!-- Zobrazení odeslaných údajů -->
    <?php if ($_SERVER["REQUEST_METHOD"] == "POST"): ?>
        <hr>
        <div class="response">
            <h2>Vaše údaje:</h2>
            <p><strong>Jméno:</strong> <?= $name ?></p>
            <p><strong>E-mail:</strong> <?= $email ?></p>
            <p><strong>Adresa:</strong> <?= $address ?></p>
            <p><strong>Telefon:</strong> <?= $phone ?></p>
            <p><strong>Věk:</strong> <?= $age ?></p>
            <p><strong>Pohlaví:</strong> <?= ($gender == 'male' ? 'Muž' : ($gender == 'female' ? 'Žena' : 'Jiné')) ?></p>
            <p><strong>Datum narození:</strong> <?= $birthdate ?></p>
            <p><strong>Poznámka:</strong> <?= $note ?></p>
        </div>
    <?php endif; ?>
</div>

<div class="text-container">
    <h1>Co je to POST a GET?</h1>
    <p>
        Metody POST a GET slouží k odesílání dat mezi klientem (např. webovým prohlížečem) a serverem. GET posílá data v URL, což znamená, že jsou viditelná v adresním řádku prohlížeče a jsou omezená na 2048 znaků. Je vhodná pro požadavky, které neovlivňují stav serveru, např. vyhledávání nebo filtrování dat. POST odesílá data v těle HTTP požadavku, což je bezpečnější pro citlivé informace a neomezené množství dat. Používá se při odesílání formulářů, registracích nebo změnách na serveru (např. přidání nového záznamu). GET je rychlejší a jednodušší, ale POST je bezpečnější a vhodnější pro větší nebo citlivější data. 
    </p>
</div>

</body>
</html>