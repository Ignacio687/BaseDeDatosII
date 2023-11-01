db.Personaje.update(
    { _id: ObjectId("Personaje_id") },
    { $pull: { inventario: "objeto"} }
);
