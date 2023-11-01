[
  {
    $match: {
      _id: ObjectId("6530028a48b48ffdd9e8f1f0"),
    },
  },
  {
    $lookup: {
      from: "Consumible",
      localField: "inventario._id",
      foreignField: "_id",
      as: "consumibleData",
    },
  },
  {
    $lookup: {
      from: "Objeto_Clave",
      localField: "inventario._id",
      foreignField: "_id",
      as: "objetoClaveData",
    },
  },
  {
    $project: {
      _id: 0,
      inventario: {
        $concatArrays: ["$consumibleData", "$objetoClaveData"],
      },
    },
  },
]