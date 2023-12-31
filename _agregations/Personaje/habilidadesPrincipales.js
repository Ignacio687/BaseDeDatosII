db.Personaje.aggregate([
    {
      $match: {
        _id: ObjectId("6530028a48b48ffdd9e8f1f1"),
      },
    },
    {
      $unwind: "$habilidades",
    },
    {
      $lookup: {
        from: "Habilidad",
        localField: "habilidades._id",
        foreignField: "_id",
        as: "habilidades_info",
      },
    },
    {
      $project: {
        _id: 0,
        nombre_habilidad: {
          $arrayElemAt: [
            "$habilidades_info.nombre_habilidad",
            0,
          ],
        },
        detalle: {
          $arrayElemAt: [
            "$habilidades_info.detalle",
            0,
          ],
        },
        efecto: {
          $arrayElemAt: [
            "$habilidades_info.efecto",
            0,
          ],
        },
        requerimientos: {
          $arrayElemAt: [
            "$habilidades_info.requerimiento",
            0,
          ],
        },
      },
    },
  ]);