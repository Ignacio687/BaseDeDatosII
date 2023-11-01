db.Personaje.update(
    { _id: ObjectId("Personaje_id") },
    { $push: { inventario: "objeto"} }
);