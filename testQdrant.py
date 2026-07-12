from qdrant_client import QdrantClient

from app.config.constants import COLLECTION_NAME

client = QdrantClient(path="data/qdrant")

points, _ = client.scroll(
    collection_name=COLLECTION_NAME,
    limit=1,
    with_payload=True,
    with_vectors=True,
)

if not points:
    print("No data found.")
    exit()

point = points[0]

print("=" * 80)
print("POINT ID")
print("=" * 80)
print(point.id)

print("\n")

print("=" * 80)
print("PAYLOAD")
print("=" * 80)

for key, value in point.payload.items():

    if key == "text":
        print(f"\nTEXT:\n{value}\n")
    else:
        print(f"{key}: {value}")

print("\n")

print("=" * 80)
print("VECTOR INFORMATION")
print("=" * 80)

print("Vector Dimension :", len(point.vector))

print("\nFirst 20 Values:\n")

print(point.vector[:20])