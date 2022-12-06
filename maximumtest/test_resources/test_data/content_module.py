from maximumtest import utils as path


class ContentModuleData:

    @staticmethod
    def get_data():
        data = {
            "banners": {
                "url": "content/banners",
                "request": {
                    "active": True,
                    "backgroundColor": "Удали если видишь это",
                    "backgroundImage": "Удали если видишь это",
                    "image": "Удали если видишь это",
                    "title": "Удали если видишь это",
                    "text": "Удали если видишь это",
                    "category": [
                        "Удали если видишь это",
                        "Удали если видишь это"
                    ],
                    "city": [
                        "Удали если видишь это",
                        "Удали если видишь это"
                    ],
                    "firstButton": {
                        "text": "Удали если видишь это",
                        "crmId": "Удали если видишь это",
                        "actionLink": True,
                        "link": "https://example.com"
                    },
                    "secondButton": {
                        "text": "Удали если видишь это",
                        "crmId": "Удали если видишь это",
                        "actionLink": True,
                        "link": "https://example.com",
                        "active": True
                    },
                    "bannerPosition": "middle"
                }
            },

            "header": {
                "url": "content/header",
                "request": {
                    "crmId": "Удали если видишь это",
                    "actionLink": True,
                    "link": "https://example.com",
                    "text": "Удали если видишь это",
                    "outline": True,
                    "categoryTemplates": [
                        {
                            "bannerTemplates": {
                                "actionLink": True,
                                "crmId": "Удали если видишь это",
                                "link": "https://example.com",
                                "backgroundColor": "Удали если видишь это",
                                "backgroundImage": "Удали если видишь это",
                                "text": "Удали если видишь это",
                                "title": "Удали если видишь это"
                            },
                            "name": "Удали если видишь это",
                            "priority": "1",
                            "promo": [
                                {
                                    "item": "Удали если видишь это",
                                    "link": "https://example.com"
                                }
                            ],
                            "visible": True,
                            "isClickable": True,
                            "bottomMenu": True,
                            "crmId": "Удали если видишь это",
                            "actionLink": True,
                            "link": "https://example.com",
                            "categoryColor": "Удали если видишь это",
                            "categoryImage": "Удали если видишь это",
                            "subcategories": [
                                {
                                    "title": "Удали если видишь это",
                                    "priority": "1",
                                    "isShowTitle": True,
                                    "isClickable": True,
                                    "crmId": "Удали если видишь это",
                                    "actionLink": True,
                                    "link": "https://example.com",
                                    "isFullType": True,
                                    "links": [
                                        {
                                            "linkText": "Удали если видишь это",
                                            "link": "https://example.com",
                                            "priority": "1",
                                            "isBold": True
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            },

            "header-banners": {
                "url": "content/header-banners",
                "request": {
                    "actionLink": True,
                    "link": "https://example.com",
                    "crmId": "Удали если видишь это",
                    "backgroundColor": "Удали если видишь это",
                    "backgroundImage": "Удали если видишь это",
                    "text": "Удали если видишь это",
                    "title": "Удали если видишь это"
                }
            },

            "header-category": {
                "url": "content/header-category",
                "request": {
                    "bannerTemplates": {
                        "actionLink": True,
                        "crmId": "Удали если видишь это",
                        "link": "https://example.com",
                        "backgroundColor": "Удали если видишь это",
                        "backgroundImage": "Удали если видишь это",
                        "text": "Удали если видишь это",
                        "title": "Удали если видишь это"
                    },
                    "name": "Удали если видишь это",
                    "priority": "1",
                    "promo": [
                        {
                            "item": "Удали если видишь это",
                            "link": "https://example.com"
                        }
                    ],
                    "visible": True,
                    "isClickable": True,
                    "bottomMenu": True,
                    "crmId": "Удали если видишь это",
                    "actionLink": True,
                    "link": "https://example.com",
                    "categoryColor": "Удали если видишь это",
                    "categoryImage": "Удали если видишь это",
                    "subcategories": [
                        {
                            "title": "Удали если видишь это",
                            "priority": "1",
                            "isShowTitle": True,
                            "isClickable": True,
                            "crmId": "Удали если видишь это",
                            "actionLink": True,
                            "link": "https://example.com",
                            "isFullType": True,
                            "links": [
                                {
                                    "linkText": "Удали если видишь это",
                                    "link": "https://example.com",
                                    "priority": "1",
                                    "isBold": True
                                }
                            ]
                        }
                    ]
                }
            },

            "header-subcategory": {
                "url": "content/header-subcategory",
                "request": {
                    "title": "Удали если видишь это",
                    "priority": "1",
                    "isShowTitle": True,
                    "isClickable": True,
                    "crmId": "Удали если видишь это",
                    "actionLink": True,
                    "link": "https://example.com",
                    "isFullType": True,
                    "links": [
                        {
                            "linkText": "Удали если видишь это",
                            "link": "https://example.com",
                            "priority": "1",
                            "isBold": True
                        }
                    ]
                }
            },

            "product-card-labels": {
                "url": "content/product-card-labels",
                "request": {
                    "name": "Удали если видишь это",
                    "label": "Удали если видишь это",
                    "first": {
                        "active": True,
                        "outline": True,
                        "crmId": "Удали если видишь это",
                        "link": "https://example.com",
                        "text": "Удали если видишь это"
                    },
                    "second": {
                        "active": True,
                        "outline": True,
                        "crmId": "Удали если видишь это",
                        "link": "https://example.com",
                        "text": "Удали если видишь это"
                    },
                    "labelCMS": "Удали если видишь это",
                    "basicPrice": 0,
                    "basicPriceDiscount": "Удали если видишь это",
                    "additionalPrice": 0,
                    "additionalPriceDiscount": "Удали если видишь это",
                    "discount": 0,
                    "labels": [
                        {
                            "item": "Удали если видишь это",
                            "important": True
                        }
                    ],
                    "texts": [
                        {
                            "item": "Удали если видишь это"
                        }
                    ],
                    "isPresales": "Удали если видишь это"
                }
            },

            "product-cards": {
                "url": "content/product-cards",
                "request": {
                    "titleCard": "Удали если видишь это",
                    "titleCMS": "Удали если видишь это",
                    "subtitleCard": "Удали если видишь это",
                    "priority": 0,
                    "image": "string",
                    "backgroundColor": "Удали если видишь это",
                    "labelTemplates": [
                        {
                            "id": "ba7fced2-b512-439b-baa0-bf61107b7c0c",
                            "name": "Нужен для тестов",
                            "label": "string",
                            "labelCMS": "string",
                            "basicPrice": 0,
                            "basicPriceDiscount": "string",
                            "first": {
                                "active": True,
                                "outline": True,
                                "crmId": "string",
                                "link": "https://example.com",
                                "text": "string"
                            },
                            "second": {
                                "active": True,
                                "outline": True,
                                "crmId": "string",
                                "link": "https://example.com",
                                "text": "string"
                            },
                            "additionalPrice": 0,
                            "additionalPriceDiscount": "string",
                            "discount": 0,
                            "labels": [
                                {
                                    "item": "string",
                                    "important": True
                                }
                            ],
                            "texts": [
                                {
                                    "item": "string"
                                }
                            ],
                            "isPresales": "string",
                            "createdAt": "2022-07-29T17:57:23.042Z",
                            "updatedAt": "2022-07-29T17:57:23.042Z"
                        }
                    ],
                    "first": {
                        "active": True,
                        "outline": True,
                        "crmId": "Удали если видишь это",
                        "link": "https://example.com",
                        "text": "Удали если видишь это"
                    },
                    "second": {
                        "active": True,
                        "outline": True,
                        "crmId": "Удали если видишь это",
                        "link": "https://example.com",
                        "text": "Удали если видишь это"
                    },
                    "isUndefinedResultCard": True,
                    "isDefaultCard": True,
                    "category": "Удали если видишь это",
                    "categories": [
                        "Удали если видишь это"
                    ],
                    "city": [
                        "Удали если видишь это"
                    ],
                    "visible": True,
                    "filters": {
                        "grades": [
                            "Удали если видишь это"
                        ],
                        "disciplines": [
                            "Удали если видишь это"
                        ],
                        "formats": [
                            "Удали если видишь это"
                        ],
                        "months": [
                            "Удали если видишь это"
                        ],
                        "additionals": [
                            "Удали если видишь это"
                        ]
                    }
                }
            },

            "summer-product-cards": {
                "url": "content/summer-product-cards",
                "request": {
                    "titleCMS": "Удали если видишь это",
                    "title": "test",
                    "priority": "1",
                    "button": {
                        "outline": True,
                        "active": True,
                        "link": "test",
                        "crmId": "test",
                        "text": "test"
                    },
                    "buttonReg": {
                        "outline": True,
                        "active": True,
                        "link": "test",
                        "crmId": "test",
                        "text": "test"
                    },
                    "description": {
                        "theme": "test",
                        "title": "test",
                        "text": "test"
                    },
                    "visible": True,
                    "discountedPrice": "test",
                    "fullPrice": "test",
                    "labels": [
                        {
                            "text": "test",
                            "backgroundColor": "test"
                        }
                    ],
                    "groupId": "90c90826-a7c8-e811-a97a-000d3ab20be2",
                    "lmsId": "1312",
                    "filters": {
                        "grades": [
                            "Удали если видишь это"
                        ],
                        "disciplines": [
                            "Удали если видишь это"
                        ],
                        "formats": [
                            "Удали если видишь это"
                        ],
                        "months": [
                            "Удали если видишь это"
                        ],
                        "additionals": [
                            "Удали если видишь это"
                        ]
                    }
                }
            },

            "store-subject-templates": {
                "url": "content/store-subject-templates",
                "request": {
                    "name": "Удали если видишь это",
                    "list": [
                        {
                            "item": "Удали если видишь это",
                            "groupId": "1312",
                            "courseId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
                        }
                    ]
                }
            },

            "store-text-templates": {
                "url": "content/store-text-templates",
                "request": {
                    "name": "Удали если видишь это",
                    "label": "Удали если видишь это",
                    "points": [
                        {
                            "title": "Удали если видишь это",
                            "text": "Удали если видишь это"
                        }
                    ]
                }
            },

            "store-page-templates": {
                "url": "content/store-page-templates",
                "request": {
                    "name": "Удали если видишь это",
                    "courseName": "Удали если видишь это",
                    "courseFormat": "Удали если видишь это",
                    "url": "data_for_test",
                    "title": "Удали если видишь это",
                    "subtitle": "Удали если видишь это",
                    "selectSubjectStep": {
                        "label": "Удали если видишь это",
                        "title": "Удали если видишь это",
                        "text": "Удали если видишь это"
                    },
                    "typePaymentStep": {
                        "label": "Удали если видишь это",
                        "title": "Удали если видишь это",
                        "text": "Удали если видишь это"
                    },
                    "paymentSectionStep": {
                        "label": "Удали если видишь это",
                        "title": "Удали если видишь это",
                        "text": "Удали если видишь это"
                    },
                    "textTemplates": [
                        {
                            "name": "Удали если видишь это",
                            "label": "Удали если видишь это",
                            "points": [
                                {
                                    "title": "Удали если видишь это",
                                    "text": "Удали если видишь это"
                                }
                            ]
                        }
                    ],
                    "subjectTemplate": {
                        "name": "Удали если видишь это",
                        "list": [
                            {
                                "item": "Удали если видишь это",
                                "groupId": "1312",
                                "courseId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
                            }
                        ]
                    },
                    "thankTemplates": {
                        "name": "Удали если видишь это",
                        "isForm": True,
                        "topBlock": {
                            "title": "Удали если видишь это",
                            "description": "Удали если видишь это",
                            "promocode": "Удали если видишь это"
                        },
                        "bottomBlock": {
                            "title": "Удали если видишь это",
                            "description": "Удали если видишь это",
                            "promocode": "Удали если видишь это"
                        },
                        "button": {
                            "title": "Удали если видишь это",
                            "link": "Удали если видишь это"
                        }
                    },
                    "preselectedSubject": "Удали если видишь это",
                    "preselectedPaymentType": "Удали если видишь это",
                    "once": {
                        "active": True,
                        "fullPrice": 0,
                        "discount": 0,
                        "discountedPrice": 0
                    },
                    "recurrent": {
                        "active": True,
                        "fullPrice": 0,
                        "firstPayDiscount": 0,
                        "discountedPrice": 0,
                        "followingPaysPrice": 0,
                        "duration": 0
                    },
                    "crmId": "Удали если видишь это",
                    "dropCartCrmId": "Удали если видишь это",
                    "successCartCrmId": "Удали если видишь это",
                    "issueYear": 0,
                    "promo": True,
                    "schedule": True,
                    "showGroupStartDate": True,
                    "monthlyPayment": True
                }
                # "unique": ["url"]
            },

            "store-thanks-page-templates": {
                "url": "content/store-thanks-page-templates",
                "request": {
                    "name": "data_for_test",
                    "isForm": True,
                    "topBlock": {
                        "title": "Удали если видишь это",
                        "description": "Удали если видишь это",
                        "promocode": "Удали если видишь это"
                    },
                    "bottomBlock": {
                        "title": "Удали если видишь это",
                        "description": "Удали если видишь это",
                        "promocode": "Удали если видишь это"
                    },
                    "button": {
                        "title": "Удали если видишь это",
                        "link": "Удали если видишь это"
                    }
                }
                # "unique": ["name"]
            },

            "filters": {
                "url": "content/filters",
                "request": {
                    "name": "Удали если видишь это",
                    "url": "Удали если видишь это",
                    "fields": {
                        "grade": {
                            "name": "Удали если видишь это",
                            "nameMobile": "Удали если видишь это",
                            "priority": 1,
                            "showAll": True,
                            "showAllTitle": "Удали если видишь это",
                            "multi": True
                        },
                        "discipline": {
                            "name": "Удали если видишь это",
                            "nameMobile": "Удали если видишь это",
                            "priority": 1,
                            "showAll": True,
                            "showAllTitle": "Удали если видишь это",
                            "multi": True
                        },
                        "format": {
                            "name": "Удали если видишь это",
                            "nameMobile": "Удали если видишь это",
                            "priority": 1,
                            "showAll": True,
                            "showAllTitle": "Удали если видишь это",
                            "multi": True
                        },
                        "month": {
                            "name": "Удали если видишь это",
                            "nameMobile": "Удали если видишь это",
                            "priority": 1,
                            "showAll": True,
                            "showAllTitle": "Удали если видишь это",
                            "multi": True
                        },
                        "additional": {
                            "name": "Удали если видишь это",
                            "nameMobile": "Удали если видишь это",
                            "priority": 1,
                            "showAll": True,
                            "showAllTitle": "Удали если видишь это",
                            "multi": True
                        }
                    }
                }
            },

            "teachers": {
                "url": "content/teachers",
                "request": {
                    "name": "Удали если видишь это",
                    "image": "Удали если видишь это",
                    "subject": "Удали если видишь это",
                    "description": "Удали если видишь это",
                    "quote": "Удали если видишь это",
                    "details": [
                        {
                            "value": "Удали если видишь это",
                            "text": "Удали если видишь это"
                        }
                    ]
                }
            },

            "trial-lessons": {
                "url": "content/trial-lessons",
                "request": {
                    "digestName": "Удали если видишь это",
                    "grade": "11",
                    "subject": "Удали если видишь это",
                    "dateTime": "2023-06-24T00:00:00.000Z",
                    "companyId": "Удали если видишь это",
                    "express": False,
                    "tags": [
                        "11"
                    ],
                    "online": True
                }
            },

            "free-lessons": {
                "url": "content/free-lessons",
                "request": {
                    "name": "Удали если видишь это",
                    "url": "/Удали если видишь это",
                    "blockColor": "Удали если видишь это",
                    "firstScreen": {
                        "title": "Удали если видишь это",
                        "subtitle": "Удали если видишь это",
                        "btnText": "Удали если видишь это",
                        "imageUrl": "https://example.com"
                    },
                    "meta": {
                        "title": "Удали если видишь это",
                        "description": "Удали если видишь это"
                    },
                    "videoTitle": "Удали если видишь это",
                    "videos": [
                        {
                            "title": "Удали если видишь это",
                            "description": "Удали если видишь это",
                            "videoLink": "https://example.com",
                            "imageLink": "https://example.com",
                            "labels": [
                                "Удали если видишь это",
                                "Удали если видишь это"
                            ]
                        }
                    ]
                }
            },

            "vacancies": {
                "url": "content/vacancies",
                "request": {
                    "department": "IT",
                    "area": "Backend",
                    "name": "Удали если видишь это",
                    "experience": "Senior",
                    "city": [
                        "test"
                    ],
                    "salary": "test",
                    "video": None,
                    "skills": [
                        {
                            "name": "test"
                        },
                        {
                            "name": "test"
                        },
                        {
                            "name": "test"
                        },
                        {
                            "name": "test"
                        },
                        {
                            "name": "test"
                        }
                    ],
                    "recruiterEmail": "user@example.com",
                    "descriptionBlocks": [
                        {
                            "title": "Удали если видишь эт",
                            "description": "Удали если видишь эт"
                        }
                    ]
                }
            },

            "accordion": {
                "url": "content/accordion",
                "request": {
                    "name": "Удали если видишь это",
                    "category": "Удали если видишь это",
                    "title": "Удали если видишь это",
                    "items": [
                        {
                            "title": "Удали если видишь это",
                            "description": "Удали если видишь это"
                        }
                    ]
                }
                # "unique": ["category"]
            },

            "info-about-course": {
                "url": "content/info-about-course",
                "request": {
                    "name": "Удали если видишь это",
                    "title": "Удали если видишь это",
                    "blocks": [
                        {
                            "title": "Удали если видишь это",
                            "description": "Удали если видишь это",
                            "image": "Удали если видишь это"
                        }
                    ]
                }
            },

            "lead-forms": {
                "url": "content/lead-forms",
                "request": {
                    "name": "Удали если видишь это",
                    "visible": True,
                    "position": "1",
                    "title": "Удали если видишь это",
                    "subtitle": "Удали если видишь это",
                    "buttonText": "Button text",
                    "crmId": "CMP-00000-00001",
                    "urls": [
                        "/ege",
                        "/trial"
                    ],
                    "zeroContract": True,
                    "selectedInputs": [
                        {
                            "name": "firstName",
                            "isActive": True,
                            "priority": 1,
                            "isRequired": False,
                            "studentIsActive": True,
                            "studentPriority": 1,
                            "studentIsRequired": False
                        }
                    ],
                    "agreements": [
                        {
                            "checkbox": True,
                            "description": "string"
                        }
                    ],
                    "lmsId": "123",
                    "thankYouPopup": {
                        "title": "Удали если видишь это",
                        "description": "Удали если видишь это"
                    }
                }
            },

            "regions": {
                "url": "content/regions",
                "request": {
                    "programType": "ЕГЭ",
                    "isSubjectPage": False,
                    "metaTitle": "Удали если видишь это",
                    "metaDescription": "Удали если видишь это",
                    "title": "Удали если видишь это",
                    "description": "Удали если видишь это",
                    "info": "Удали если видишь это"
                }
            },

            "catalog": {
                "url": "content/catalog",
                "request": {
                    "noIndex": False,
                    "metaTitle": "Удали если видишь это",
                    "metaDescription": "Удали если видишь это",
                    "title": "Удали если видишь это",
                    "description": "Удали если видишь это",
                    "urls": [
                        "Удали если видишь это",
                        "Удали если видишь это"
                    ]
                }
            },

            # "pc/constructor-templates": {
            #     "url": "content/page-constructor/constructor-templates",
            #     "request": {
            #         "name": "Удали если видишь это",
            #         "url": "/example/example",
            #         "metaTitle": "Удали если видишь это",
            #         "metaDescription": "Удали если видишь это",
            #         "noIndex": True,
            #         "blocks": [
            #             {
            #                 "priority": 1,
            #                 "scrollId": "1",
            #                 "blockType": "firstScreen",
            #                 "blockTemplateId": "1a3c2816-0fa4-4381-8451-3bedf2c2649d"
            #             },
            #             {
            #                 "priority": 3,
            #                 "scrollId": "3",
            #                 "blockType": "bullets",
            #                 "blockTemplateId": "ba45bfdc-e17c-4f99-854f-b1ceedfe7a8a"
            #             },
            #             {
            #                 "priority": 4,
            #                 "scrollId": "4",
            #                 "blockType": "filterCards"
            #             },
            #             {
            #                 "priority": 5,
            #                 "scrollId": "5",
            #                 "blockType": "leadForm"
            #             },
            #             {
            #                 "pdfUrl": "https://storage.yandexcloud.net/maximumtest-site/maximumeducation/courses/Программа_допобразования_БИО_10_кл.pdf",
            #                 "priority": 6,
            #                 "scrollId": "6",
            #                 "blockType": "formatText"
            #             },
            #             {
            #                 "priority": 7,
            #                 "scrollId": "7",
            #                 "blockType": "iFrame",
            #                 "blockTemplateId": "d5ea6890-9662-4743-88ac-73a374614811"
            #             }
            #         ]
            #     },
            #     "response": {
            #         "type": "object",
            #         "properties": {
            #             "id": {"type": "string"},
            #             "name": {"type": "string"},
            #             "url": {"type": "string"},
            #             "noIndex": {"type": ["boolean", "null"]},
            #             "metaTitle": {"type": "string"},
            #             "metaDescription": {"type": "string"},
            #             "blocks": {
            #                 "type": "array",
            #                 "items": {
            #                     "priority": {"type": "number"},
            #                     "scrollId": {"type": "string"},
            #                     "blockType": {"type": "string"},
            #                     "blockTemplateId": {"type": "string"}
            #                 }
            #             },
            #             "createdAt": {"type": "string"},
            #             "updatedAt": {"type": "string"}
            #         }
            #     }
            # },

            "page-constructor/bullet-templates": {
                "url": "content/page-constructor/bullet-templates",
                "request": {
                    "name": "Удали если видишь это",
                    "title": "Удали если видишь это",
                    "bullets": [
                        {
                            "text": "Удали если видишь это"
                        },
                        {
                            "text": "Удали если видишь это"
                        },
                        {
                            "text": "Удали если видишь это"
                        },
                        {
                            "text": "Удали если видишь это"
                        }
                    ]
                }
            },

            "page-constructor/first-screen-templates": {
                "url": "content/page-constructor/first-screen-templates",
                "request": {
                    "name": "Удали если видишь это",
                    "title": "Удали если видишь это",
                    "description": "Удали если видишь это",
                    "image": "https://cloud.yandex.ru/example",
                    "buttons": [
                        {
                            "text": "Удали меня",
                            "style": "outline",
                            "active": True,
                            "actionType": "scroll",
                            "actionValue": "filters"
                        }
                    ]
                }
            },

            "page-constructor/iframe-templates": {
                "url": "content/page-constructor/iframe-templates",
                "request": {
                    "name": "Удали если видишь это",
                    "url": "https://example.com",
                    "breakpoints": [
                        {
                            "breakpointMaxWidth": "1100",
                            "breakpointHeight": "100px"
                        }
                    ],
                    "ignoreContainer": False,
                    "height": "100"
                }
            },

            "page-constructor/text-block-templates": {
                "url": "content/page-constructor/text-block-templates",
                "request": {
                    "name": "Удали если видишь это",
                    "text": "Удали если видишь это"
                }
            },

            "page-constructor/html-block-templates": {
                "url": "content/page-constructor/html-block-templates",
                "request": {
                    "name": "Удали если видишь это",
                    "htmlData": "Удали если видишь это"
                }
            },

            "page-constructor/why-us-block-templates": {
                "url": "content/page-constructor/why-us-block-templates",
                "request": {
                    "name": "Удали если видишь это",
                    "title": "Удали если видишь это",
                    "subtitle": "Удали если видишь это",
                    "info": [
                        {
                            "title": "225 000",
                            "subtitle": "учеников по всей России учатся вместе с нами"
                        }
                    ],
                    "image": {
                        "width": "200px",
                        "height": "300px",
                        "src": "example.com",
                        "alt": "example"
                    }
                }
            },

            "web-events": {
                "url": "content/web-events",
                "request": {
                    "page": "/events",
                    "title": "Удали если видишь это",
                    "description": "Удали если видишь это",
                    "filter": [
                        "string"
                    ],
                    "keyWords": [
                        "string"
                    ],
                    "class": "string",
                    "image": "https://staging-maximumtestru-bucket.storage.yandexcloud.net/autosales-images/9313f185-3f69-4acf-8a8c-ce7b0c283221-1600703741155793420.jpeg",
                    "buttonText": "Удали если видишь это",
                    "formatOnline": True,
                    "classes": [
                        "string"
                    ],
                    "date": "2022-01-27T12:00:00.000Z",
                    "address": "Удали если видишь это",
                    "crmId": "string",
                    "actionLink": True,
                    "link": "string",
                    "examType": "string",
                    "price": "string",
                    "oldPrice": "string"
                }
            },

            "web-event-filters": {
                "url": "content/web-event-filters",
                "request": {
                    "page": "/events",
                    "filterElement": "Filter",
                    "subFilterElements": [
                        "Удали если видишь это",
                        "Удали если видишь это"
                    ]
                }
            },

            "web-event-page": {
                "url": "content/web-event-page?page=%2Fevents'"
            },

            "webhooks/marquiz": {
                "url": "content/webhooks/marquiz",
                "request": {
                    "quizId": "Удали если видишь это",
                    "campaignCode": "Удали если видишь это"
                }
            },

            "handbooks": {
                "url": "content/handbooks",
                "request": {
                    "type": "Удали если видишь это",
                    "value": "Удали если видишь это"
                }
            },

            "footer": {
                "url": "content/footer",
                "request": {
                    "sections": [
                    ]
                }
            },

            "footer-sections": {
                "url": "content/footer-sections",
                "request": {
                    "title": "Удали если видишь это",
                    "priority": "1",
                    "isShowTitle": True,
                    "links": [
                        {
                            "linkText": "Удали если видишь это",
                            "link": "https://example.com",
                            "priority": "1"
                        }
                    ]
                }
            },

            "static-pages-first-screen": {
                "url": "content/static-pages-first-screen",
                "request": {
                    "category": "/Удали если видишь это",
                    "title": "Удали если видишь это",
                    "subtitle": "Удали если видишь это",
                    "formTitle": "Удали если видишь это",
                    "image": "https://example.com",
                    "subjectsInfo": "string",
                    "firstButton": {
                        "text": "Удали если видишь это",
                        "action": "string"
                    },
                    "secondButton": {
                        "text": "Удали если видишь это",
                        "action": "string"
                    }
                }
            },

            "static-pages-group-info": {
                "url": "content/static-pages-group-info",
                "request": {
                    "category": "/Удали если видишь это",
                    "cards": [
                        {
                            "title": "Удали если видишь это",
                            "text": "Удали если видишь это"
                        }
                    ]
                }
            },

            "static-pages-guarantee-info": {
                "url": "content/static-pages-guarantee-info",
                "request": {
                    "category": "/Удали если видишь это",
                    "paragraphs": [
                        "Удали если видишь это"
                    ]
                }
            },

            "static-pages-course-program": {
                "url": "content/static-pages-course-program",
                "request": {
                    "category": "/Удали если видишь это",
                    "classes": [
                        {
                            "class": "Удали если видишь это",
                            "courseProgram": [
                                {
                                    "item": "Удали если видишь это",
                                    "important": True
                                }
                            ]
                        }
                    ]
                }
            },

            "static-pages-benefits-info": {
                "url": "content/static-pages-benefits-info",
                "request": {
                    "category": "/Удали если видишь это",
                    "title": "Удали если видишь это",
                    "subtitle": "Удали если видишь это",
                    "statBlocks": [
                        {
                            "title": "Удали если видишь это",
                            "text": "Удали если видишь это"
                        }
                    ]
                }
            },

            "static-pages-content": {
                "url": "content/static-pages-content?category=%2Fege'"
            },

            "cities": {
                "url": "content/cities",
                "request": {
                    "country": "ru",
                    "city": "Удали если видишь это",
                    "actualAddress": {
                        "address": "Удали если видишь это",
                        "email": "Удали если видишь это",
                        "metro": "Удали если видишь это",
                        "workTime": "12:00-19:00",
                        "phone": "+7 (999) 999-99-99",
                        "abbreviation": "spb",
                        "isPhoneCalltracking": False
                    },
                    "requisites": [
                        {
                            "name": "ИНН",
                            "value": "0123456789"
                        }
                    ],
                    "multiAddress": False,
                    "secondaryAddresses": [
                        {
                            "address": "Удали если видишь это",
                            "email": "Удали если видишь это",
                            "metro": "Удали если видишь это",
                            "workTime": "12:00-19:00",
                            "phone": "+7 (999) 999-99-99",
                            "abbreviation": "spb",
                            "isPhoneCalltracking": False
                        }
                    ]
                }
            },

            "cities/ip": {
                "url": "/content/cities/ip"
            },

            "uchebnik/seo-settings": {
                "url": "content/uchebnik/seo-settings",
                "request": {
                    "url": "Удали если видишь это",
                    "propagation": True,
                    "metaTitle": "Удали если видишь это",
                    "metaDescription": "Удали если видишь это",
                    "noIndex": True
                }
            }

            # "": {
            #     "url": "",
            #     "request": {
            #
            #     }
            # },
        }

        return data

    @staticmethod
    def get_mass_data():
        data = {
            "mass/product-card-labels": {
                "url": "content/mass/product-card-labels",
                "request": [
                    {
                        "name": "Удали если видишь это",
                        "label": "Удали если видишь это",
                        "first": {
                            "active": True,
                            "outline": True,
                            "crmId": "Удали если видишь это",
                            "link": "https://example.com",
                            "text": "Удали если видишь это"
                        },
                        "second": {
                            "active": True,
                            "outline": True,
                            "crmId": "Удали если видишь это",
                            "link": "https://example.com",
                            "text": "Удали если видишь это"
                        },
                        "labelCMS": "string",
                        "basicPrice": 0,
                        "basicPriceDiscount": "Удали если видишь это",
                        "additionalPrice": 0,
                        "additionalPriceDiscount": "Удали если видишь это",
                        "discount": 0,
                        "labels": [
                            {
                                "item": "Удали если видишь это",
                                "important": True
                            }
                        ],
                        "texts": [
                            {
                                "item": "Удали если видишь это"
                            }
                        ],
                        "isPresales": "Удали если видишь это"
                    },
                ]
            },

            "mass/product-cards": {
                "url": "content/mass/product-cards",
                "request": [
                    {
                        "titleCard": "Удали если видишь это",
                        "titleCMS": "Удали если видишь это",
                        "subtitleCard": "string",
                        "priority": 0,
                        "image": "string",
                        "backgroundColor": "string",
                        "labelTemplates": [
                            {
                                "name": "Удали если видишь это",
                                "label": "string",
                                "first": {
                                    "active": True,
                                    "outline": True,
                                    "crmId": "string",
                                    "link": "https://example.com",
                                    "text": "string"
                                },
                                "second": {
                                    "active": True,
                                    "outline": True,
                                    "crmId": "string",
                                    "link": "https://example.com",
                                    "text": "string"
                                },
                                "labelCMS": "string",
                                "basicPrice": 0,
                                "basicPriceDiscount": "string",
                                "additionalPrice": 0,
                                "additionalPriceDiscount": "string",
                                "discount": 0,
                                "labels": [
                                    {
                                        "item": "string",
                                        "important": True
                                    }
                                ],
                                "texts": [
                                    {
                                        "item": "string"
                                    }
                                ],
                                "isPresales": "string"
                            }
                        ],
                        "first": {
                            "active": True,
                            "outline": True,
                            "crmId": "string",
                            "link": "https://example.com",
                            "text": "string"
                        },
                        "second": {
                            "active": True,
                            "outline": True,
                            "crmId": "string",
                            "link": "https://example.com",
                            "text": "string"
                        },
                        "isUndefinedResultCard": True,
                        "isDefaultCard": True,
                        "category": "string",
                        "categories": [
                            "string"
                        ],
                        "city": [
                            "string"
                        ],
                        "visible": True,
                        "filters": {
                            "grades": [
                                "string"
                            ],
                            "disciplines": [
                                "string"
                            ],
                            "formats": [
                                "string"
                            ],
                            "months": [
                                "string"
                            ],
                            "additionals": [
                                "string"
                            ]
                        }
                    }
                ]
            }
        }

        return data

    @staticmethod
    def get_file_data():
        data = {
            "files": {
                "url": "content/files/for_test_dont_remove",
                "request": {'file': ('for_test_txt.txt', open(path.to_resource('for_test_txt.txt'), 'rb'))}
                # "unique": ["name"]
            }
        }

        return data
