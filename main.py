import os
import asyncio


import uvicorn
from schemas.fieldsschema import ArtworkCreate, CommentCreate
from schemas.graphschema import type_defs
from fastapi import FastAPI
from ariadne import make_executable_schema, ObjectType, QueryType, MutationType, graphql
from ariadne.asgi import GraphQL
from motor.motor_asyncio import AsyncIOMotorClient
from db.database import PyObjectId,ObjectId


MONGO_DATABASE_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DATABASE_NAME = "cosmic_canvas"   
   
client = AsyncIOMotorClient(MONGO_DATABASE_URL)
db = client[DATABASE_NAME]


query = QueryType()
mutation = MutationType()
artwork = ObjectType("Artwork")


@query.field("all_artworks")
async def resolve_all_artworks(_, info):
    artwork_docs = await db.artworks.find().to_list(length=100)
    return [
        {
            "id": str(doc["_id"]),
            "title": doc["title"],
            "description": doc.get("description"),
            "artistName": doc["artist_name"]  
        } for doc in artwork_docs
    ]

@query.field("artwork_by_id")
async def resolve_artwork_by_id(_, info, id):
    doc = await db.artworks.find_one({"_id": ObjectId(id)})
    if doc:
        return {
            "id": str(doc["_id"]),
            "title": doc["title"],
            "description": doc.get("description"),
            "artistName": doc["artist_name"]  
        }
    return None

@artwork.field("comments")
async def resolve_comments(obj, info):
    comment_docs = await db.comments.find({"artwork_id": ObjectId(obj["id"])}).to_list(length=100)
    return [
        {
            "id": str(comment_doc["_id"]),
            "author": comment_doc["author"],
            "text": comment_doc["text"],
            "artwork_id": str(comment_doc["artwork_id"])
        } for comment_doc in comment_docs
    ]

@mutation.field("createArtwork")
async def resolve_create_artwork(_, info, title, artistName, description=None):
    artwork_data = ArtworkCreate(title=title, description=description, artist_name=artistName)
    result = await db.artworks.insert_one(artwork_data.dict())
    new_artwork_doc = await db.artworks.find_one({"_id": result.inserted_id})
    artwork = {
        "id": str(new_artwork_doc["_id"]),
        "title": new_artwork_doc["title"],
        "description": new_artwork_doc.get("description"),
        "artistName": new_artwork_doc["artist_name"]
    }
    return {"ok": True, "artwork": artwork}

@mutation.field("createComment")
async def resolve_create_comment(_, info, artworkId, author, text):
    if not await db.artworks.find_one({"_id": ObjectId(artworkId)}):
        raise Exception("Artwork not found!")
    comment_data = CommentCreate(author=author, text=text)
    comment_doc = comment_data.dict()
    comment_doc["artwork_id"] = ObjectId(artworkId)
    result = await db.comments.insert_one(comment_doc)
    new_comment_doc = await db.comments.find_one({"_id": result.inserted_id})
    comment = {
        "id": str(new_comment_doc["_id"]),
        "author": new_comment_doc["author"],
        "text": new_comment_doc["text"],
        "artworkId": str(new_comment_doc["artwork_id"])
    }
    return {"ok": True, "comment": comment}



@mutation.field("updateArtwork")
async def resolve_update_artwork(_, info, id, title=None, description=None, artistName=None):
    update_data = {}
    if title is not None:
        update_data["title"] = title
    if description is not None:
        update_data["description"] = description
    if artistName is not None:
        update_data["artist_name"] = artistName
    result = await db.artworks.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.modified_count == 0:
        return {"ok": False, "artwork": None}
    updated_doc = await db.artworks.find_one({"_id": ObjectId(id)})
    artwork = {
        "id": str(updated_doc["_id"]),
        "title": updated_doc["title"],
        "description": updated_doc.get("description"),
        "artistName": updated_doc["artist_name"]
    }
    return {"ok": True, "artwork": artwork}


@mutation.field("deleteArtwork")
async def resolve_delete_artwork(_, info, id):
    result = await db.artworks.delete_one({"_id": ObjectId(id)})
    return {"ok": result.deleted_count > 0}

@mutation.field("updateComment")
async def resolve_update_comment(_, info, id, author=None, text=None):
    update_data = {}
    if author is not None:
        update_data["author"] = author
    if text is not None:
        update_data["text"] = text
    result = await db.comments.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.modified_count == 0:
        return {"ok": False, "comment": None}
    updated_doc = await db.comments.find_one({"_id": ObjectId(id)})
    comment = {
        "id": str(updated_doc["_id"]),
        "author": updated_doc["author"],
        "text": updated_doc["text"],
        "artworkId": str(updated_doc["artwork_id"])
    }
    return {"ok": True, "comment": comment}

@mutation.field("deleteComment")
async def resolve_delete_comment(_, info, id):
    result = await db.comments.delete_one({"_id": ObjectId(id)})
    return {"ok": result.deleted_count > 0}



schema = make_executable_schema(type_defs, [query, mutation, artwork])



app = FastAPI(
    title="Cosmic Canvas API",
    description="A GraphQL API for a collaborative art gallery, built with FastAPI and MongoDB.",
    version="1.0.0",
)

graphql_app = GraphQL(schema, debug=True)

@app.on_event("startup")
async def startup_event():
    print("Connecting to MongoDB...")
    try:
        await client.admin.command('ping')
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

@app.on_event("shutdown")
async def shutdown_event():
    print("Closing MongoDB connection.")
    client.close()


app.mount("/graphql", graphql_app)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cosmic Canvas API! Visit /graphql to use the GraphiQL interface."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

