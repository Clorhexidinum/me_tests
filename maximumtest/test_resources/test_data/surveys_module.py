class SurveysModule:
    @staticmethod
    def get_data():
        data = {
            "surveys": {
                "url": "surveys"
            },

            "surveys/generate-url": {
                "url": "surveys/generate-url",
                "request": {
                    "surveyId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "surveyFor": "None",
                    "surveyForEntityId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
                }
            },

            "surveys/id": {
                "url": "surveys",
                "request": {
                    "results": [
                        {
                            "id": None,
                            "questionId": "e31e9d38-8ac0-ec11-983f-000d3ab1b404",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "579bc092-75da-ec11-bb3d-000d3ab7912d",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "43503806-7dda-ec11-bb3d-000d3ab7912d",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "289b2f7d-eee0-ec11-bb3c-000d3ade4682",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "2187779d-eee0-ec11-bb3c-000d3ade4682",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "8cc6eba3-eee0-ec11-bb3c-000d3ade4682",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "9cc6eba3-eee0-ec11-bb3c-000d3ade4682",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "f1129d7d-432b-ec11-b6e5-000d3ade7cac",
                            "result": "true"
                        },
                        {
                            "id": None,
                            "questionId": "097a3a53-65b6-ec11-983f-000d3a66c4b5",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "3a4e9339-47ba-ec11-983f-000d3a66fec2",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "93e07d2e-48ba-ec11-983f-000d3a66fec2",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "fcb4c0ac-62a4-ec11-983f-000d3adf996e",
                            "result": None
                        },
                        {
                            "id": None,
                            "questionId": "c2b2dfd8-62a4-ec11-983f-000d3adf996e",
                            "result": None
                        }
                    ]
                }
            },

            "diagnostics": {
                "url": "diagnostics",
                "request": {
                    "survey": {
                        "results": [
                            {
                                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                                "questionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                                "result": "string"
                            }
                        ]
                    },
                    "diagnostika": {
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
                }
            }
        }

        return data
