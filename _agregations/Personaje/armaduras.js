db.Personaje.aggregate([
    {
      $match: {
        _id: ObjectId("6530028a48b48ffdd9e8f1f2"),
      },
    },
    {
      $unwind: "$equipo.equipamiento",
    },
    
    {
      $lookup: {
        from: "Habilidad",
        localField:
          "equipo.equipamiento.habilidad._id",
        foreignField: "_id",
        as: "equipo.equipamiento.habilidad",
      },
    },
    {
      $project: {
        equipo_f: "$equipo.equipamiento",
        habilidad:
          "$equipo.equipamiento.habilidad.nombre",
      },
    },
  ])  