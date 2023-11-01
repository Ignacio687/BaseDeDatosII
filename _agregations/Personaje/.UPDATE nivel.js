db.Personaje.update(
    { _id: ObjectId("Personaje_id") },
    { $inc: { 
        nivel
        : "valor"} }
);