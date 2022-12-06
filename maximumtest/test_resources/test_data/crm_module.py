class CrmModuleData:
    @staticmethod
    def get_data():
        data = {
            "registrations": {
                "url": "crm/registrations",
                "request": {
                    "firstParent": {
                        "email": "user@example.com",
                        "phone": "+7 999 999 99 99",
                        "firstName": "Удали если видишь это",
                        "lastname": "Удали если видишь это",
                        "middleName": "Удали если видишь это",
                        "contactId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "contactType": 0,
                        "acAccountCreated": True,
                        "territoryId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "regionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "issueYear": 2099
                    },
                    "schoolchild": {
                        "email": "user@example.com",
                        "phone": "+7 999 999 99 99",
                        "firstName": "Удали если видишь это",
                        "lastname": "Удали если видишь это",
                        "middleName": "Удали если видишь это",
                        "contactId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "contactType": 0,
                        "acAccountCreated": True,
                        "territoryId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "regionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "issueYear": 2099
                    },
                    "campaignCode": "string",
                    "eventCode": "string",
                    "city": "string",
                    "issueYear": 2099,
                    "additionalInfo": "string",
                    "gaCid": "string",
                    "utm": "string",
                    "utMcontent": "string",
                    "utMterm": "string",
                    "utmSource": "string",
                    "utmMedium": "string",
                    "utmCampaign": "string",
                    "hotLead": 0,
                    "transactionCode": "string",
                    "promocodeId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "registrationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "webformId": "string",
                    "products": [
                        {
                            "groupId": "31a16e5b-49a1-ec11-b400-000d3ab75e5b",
                            "paymentType": "StepByStep",
                            "agreementFormat": "print",
                            "isLadderApplied": True,
                            "discounts": [
                                "3fa85f64-5717-4562-b3fc-2c963f66afa6"
                            ]
                        }
                    ]
                }
            },

            "proftest": {
                "url": "crm/registrations/proftest",
                "request": {
                    "time": "string",
                    "studentPhone": "+7 999 999 99 99",
                    "studentEmail": "user@example.com",
                    "parentPhone": "+7 999 999 99 99",
                    "parentEmail": "user@example.com",
                    "type": "string",
                    "link": "https://example.com",
                    "subject": "string",
                    "resultPercent": "string",
                    "score": "string",
                    "generalScore": "string",
                    "results": [
                        {
                            "first": "string",
                            "second": "string"
                        }
                    ]
                }
            },

            "groups": {
                "url": "crm/groups",
                "response": {
                    "type": "object",
                    "properties": {
                        "brand": {"type": "string"},
                        "groupId": {"type": "string"},
                        "class": {"type": ["string", "null"]},
                        "format": {"type": ["string", "null"]},
                        "territory": {"type": ["string", "null"]},
                        "duration": {"type": ["string", "null"]},
                        "learningStartDate": {"type": "string"},
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
        }

        return data
