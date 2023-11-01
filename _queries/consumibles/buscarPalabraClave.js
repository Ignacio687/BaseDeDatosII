db.Cosumible.find({
    $text: {$search: "pocion"}
})