db.Personaje.updateOne(
    { "_id": ObjectId("6530028a48b48ffdd9e8f1f0") }, 
    {
      $pull: {
        "inventario": { "_id": ObjectId("6530027f48b48ffdd9e8f196") } 
      }
    }
  )
  