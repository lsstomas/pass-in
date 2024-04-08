from typing import Dict
from src.models.entities.check_ins import CheckIns
from src.models.settings.connection import db_connection_handler
from sqlalchemy.exc import IntegrityError


class CheckInsRepository:
    def insert_check_in(self, attendee_id: int):
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIns(attendeeId=attendee_id)
                )

                database.session.add(check_in)
                database.session.commit()

                return attendee_id

            except Exception as exception:
                database.session.rollback()
                raise exception

            except IntegrityError:
                raise Exception("Check-in já efetuado!")
