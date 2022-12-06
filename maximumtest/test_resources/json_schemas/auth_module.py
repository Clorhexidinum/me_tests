schemas = {
    "auth/login": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "email": {"type": "string"},
            "name": {"type": "string"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"}
        }
    },

    "auth": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "email": {"type": "string"},
            "name": {"type": "string"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"}
        }
    },

    "auth/refresh": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "email": {"type": "string"},
            "name": {"type": "string"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"}
        }
    },

    "users": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "email": {"type": "string"},
            "name": {"type": "string"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"}
        }
    }
}
