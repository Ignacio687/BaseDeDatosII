db.Personaje.aggregate([
  {
    $match: {
      _id: ObjectId("6530028a48b48ffdd9e8f1f1"),
    },
  },
  {
    $lookup: {
      from: "Mision",
      localField: "misiones._id",
      foreignField: "_id",
      as: "misiones",
    },
  },
  {
    $unwind: "$misiones",
  },
  {
    $project: {
      nombre: "$misiones.nombre",
      etapas: "$misiones.etapas",
    },
  },
]);