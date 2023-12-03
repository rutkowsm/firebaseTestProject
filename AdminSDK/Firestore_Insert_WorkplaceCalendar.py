import firebase_admin
from firebase_admin import credentials, firestore

DAYS_OF_THE_WEEK = {
    1: 'MONDAY',
    2: 'TUESDAY',
    3: 'WEDNESDAY',
    4: 'THURSDAY',
    5: 'FRIDAY',
    6: 'SATURDAY',
    7: 'SUNDAY'
}

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

workplace_id_input = 'Bvl0wDXzB3hpi7WaTiVx'

wkpl_cal_ref = db.collection('Workplace_Calendar').document(workplace_id_input + '20231204')

#
# for day_id, day in DAYS_OF_THE_WEEK:
#
#
# weekly_calendar_input = {}

wkpl_cal_ref.set({
    'workplace_id': workplace_id_input,
    'weekly_calendar': {
        'date_from': '20231204',
        'status': 'A',
        'daily_blocks': {
            '20231204': {
                'day_index': 1,
                'date': '20231204',
                'day_name': 'Monday',
                'vacancies': {
                    None
                }
            },
            '20231205': {
                'day_index': 2,
                'date': '20231205',
                'day_name': 'Tuesday',
                'vacancies': {
                    '1': {
                        'sequence_number': 1,
                        'hour_from': 12,
                        'hour_to': 22,
                        'hour_blocks': {
                            '12': {
                                'hour_index': 12,
                                'hour_txt': '12:00',
                                'covered_by': {
                                    'employee_id': 'empdoc1',
                                    'employee_name': 'Alicia'
                                }
                            },
                            '13': {
                                'hour_index': 13,
                                'hour_txt': '13:00',
                                'covered_by': {
                                    'employee_id': 'empdoc1',
                                    'employee_name': 'Alicia'
                                }
                            },
                            '14': {
                                'hour_index': 14,
                                'hour_txt': '14:00',
                                'covered_by': {
                                    'employee_id': 'empdoc1',
                                    'employee_name': 'Alicia'
                                }
                            },
                            '15': {
                                'hour_index': 15,
                                'hour_txt': '15:00',
                                'covered_by': {
                                    'employee_id': 'empdoc1',
                                    'employee_name': 'Alicia'
                                }
                            },
                            '16': {
                                'hour_index': 16,
                                'hour_txt': '16:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '17': {
                                'hour_index': 17,
                                'hour_txt': '17:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '18': {
                                'hour_index': 18,
                                'hour_txt': '18:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '19': {
                                'hour_index': 19,
                                'hour_txt': '19:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '20': {
                                'hour_index': 20,
                                'hour_txt': '20:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '21': {
                                'hour_index': 21,
                                'hour_txt': '21:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '22': {
                                'hour_index': 22,
                                'hour_txt': '22:00',
                                'covered_by': {
                                    None
                                }
                            },
                        }
                    },
                    '2': {
                        'sequence_number': 2,
                        'hour_from': 12,
                        'hour_to': 22,
                        'hour_blocks': {
                            '12': {
                                'hour_index': 12,
                                'hour_txt': '12:00',
                                'covered_by': {
                                    'employee_id': 'empdoc1',
                                    'employee_name': 'Alicia'
                                }
                            },
                            '13': {
                                'hour_index': 13,
                                'hour_txt': '13:00',
                                'covered_by': {
                                    'employee_id': 'empdoc1',
                                    'employee_name': 'Alicia'
                                }
                            },
                            '14': {
                                'hour_index': 14,
                                'hour_txt': '14:00',
                                'covered_by': {
                                    'employee_id': 'empdoc1',
                                    'employee_name': 'Alicia'
                                }
                            },
                            '15': {
                                'hour_index': 15,
                                'hour_txt': '15:00',
                                'covered_by': {
                                    'employee_id': 'empdoc1',
                                    'employee_name': 'Alicia'
                                }
                            },
                            '16': {
                                'hour_index': 16,
                                'hour_txt': '16:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '17': {
                                'hour_index': 17,
                                'hour_txt': '17:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '18': {
                                'hour_index': 18,
                                'hour_txt': '18:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '19': {
                                'hour_index': 19,
                                'hour_txt': '19:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '20': {
                                'hour_index': 20,
                                'hour_txt': '20:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '21': {
                                'hour_index': 21,
                                'hour_txt': '21:00',
                                'covered_by': {
                                    None
                                }
                            },
                            '22': {
                                'hour_index': 22,
                                'hour_txt': '22:00',
                                'covered_by': {
                                    None
                                }
                            },
                        }
                    },

                }
            }
        }
    }
})
