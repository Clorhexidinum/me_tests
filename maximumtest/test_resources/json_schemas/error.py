schema = {
    "response": {
        "type": "object",
        "properties": {
            "statusCode": {"type": "number"},
            "response": {
                "type": ["string", "array"],
                "items": {
                    "type": "string"
                }
            },
            "timestamp": {"type": "string"},
            "path": {"type": "string"}
        }
    }
}

