from app.db.database import SessionLocal
from app.db.models import HealthResult as HealthResultModel
from app.health.result import HealthResult


class HealthRepository:

    def save(self, result: HealthResult):

        session = SessionLocal()

        try:
            db_result = HealthResultModel(
                service_name=result.service_name,
                status=result.status,
                response_time_ms=result.response_time_ms,
            )

            session.add(db_result)
            session.commit()

        finally:
            session.close()

    def get_all(self):

        session = SessionLocal()

        try:
            return session.query(HealthResultModel).all()

        finally:
            session.close()

    def get_latest(self):

        session = SessionLocal()

        try:
            return (
                session.query(HealthResultModel)
                .order_by(HealthResultModel.checked_at.desc())
                .all()
            )
        finally:
            session.close()