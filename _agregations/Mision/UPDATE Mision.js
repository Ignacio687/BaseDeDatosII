db.Mision.updateOne(
    { "_id": ObjectId("6530028148b48ffdd9e8f1be") },
    {
      $set: {
        "nombre": "La busqueda del artefacto perdido", 
        "recompensa_xp": 55, 
        "recompensa_oro": 188, 
        "etapas.0.nombre": "Rastrea las pistas del ladron maestro" 
      }
    }
  );