<?php
// Povolení zobrazení chyb pro ladění
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Připojení k databázi
$conn = mysqli_connect("sql8.endora.cz:3313", "filmarsemoda", "DatabazeHeslo@", "filmkolekcesemoda");

// Kontrola připojení
if ($conn === false) {
    die("ERROR: Could not connect. " . mysqli_connect_error());
}

// Třída pro film
class Film {
    private $id;
    private $nazev;
    private $reziser;
    private $rok_vydani;
    private $zanr;

    public function __construct($nazev, $reziser, $rok_vydani, $zanr, $id = null) {
        $this->nazev = $nazev;
        $this->reziser = $reziser;
        $this->rok_vydani = $rok_vydani;
        $this->zanr = $zanr;
        $this->id = $id;
    }

    public function saveToDatabase($conn) {
        if ($this->id) {
            $stmt = $conn->prepare("UPDATE filmy SET nazev = ?, reziser = ?, rok_vydani = ?, zanr = ? WHERE id = ?");
            $stmt->bind_param("ssisi", $this->nazev, $this->reziser, $this->rok_vydani, $this->zanr, $this->id);
        } else {
            $stmt = $conn->prepare("INSERT INTO filmy (nazev, reziser, rok_vydani, zanr) VALUES (?, ?, ?, ?)");
            $stmt->bind_param("ssis", $this->nazev, $this->reziser, $this->rok_vydani, $this->zanr);
        }
        return $stmt->execute();
    }

    public static function getById($conn, $id) {
        $stmt = $conn->prepare("SELECT * FROM filmy WHERE id = ?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        $filmData = $result->fetch_assoc();

        if ($filmData) {
            return new Film($filmData['nazev'], $filmData['reziser'], $filmData['rok_vydani'], $filmData['zanr'], $filmData['id']);
        }
        return null;
    }

    public static function getAllFilms($conn) {
        $sql = "SELECT * FROM filmy";
        $result = $conn->query($sql);
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getId() { return $this->id; }
    public function getNazev() { return $this->nazev; }
    public function setNazev($nazev) { $this->nazev = $nazev; }
    public function getReziser() { return $this->reziser; }
    public function setReziser($reziser) { $this->reziser = $reziser; }
    public function getRokVydani() { return $this->rok_vydani; }
    public function setRokVydani($rok_vydani) { $this->rok_vydani = $rok_vydani; }
    public function getZanr() { return $this->zanr; }
    public function setZanr($zanr) { $this->zanr = $zanr; }
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['nazev'])) {
    $nazev = $_POST['nazev'];
    $reziser = $_POST['reziser'];
    $rok_vydani = $_POST['rok_vydani'];
    $zanr = $_POST['zanr'];

    if (isset($_POST['film_id']) && !empty($_POST['film_id'])) {
        $film = Film::getById($conn, $_POST['film_id']);
        if ($film) {
            $film->setNazev($nazev);
            $film->setReziser($reziser);
            $film->setRokVydani($rok_vydani);
            $film->setZanr($zanr);
            $film->saveToDatabase($conn);
            echo "Film byl úspěšně upraven.";
        }
    } else {
        $novyFilm = new Film($nazev, $reziser, $rok_vydani, $zanr);
        $novyFilm->saveToDatabase($conn);
        echo "Film byl přidán do kolekce.";
    }
}

$film = null;
if (isset($_GET['edit_id'])) {
    $filmId = $_GET['edit_id'];
    $film = Film::getById($conn, $filmId);
}

$filmy = Film::getAllFilms($conn);
?>

<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Filmova Kolekce</title>
</head>
<body>
    <h1>Filmova Kolekce</h1>
    <h2>Seznam filmů</h2>
    <ul>
        <?php foreach ($filmy as $filmItem) { ?>
            <li>
                <?php echo htmlspecialchars($filmItem['nazev']) . " (" . htmlspecialchars($filmItem['rok_vydani']) . ") - " . htmlspecialchars($filmItem['reziser']) . " [" . htmlspecialchars($filmItem['zanr']) . "]"; ?>
                <a href="?edit_id=<?php echo $filmItem['id']; ?>">Upravit</a>
            </li>
        <?php } ?>
    </ul>
    
    <h2>Přidat / Upravit film</h2>
    <form method="POST">
        <input type="hidden" name="film_id" value="<?php echo $film ? $film->getId() : ''; ?>">
        <label for="nazev">Název filmu:</label><br>
        <input type="text" id="nazev" name="nazev" value="<?php echo $film ? htmlspecialchars($film->getNazev()) : ''; ?>" required><br><br>

        <label for="reziser">Režisér:</label><br>
        <input type="text" id="reziser" name="reziser" value="<?php echo $film ? htmlspecialchars($film->getReziser()) : ''; ?>" required><br><br>

        <label for="rok_vydani">Rok vydání:</label><br>
        <input type="number" id="rok_vydani" name="rok_vydani" value="<?php echo $film ? htmlspecialchars($film->getRokVydani()) : ''; ?>" required><br><br>

        <label for="zanr">Žánr:</label><br>
        <input type="text" id="zanr" name="zanr" value="<?php echo $film ? htmlspecialchars($film->getZanr()) : ''; ?>" required><br><br>

        <button type="submit"><?php echo $film ? "Upravit film" : "Přidat film"; ?></button>
    </form>
</body>
</html>