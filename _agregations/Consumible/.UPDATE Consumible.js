db.Consumible.updateOne(
  { "_id": ObjectId("6530027d48b48ffdd9e8f076") },
  {
    $set: {
      "tipo": "pocion",
      "nombre": "poderoso pocion",
      "peso": 0.57,
      "valor": 66,
      "descripcion": "Esta pocion fue conseguido tras derramar mucha sangre y es misterioso.",
      "efectos.0.Percepcion": 9,
      "efectos.1.Voluntad": 10,
      "efectos.2.Agilidad": 7,
      "duracion": 7
    }
  }
);
