schemas = {
    "registrations": {
        "type": "object",
        "properties": {
            "registrationId": {"type": "string"},
            "registrationURL": {"type": "string"}
        }
    },

    "groups": {
        "type": "object",
        "properties": {
            "brand": {"type": "string"},
            "groupId": {"type": "string"},
            "class": {"type": ["string", "null"]},
            "format": {"type": ["string", "null"]},
            "territory": {"type": ["string", "null"]},
            "duration": {"type": ["string", "null"]},
            "learningStartDate": {"type": ["string", "null"]},
            "learningFinishDate": {"type": ["string", "null"]},
            "groupLimit": {"type": "number"},
            "actualAgreementQuantity": {"type": "number"},
            "timeLesson": {"type": "string"},
            "timeWebinar": {"type": ["string", "null"]},
            "timeStudy": {"type": ["string", "null"]},
            "statuscode": {"type": "number"},
            "courseId": {"type": "string"},
            "courseName": {"type": ["string", "null"]},
            "discipline": {"type": "string"},
            "lessonDay": {"type": "string"},
            "webinarDay": {"type": ["string", "null"]},
            "studyDay": {"type": ["string", "null"]},
            "lmsId": {"type": ["string", "null"]}
        }
    }
}