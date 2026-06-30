import csv

from app.database.mysql import Database
from app.services.question_service import QuestionService
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "question_DD_data.csv")

def create_table():
    conn, cursor = Database.get_transaction()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question TEXT NOT NULL,
        normalized_question TEXT NOT NULL,
        department VARCHAR(255) NOT NULL,
        division VARCHAR(255) NOT NULL
    )
    """)

    conn.commit()

    cursor.close()
    conn.close()


def import_data():
    with open(CSV_PATH , newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                QuestionService.add_question(
                    question=row["question"],
                    department=row["department"],
                    division=row["division"]
                )
                print(f"Imported: {row['question']}")

            except ValueError:
                print(f"Skipped: {row['question']} (Already exists)")

            except Exception as e:
                print(f"Error: {row['question']} -> {e}")


if __name__ == "__main__":
    create_table()
    import_data()
    print("Import completed.")