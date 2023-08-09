from sqlalchemy.orm import Session

with Session() as session:
    with session.begin() as blok:
        a = 5
