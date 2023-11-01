db.Personaje.updateOne(
    { "_id": ObjectId("6530028a48b48ffdd9e8f1f0") }, 
    {
      $push: {
        "misiones": {
          "_id": ObjectId("6530028148b48ffdd9e8f1be"), 
          "collection": { "$ref": "Mision" }, 
        }
      }
    }
  )
  