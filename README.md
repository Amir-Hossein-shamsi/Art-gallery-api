# 🎨 Art Gallery API

**Art Gallery API** — a collaborative art gallery backend built with FastAPI, GraphQL (Ariadne), and MongoDB. This project lets you create, update, and explore artworks and comments in real time!

---

## 🚀 Features

- **GraphQL API** for flexible queries and mutations
- **MongoDB** for scalable, document-based storage
- **Artwork & Comments** management
- **Live reload** for development

---

## 📁 Project Structure

```bash
.
├── main.py              # FastAPI app & GraphQL schema (Strawberry)
├── db/
│   └── database.py      # MongoDB connection & ObjectId helpers
├── schemas/
│   ├── fieldsschema.py  # Pydantic models (Artwork & Comment)
│   └── graphschema.py   # GraphQL type definitions (Strawberry)
├── requirements.txt     # Python dependencies
└── README.md            # You're here!
```

---

## 🧑‍🎨 GraphQL Schema Highlights
- **Artwork**
  - `id`, `title`, `description`, `artistName`, `comments`
- **Comment**
  - `id`, `author`, `text`, `artworkId`
- **Queries**
  - `all_artworks`, `artwork_by_id`
- **Mutations**
  - `createArtwork`, `updateArtwork`, `deleteArtwork`
  - `createComment`, `updateComment`, `deleteComment`

See [`schemas/graphschema.py`](schemas/graphschema.py) for full schema.

---

## 🛠️ Getting Started

### 1. Clone & Install

```sh
git clone https://github.com/Amir-hossein-shamsi/Art-gallery-api.git
cd Art-gallery-api
pip install -r requirements.txt
```
---

## 🐳 Run with Docker  

```bash  
docker-compose up --build  
```  

- **API**: [http://localhost:8000](http://localhost:8000)  
- **GraphQL Playground**: [http://localhost:8000/graphql](http://localhost:8000/graphql)  
  - Interact with the API using GraphQL via Apollo Server (enabled by default in development) .  
- **MongoDB**: `localhost:27017`  

---

## 🔧 Local Development  

```bash  
uvicorn main:app --reload  
```  
---

## 📝 Example GraphQL Queries  

### Get All Artworks  
```graphql  
query {  
  all_artworks {  
    id  
    title  
    artistName  
    description  
    comments {  
      author  
      text  
    }  
  }  
}  
```  

### Create an Artwork  
```graphql  
mutation {  
  createArtwork(  
    title: "Starry Night",  
    description: "A masterpiece",  
    artistName: "Vincent"  
  ) {  
    ok  
    artwork {  
      id  
      title  
    }  
  }  
}  
```  
---

## 📦 Tech Stack  

- **FastAPI**: High-performance API framework  
- **Ariadne**: GraphQL schema-first implementation  
- **MongoDB**: NoSQL database for flexible data modeling  
- **Docker**: Containerization for reproducibility  
- **Pydantic**: Data validation and settings management  

---

## 🧩 Key Files  

- `main.py`: App entrypoint and GraphQL resolvers  
- `db/database.py`: MongoDB ObjectId integration  
- `schemas/fieldsschema.py`: Pydantic models for data validation  
- `schemas/graphschema.py`: GraphQL schema definition  

---


## 📜 License  

MIT License  

---

> "Art enables us to find ourselves and lose ourselves at the same time." — Thomas Merton  

--- 
