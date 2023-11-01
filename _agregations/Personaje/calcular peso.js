db.Personaje.aggregate([
    {
      $match:
        /**
         * query: The query in MQL.
         */
        {
          _id: ObjectId("6530028a48b48ffdd9e8f1f9"),
        },
    },
    {
      $project:
        /**
         * specifications: The fields to
         *   include or exclude.
         */
        {
          oro: 1,
          "equipo.armas.peso": 1,
          "equipo.equipamiento.peso": 1,
          inventario: 1,
        },
    },
    // {
    //   $unwind: "$inventario",
    // }
    {
      $lookup: {
        from: "Consumible",
        localField: "inventario._id",
        foreignField: "_id",
        as: "consumible",
      },
    },
    {
      $lookup: {
        from: "Objeto_Clave",
        localField: "inventario._id",
        foreignField: "_id",
        as: "objeto",
      },
    },
    // {
    //   $set: {
    //     consumible: {
    //       $cond: {
    //         if: {
    //           $gte: [
    //             "$inventario._id",
    //             "$consumible._id",
    //           ],
    //         },
    //         then: {
    //           $multiply: [
    //             "$consumible.peso",
    //             "$inventario.cantidad",
    //           ],
    //         },
    //         else: null,
    //       },
    //     },
    //   },
    // }
    {
      $group: {
        _id: null,
        peso: {
          $sum: {
            $add: [
              "$oro",
              {
                $sum: "$equipo.armas.peso",
              },
              {
                $sum: "$equipo.equipamiento.peso",
              },
              {
                $sum: "$inventario.peso",
              },
              {
                $sum: "$consumible.peso",
              },
              {
                $sum: "$objeto.peso",
              },
            ],
          },
        },
      },
    },
  ]);