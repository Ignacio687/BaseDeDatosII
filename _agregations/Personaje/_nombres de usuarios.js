db.Personaje.aggregate([
  {
    $project: {
      _id: 0,
      nombre: "$nombre",
    },
  },
])