

ASSESSMENTS_TABLE = """create table assessments (
                    id bigint generated by default as identity primary key,
                    inserted_at timestamp with time zone default timezone('utc'::text, now()) not null,
                    updated_at timestamp with time zone default timezone('utc'::text, now()) not null,
                    data jsonb,
                    name text
                    )"""