db.Personaje.aggregate([
    {
      $match: {
        _id: ObjectId("6530028a48b48ffdd9e8f1f1")
      }
    },
    {
      $set: {
        nombre: "new_username"
      }
    }
])