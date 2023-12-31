db.Personaje.aggregate([
  {
    $match: {
      _id: ObjectId("6530028a48b48ffdd9e8f1f1"),
    },
  },
  {
    $lookup: {
      from: "Habilidad",
      localField: "equipo.armas.habilidad._id",
      foreignField: "_id",
      as: "habilidades",
    },
  },
  {
    $project: {
      arma: "$equipo.armas",
      habilidad: "$habilidades.nombre",
    },
  },
])