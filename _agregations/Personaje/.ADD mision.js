db.Personaje.updateOne(
    { "_id": ObjectId("Personaje_id") },
    { $push: { mision: "mision_id"} }
);