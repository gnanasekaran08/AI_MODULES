from app.database.mysql import DatabaseHelper
from app.services.training_service import TrainingService
from app.services.qdrant_service import QdrantService

QdrantService.create_collection()

rows = DatabaseHelper.fetch_all("""
SELECT
    id,
    question,
    department,
    division
FROM questions
""")

print(f"Found {len(rows)} questions")

for row in rows:

    embedding = TrainingService.encode(row["question"])

    QdrantService.insert_vector(
        question_id=row["id"],
        embedding=embedding,
        question=row["question"],
        department=row["department"],
        division=row["division"]
    )

print("Import completed successfully.")