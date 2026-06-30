from app.database.mysql import DatabaseHelper
from app.services.training_service import TrainingService
from app.services.qdrant_service import QdrantService
from app.utils.logger import get_logger
from app.utils.validator import normalize_question
from app.database.mysql import Database

logger = get_logger(__name__)


class QuestionService:

    @staticmethod
    def question_exists(question: str):

        normalized = normalize_question(question)

        sql = """
        SELECT id
        FROM questions
        WHERE normalized_question=%s
        """

        return DatabaseHelper.fetch_one(
            sql,
            (normalized,)
        )


    @staticmethod
    def add_question(question, department, division):

        normalized = normalize_question(question)

        if QuestionService.question_exists(question):
            raise ValueError("Question already exists.")

        conn, cursor = Database.get_transaction()

        try:

            cursor.execute(
                """
                INSERT INTO questions
                (
                    question,
                    normalized_question,
                    department,
                    division
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s
                )
                """,
                (
                    question,
                    normalized,
                    department,
                    division
                )
            )

            question_id = cursor.lastrowid

            conn.commit()

            embedding = TrainingService.encode(question)
            
            QdrantService.insert_vector(
                question_id,
                embedding,
                question,
                department,
                division
            )

            conn.commit()

            logger.info(f"Question Created : {question_id}")

            return question_id

        except Exception as e:

            conn.rollback()

            logger.exception("Failed to add question")

            raise

        finally:

            cursor.close()

            conn.close()
    @staticmethod
    def get_question(question_id):

        sql = """
        SELECT *
        FROM questions
        WHERE id=%s
        """

        return DatabaseHelper.fetch_one(
            sql,
            (question_id,)
        )

    @staticmethod
    def get_all():

        sql = """
        SELECT *
        FROM questions
        ORDER BY id DESC
        """

        return DatabaseHelper.fetch_all(sql)


    
    @staticmethod
    def delete_question(question_id):

        existing = QuestionService.get_question(question_id)

        if existing is None:
            raise Exception("Question not found")

        conn, cursor = Database.get_transaction()

        try:

            cursor.execute(
                """
                DELETE FROM questions
                WHERE id=%s
                """,
                (question_id,)
            )

            QdrantService.delete_vector(question_id)

            conn.commit()

            logger.info(
                f"Question Deleted : {question_id}"
            )

        except Exception as e:

            conn.rollback()

            logger.exception(e)

            raise

        finally:

            cursor.close()

            conn.close()

    @staticmethod
    def update_question(
        question_id,
        question,
        department,
        division
    ):
        
        existing_question = QuestionService.get_question(question_id)

        if existing_question is None:
            raise Exception("Question not found")

        normalized = normalize_question(question)

        sql = """
        UPDATE questions

        SET

        question=%s,

        normalized_question=%s,

        department=%s,

        division=%s

        WHERE id=%s
        """

        DatabaseHelper.execute(

            sql,

            (

                question,

                normalized,

                department,

                division,

                question_id

            )

        )

        embedding = TrainingService.encode(
            question
        )

        QdrantService.update_vector(

            question_id,

            embedding,

            question,

            department,

            division

        )

        logger.info(
            f"Question Updated : {question_id}"
        )