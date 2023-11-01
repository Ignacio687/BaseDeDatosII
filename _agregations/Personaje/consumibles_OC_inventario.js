db.Personaje.aggregate([
  {
    $match: {
      _id: ObjectId("6530028a48b48ffdd9e8f1f0"),
    },
  },
  {
    $unwind: "$inventario",
  },
  {
    $project: {
      _id: "$inventario._id",
      objeto: {
        $cond: {
          if: {
            $eq: [
              {
                $ifNull: [
                  "$inventario.nombre",
                  null,
                ],
              },
              null,
            ],
          },
          then: "$REMOVE",
          else: "$inventario",
        },
      },
    },
  },
  {
    $lookup: {
      from: "Consumible",
      localField: "_id",
      foreignField: "_id",
      as: "consumibleData",
    },
  },
  {
    $lookup: {
      from: "Objeto_Clave",
      localField: "_id",
      foreignField: "_id",
      as: "objetoClaveData",
    },
  },
  {
    $unwind: {
      path: "$consumibleData",
      preserveNullAndEmptyArrays: true,
    },
  },
  {
    $unwind: {
      path: "$objetoClaveData",
      preserveNullAndEmptyArrays: true,
    },
  },
]);