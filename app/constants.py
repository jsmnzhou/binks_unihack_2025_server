ASSESSMENTS_TABLE = """create table assessments (
                    name text
                    weight float8
                    due_date timestamptz
                    description text
                    )"""

CLASS_TABLE = """create table assessments (
                    name text
                    start_time timestamptz
                    end_time timestamptz
                    location text
                    description text
                    )"""

ASSESSMENTS_JSON = [{'name' : 'Structured Test (Integrated Skills)',
                       'weight' : 20,
                       'due_date': '2025-03-24T00:00:00+00',
                       'description': 'Reading Comprehension; Listening Comprehension, Grammar and Vocabulary. True/false, multiple  choice, direct  question, matching, gap- filling exercises'},
                    {'name' : 'Collaborative Project: "Inventions"',
                       'weight' : 10,
                       'due_date': '2025-03-24T00:00:00+00',
                       'description': 'Assessed with rubric'}
                    ]
ASSESSMENTS_TEXT = """
                    DATE TYPE DESCRIPTION WEIGHT
                    Tuesday, 24 March TEST Structured Test (Integrated Skills): Reading Comprehension; Listening Comprehension, Grammar and Vocabulary. True/false, multiple  choice, direct  question, matching, gap- filling exercises. 20% 
                    Wednesday, 8 April PERFORMANCE Collaborative Project: "Inventions" Assessed with rubric 10%
                    """