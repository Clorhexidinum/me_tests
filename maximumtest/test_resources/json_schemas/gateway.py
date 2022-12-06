schemas = {
    "health": {
        "type": "object",
        "properties": {
            "statusCode": {"type": "number"},
            "response": {
                "type": "object",
                "properties": {
                    "database": {
                        "type": "object",
                        "properties": {
                            "status": {"type": "string"}
                        }
                    },
                    "memory_heap": {
                        "type": "object",
                        "properties": {
                            "status": {"type": "string"}
                        }
                    },
                    "crm_microservice": {
                        "type": "object",
                        "properties": {
                            "status": {"type": "string"}
                        }
                    },
                    "payment_microservice": {
                        "type": "object",
                        "properties": {
                            "status": {"type": "string"}
                        }
                    },
                    "survey_microservice": {
                        "type": "object",
                        "properties": {
                            "status": {"type": "string"}
                        }
                    },
                    "content_microservice": {
                        "type": "object",
                        "properties": {
                            "status": {"type": "string"}
                        }
                    },
                    "payapp_microservice": {
                        "type": "object",
                        "properties": {
                            "status": {"type": "string"}
                        }
                    },
                    "auth_microservice": {
                        "type": "object",
                        "properties": {
                            "status": {"type": "string"}
                        }
                    }
                }
            },
            "timestamp": {"type": "string"},
            "path": {"type": "string"}
        }
    },

    "email/vacancy": {
        "type": "object",
        "properties": {
            "accepted": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "rejected": {"type": "array"},
            "envelopeTime": {"type": "number"},
            "messageTime": {"type": "number"},
            "messageSize": {"type": "number"},
            "response": {"type": "string"},
            "envelope": {
                "type": "object",
                "properties": {
                    "from": {"type": "string"},
                    "to": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        }
                    }
                }
            },
            "messageId": {"type": "string"}
        }
    },

    "post_registrations": {
        "type": "object",
        "properties": {
            "registrationId": {"type": "string"}
        }
    },

    "get_registrations": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "referer": {"type": ["string", "null"]},
            "country": {"type": "string"},
            "firstName": {"type": ["string", "null"]},
            "lastName": {"type": ["string", "null"]},
            "email": {"type": ["string", "null"]},
            "phone": {"type": ["string", "null"]},
            "parentName": {"type": ["string", "null"]},
            "parentEmail": {"type": ["string", "null"]},
            "parentPhone": {"type": ["string", "null"]},
            "city": {"type": ["string", "null"]},
            "companyId": {"type": "string"},
            "eventCode": {"type": ["string", "null"]},
            "place": {"type": ["string", "null"]},
            "school": {"type": ["string", "null"]},
            "grade": {"type": ["string", "null"]},
            "issueYear": {"type": "string"},
            "additionalInfo": {"type": ["string", "null"]},
            "gaCid": {"type": ["string", "null"]},
            "product": {"type": ["string", "null"]},
            "utm": {
                "type": ["object", "null"],
                "properties": {
                    "utm_medium": {"type": "string"},
                    "utm_source": {"type": "string"},
                    "utm_campaign": {"type": "string"}
                }
            },
            "examType": {"type": ["string", "null"]},
            "month": {"type": ["string", "null"]},
            "crmRegistrationId": {"type": ["string", "null"]},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"}
        }
    },
}
