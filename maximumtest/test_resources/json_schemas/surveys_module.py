schemas = {
    "surveys": {
        "type": "object",
        "properties": {
            "priorities": {"type": "number"},
            "questions": {"type": "array"},
            "groups": {"type": "array"}
        }
    },

    "diagnostics": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "results": {
                "type": "array",
                "items": {
                    "id": {"type": "string"},
                    "result": {"type": "string"},
                    "questionId": {"type": "string"}
                }
            },
            "diagnostikaCode": {"type": "string"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"}
        }
    }
}
