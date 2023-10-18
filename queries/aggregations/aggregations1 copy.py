def getAllEmbeddedObjects(jsonObj):
    def recursiveFinder(jsonObj):
        if isinstance(jsonObj.values(), list):
            for element in value:
                keyRecList = recursiveFinder(value)
                if keyRecList:
                    keyRecList.insert(0, element)
                    return keyRecList
        else:
            for key, value in jsonObj.items():
                if isinstance(value, dict):
                    keyRecList = recursiveFinder(value)
                    if keyRecList:
                        keyRecList.insert(0, key)
                        return keyRecList
                elif key == '$oid':
                    return [1]

    if jsonObj:
        keyValues = []
        for key, value in jsonObj.items():
            if isinstance(value, (dict)):
                keyRecList = recursiveFinder(value)
                if keyRecList:
                    keyValues.append(keyRecList)
            elif isinstance(value, (list)):
                for element in value:
                    keyRecList = recursiveFinder(element)
                    if keyRecList:
                        keyValues.append(keyRecList)
        print(keyValues)

if __name__ == "__main__":
    getAllEmbeddedObjects(
        {
  "_id": {
    "$oid": "652ed7e8fa9783ea7729bd81"
  },
  "nombre": "MechanicalMaster18",
  "nivel": 52,
  "oro": 200,
  "puntos_vida": 220,
  "puntos_accion": 2,
  "atributos": {
    "fuerza": 15,
    "pericia": 56,
    "inteligencia": 99,
    "constitucion": 60,
    "memoria": 60,
    "ingenio": 47,
    "armadura_fisica": 131,
    "armadura_magica": 167,
    "movimiento": 31,
    "iniciativa": 18,
    "res-fuego": 47,
    "res-agua": 81,
    "res-tierra": 25,
    "res-aire": 70,
    "res-veneno": 77
  },
  "aptitudes": {
    "aeroteurgo": 8,
    "canalla": 16,
    "cazador": 10,
    "contienda": 4,
    "geomante": 16,
    "hidrosofista": 12,
    "invocacion": 9,
    "necromante": 4,
    "piroquinectico": 17,
    "polimorfismo": 14
  },
  "habilidades": [
    {
      "_id": {
        "$oid": "652ed7ce239729f90829bbe4"
      },
      "collection": {
        "$ref": "Habilidad"
      }
    }
  ],
  "equipo": {
    "armas": [
      {
        "nombre": "Cetro de mago supremo",
        "arma": "Vara",
        "tipo": "Arma Mágica",
        "dano-min": 19,
        "dano-max": 97,
        "critico": 306,
        "puntos_de_accion": 2,
        "nivel": 40,
        "peso": 15.16,
        "valor": 3323,
        "rareza": "Épica",
        "alcance": 2.1,
        "efectos": [
          {
            "fuerza": 2
          },
          {
            "pericia": 1
          },
          {
            "inteligencia": 3
          },
          {
            "constitución": 1
          },
          {
            "memoria": 2
          },
          {
            "ingenio": 1
          }
        ],
        "requerimiento": [
          {
            "inteligencia": 19
          }
        ],
        "habilidad": [
          {
            "_id": {
              "$oid": "652ed7ce239729f90829bbe4"
            },
            "collection": {
              "$ref": "Habilidad"
            }
          },
          {
            "_id": {
              "$oid": "652ed7ce239729f90829bbe5"
            },
            "collection": {
              "$ref": "Habilidad"
            }
          }
        ],
        "descripcion": "Un aura mágica rodea esta arma cuando se desenvaina."
      }
    ],
    "equipamiento": [
      {
        "nombre": "Botas del Viajero",
        "tipo": "Botas",
        "nivel": 8,
        "peso": 0.98,
        "valor": 21158,
        "rareza": "Legendaria",
        "armadura fisica": 86,
        "armadura_magica": 4,
        "descripcion": "Las botas del viajero son ideales para largos recorridos a pie. Son resistentes, cómodas y permiten al portador caminar largas distancias sin fatigarse.",
        "efectos": [
          {
            "fuerza": 2
          },
          {
            "pericia": 3
          },
          {
            "inteligencia": 1
          },
          {
            "constitución": 3
          },
          {
            "memoria": 1
          },
          {
            "ingenio": 1
          }
        ],
        "requerimiento": [
          {
            "memoria": 7
          }
        ],
        "habilidad": [
          {
            "_id": {
              "$oid": "652ed7ce239729f90829bbe4"
            },
            "collection": {
              "$ref": "Habilidad"
            }
          },
          {
            "_id": {
              "$oid": "652ed7ce239729f90829bbe5"
            },
            "collection": {
              "$ref": "Habilidad"
            }
          }
        ]
      },
      {
        "nombre": "Guantes de los Vientos",
        "tipo": "Guantes",
        "nivel": 30,
        "peso": 7.68,
        "valor": 34325,
        "rareza": "Común",
        "armadura fisica": 87,
        "armadura_magica": 91,
        "descripcion": "Estos guantes permiten al portador controlar los vientos y volar brevemente. Ideales para la exploración aérea.",
        "efectos": [
          {
            "fuerza": 1
          },
          {
            "pericia": 2
          },
          {
            "inteligencia": 2
          },
          {
            "constitución": 3
          },
          {
            "memoria": 1
          },
          {
            "ingenio": 3
          }
        ],
        "requerimiento": [
          {
            "memoria": 9
          }
        ],
        "habilidad": [
          {
            "_id": {
              "$oid": "652ed7ce239729f90829bbe4"
            },
            "collection": {
              "$ref": "Habilidad"
            }
          },
          {
            "_id": {
              "$oid": "652ed7ce239729f90829bbe5"
            },
            "collection": {
              "$ref": "Habilidad"
            }
          }
        ]
      }
    ]
  },
  "inventario": [
    {
      "_id": {
        "$oid": "652ed7cf239729f90829bc7b"
      },
      "collection": {
        "$ref": "Consumible"
      },
      "cantidad": 20
    },
    {
      "nombre": "Espada larga",
      "arma": "Espada",
      "tipo": "A una mano",
      "dano-min": 37,
      "dano-max": 122,
      "critico": 335,
      "puntos_de_accion": 4,
      "nivel": 10,
      "peso": 14.62,
      "valor": 4461,
      "rareza": "Poco común",
      "alcance": 4.6,
      "efectos": [
        {
          "fuerza": 2
        },
        {
          "pericia": 1
        },
        {
          "inteligencia": 2
        },
        {
          "constitución": 3
        },
        {
          "memoria": 2
        },
        {
          "ingenio": 3
        }
      ],
      "requerimiento": [
        {
          "fuerza": 2
        }
      ],
      "habilidad": [
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe4"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        },
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe5"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        },
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe6"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        }
      ],
      "descripcion": "Esta arma brilla intensamente en la oscuridad."
    },
    {
      "nombre": "Yelmo del Caballero Valiente",
      "tipo": "Casco",
      "nivel": 39,
      "peso": 1.39,
      "valor": 33976,
      "rareza": "Mítica",
      "armadura fisica": 87,
      "armadura_magica": 42,
      "descripcion": "El yelmo del caballero valiente es conocido por su diseño elegante y resistencia. Fue usado por un héroe legendario en muchas batallas.",
      "efectos": [
        {
          "fuerza": 1
        },
        {
          "pericia": 1
        },
        {
          "inteligencia": 1
        },
        {
          "constitución": 1
        },
        {
          "memoria": 1
        },
        {
          "ingenio": 1
        }
      ],
      "requerimiento": [
        {
          "memoria": 14
        }
      ],
      "habilidad": [
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe4"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        },
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe5"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        },
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe6"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        }
      ]
    },
    {
      "nombre": "Anillo de la Armonía",
      "tipo": "Anillo",
      "nivel": 15,
      "peso": 13.35,
      "valor": 18254,
      "rareza": "Épica",
      "armadura fisica": 56,
      "armadura_magica": 43,
      "descripcion": "Este anillo otorga paz y armonía a su portador. Las emociones y el estrés desaparecen.",
      "efectos": [
        {
          "fuerza": 2
        },
        {
          "pericia": 1
        },
        {
          "inteligencia": 3
        },
        {
          "constitución": 1
        },
        {
          "memoria": 1
        },
        {
          "ingenio": 1
        }
      ],
      "requerimiento": [
        {
          "ingenio": 11
        }
      ],
      "habilidad": [
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe4"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        }
      ]
    },
    {
      "_id": {
        "$oid": "652ed7cf239729f90829bc6f"
      },
      "collection": {
        "$ref": "Consumible"
      },
      "cantidad": 2
    },
    {
      "nombre": "Lanza de fuego",
      "arma": "Lanza",
      "tipo": "Arma Mágica",
      "dano-min": 23,
      "dano-max": 86,
      "critico": 242,
      "puntos_de_accion": 4,
      "nivel": 1,
      "peso": 11.74,
      "valor": 30284,
      "rareza": "Mítica",
      "alcance": 3.3,
      "efectos": [
        {
          "fuerza": 1
        },
        {
          "pericia": 3
        },
        {
          "inteligencia": 2
        },
        {
          "constitución": 1
        },
        {
          "memoria": 3
        },
        {
          "ingenio": 3
        }
      ],
      "requerimiento": [
        {
          "inteligencia": 2
        }
      ],
      "habilidad": [
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe4"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        }
      ],
      "descripcion": "El ronroneo de un gato se puede escuchar cuando esta arma está desenvainada."
    },
    {
      "nombre": "Vara ancestral",
      "arma": "Vara",
      "tipo": "Arma Mágica",
      "dano-min": 27,
      "dano-max": 89,
      "critico": 227,
      "puntos_de_accion": 5,
      "nivel": 43,
      "peso": 6.34,
      "valor": 30790,
      "rareza": "Legendaria",
      "alcance": 0.4,
      "efectos": [
        {
          "fuerza": 3
        },
        {
          "pericia": 3
        },
        {
          "inteligencia": 3
        },
        {
          "constitución": 2
        },
        {
          "memoria": 3
        },
        {
          "ingenio": 2
        }
      ],
      "requerimiento": [
        {
          "constitución": 8
        }
      ],
      "habilidad": [
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe4"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        },
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe5"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        },
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe6"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        }
      ],
      "descripcion": "El sonido metálico de esta arma al chocar contra otra es armonioso."
    },
    {
      "nombre": "Lanza",
      "arma": "Lanza",
      "tipo": "A dos manos",
      "dano-min": 5,
      "dano-max": 69,
      "critico": 226,
      "puntos_de_accion": 6,
      "nivel": 24,
      "peso": 7.37,
      "valor": 20210,
      "rareza": "Inusual",
      "alcance": 5.7,
      "efectos": [
        {
          "fuerza": 2
        },
        {
          "pericia": 2
        },
        {
          "inteligencia": 1
        },
        {
          "constitución": 1
        },
        {
          "memoria": 2
        },
        {
          "ingenio": 3
        }
      ],
      "requerimiento": [
        {
          "inteligencia": 10
        }
      ],
      "habilidad": [
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe4"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        },
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe5"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        },
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe6"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        }
      ],
      "descripcion": "Esta arma destella intensamente en la luz."
    },
    {
      "_id": {
        "$oid": "652ed7cf239729f90829bc9f"
      },
      "collection": {
        "$ref": "Consumible"
      },
      "cantidad": 6
    },
    {
      "_id": {
        "$oid": "652ed7cf239729f90829bc37"
      },
      "collection": {
        "$ref": "Consumible"
      },
      "cantidad": 20
    },
    {
      "nombre": "Yelmo del Sabio Magus",
      "tipo": "Casco",
      "nivel": 23,
      "peso": 4.39,
      "valor": 20737,
      "rareza": "Épica",
      "armadura fisica": 4,
      "armadura_magica": 25,
      "descripcion": "Este yelmo está adornado con runas mágicas. Otorga un mayor control sobre la magia y el conocimiento arcano.",
      "efectos": [
        {
          "fuerza": 2
        },
        {
          "pericia": 1
        },
        {
          "inteligencia": 2
        },
        {
          "constitución": 3
        },
        {
          "memoria": 1
        },
        {
          "ingenio": 2
        }
      ],
      "requerimiento": [
        {
          "constitución": 6
        }
      ],
      "habilidad": [
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe4"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        }
      ]
    },
    {
      "_id": {
        "$oid": "652ed7cf239729f90829bd25"
      },
      "collection": {
        "$ref": "Consumible"
      },
      "cantidad": 14
    },
    {
      "nombre": "Arco del bosque encantado",
      "arma": "Arco",
      "tipo": "Arma Mágica",
      "dano-min": 6,
      "dano-max": 74,
      "critico": 291,
      "puntos_de_accion": 6,
      "nivel": 4,
      "peso": 6.67,
      "valor": 12966,
      "rareza": "Poco común",
      "alcance": 5.4,
      "efectos": [
        {
          "fuerza": 1
        },
        {
          "pericia": 3
        },
        {
          "inteligencia": 1
        },
        {
          "constitución": 2
        },
        {
          "memoria": 2
        },
        {
          "ingenio": 1
        }
      ],
      "requerimiento": [
        {
          "constitución": 14
        }
      ],
      "habilidad": [
        {
          "_id": {
            "$oid": "652ed7ce239729f90829bbe4"
          },
          "collection": {
            "$ref": "Habilidad"
          }
        }
      ],
      "descripcion": "Esta arma tiene un tono dorado que la hace parecer divina."
    }
  ],
  "misiones": [
    {
      "_id": {
        "$oid": "652ed7d1239729f90829bd26"
      },
      "collection": {
        "$ref": "Mision"
      }
    },
    {
      "_id": {
        "$oid": "652ed7d1239729f90829bd27"
      },
      "collection": {
        "$ref": "Mision"
      }
    },
    {
      "_id": {
        "$oid": "652ed7d1239729f90829bd28"
      },
      "collection": {
        "$ref": "Mision"
      }
    },
    {
      "_id": {
        "$oid": "652ed7d1239729f90829bd29"
      },
      "collection": {
        "$ref": "Mision"
      }
    },
    {
      "_id": {
        "$oid": "652ed7d1239729f90829bd2a"
      },
      "collection": {
        "$ref": "Mision"
      }
    },
    {
      "_id": {
        "$oid": "652ed7d1239729f90829bd2b"
      },
      "collection": {
        "$ref": "Mision"
      }
    },
    {
      "_id": {
        "$oid": "652ed7d1239729f90829bd2c"
      },
      "collection": {
        "$ref": "Mision"
      }
    },
    {
      "_id": {
        "$oid": "652ed7d1239729f90829bd2d"
      },
      "collection": {
        "$ref": "Mision"
      }
    },
    {
      "_id": {
        "$oid": "652ed7d1239729f90829bd2e"
      },
      "collection": {
        "$ref": "Mision"
      }
    }
  ]
}
    )