db.Personaje.aggregate([
  {
    $match: {
      _id: ObjectId("6530028a48b48ffdd9e8f1f0"),
    },
  },
  {
    $project: {
      habilidades: 1,
      "equipo.armas.habilidad": 1,
      "equipo.equipamiento.habilidad": 1,
    },
  },
  {
    $unwind: {
      path: "$habilidades",
      preserveNullAndEmptyArrays: true,
    },
  },
  {
    $unwind: {
      path: "$equipo.armas",
      preserveNullAndEmptyArrays: true,
    },
  },
  {
    $unwind: {
      path: "$equipo.armas.habilidad",
      preserveNullAndEmptyArrays: true,
    },
  },
  {
    $unwind: {
      path: "$equipo.equipamiento",
      preserveNullAndEmptyArrays: true,
    },
  },
  {
    $unwind: {
      path: "$equipo.equipamiento.habilidad",
      preserveNullAndEmptyArrays: true,
    },
  },
  {
    $group: {
      _id: null,
      habilidades_totales: {
        $addToSet: "$habilidades",
      },
      habilidades_armas: {
        $addToSet: "$equipo.armas.habilidad",
      },
      habilidad_equipo: {
        $addToSet:
          "$equipo.equipamiento.habilidad",
      },
    },
  },
  {
    $project: {
      _id: 0,
      habilidades_totales: {
        $concatArrays: [
          "$habilidades_totales",
          "$habilidades_armas",
          "$habilidad_equipo",
        ],
      },
    },
  },
]);