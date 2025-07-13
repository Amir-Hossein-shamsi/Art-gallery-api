# 🖼️ Art Gallery API — Type Reference

Welcome to the **Art Gallery API** type documentation!  
This section describes the main types, fields, and relationships in your GraphQL schema, making it easy to understand and explore your collaborative art gallery backend.

---

## 🎨 Types

### `Artwork`
Represents a single piece of art in the gallery.

| Field        | Type      | Description                       | Constraints      |
|--------------|-----------|-----------------------------------|------------------|
| `id`         | `ID!`     | Unique identifier                 | Auto-generated   |
| `title`      | `String!` | Title of the artwork              | **Unique**       |
| `description`| `String`  | Description of the artwork        | Optional         |
| `artistName` | `String!` | Name of the artist                | Required         |
| `comments`   | `[Comment]`| List of comments for this artwork | Related by `artworkId` |

---

### `Comment`
Represents a comment left on an artwork.

| Field        | Type      | Description                       | Constraints      |
|--------------|-----------|-----------------------------------|------------------|
| `id`         | `ID!`     | Unique identifier                 | Auto-generated   |
| `author`     | `String!` | Name of the commenter             | Required         |
| `text`       | `String!` | The comment text                  | Required         |
| `artworkId`  | `ID!`     | The artwork this comment belongs to| Required         |

---

## 🔍 Queries

### `all_artworks: [Artwork]`
Returns a list of all artworks in the gallery.

### `artwork_by_id(id: ID!): Artwork`
Returns a single artwork by its unique ID.

---

## ✏️ Mutations

### `createArtwork(title: String!, description: String, artistName: String!): CreateArtworkPayload`
Creates a new artwork.  
- **title** must be unique.

### `updateArtwork(id: ID!, title: String, description: String, artistName: String): UpdateArtworkPayload`
Updates an existing artwork.

### `deleteArtwork(id: ID!): DeleteArtworkPayload`
Deletes an artwork.

### `createComment(artworkId: ID!, author: String!, text: String!): CreateCommentPayload`
Adds a comment to an artwork.

### `updateComment(id: ID!, author: String, text: String): UpdateCommentPayload`
Updates a comment.

### `deleteComment(id: ID!): DeleteCommentPayload`
Deletes a comment.

---

## 🧩 Example Type Usage

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

---

## 🛡️ Constraints & Indexes

- **Artwork.title** is unique (enforced at the database level).
- All IDs are MongoDB ObjectIds, returned as strings.

---

## 🚀 Getting Started

To run the Cosmic Canvas API locally with Docker Compose:

```bash
docker-compose up --build
```

- The API will be available at [http://localhost:8000/graphql](http://localhost:8000/graphql).
- MongoDB and Redis services are started automatically.

---

## 🛠️ Technologies Used

- **FastAPI** — High-performance Python web framework.
- **GraphQL (Ariadne)** — Flexible API query language.
- **MongoDB** — NoSQL database for storing artworks and comments.
- **Redis** — In-memory cache for fast query responses.
- **Docker Compose** — Easy orchestration of multi-service environments.

---

## 🧑‍💻 Development Tips

- **Hot Reload:** The API service mounts your code for instant updates.
- **Database Indexes:** Unique indexes are created for artwork titles at startup.
- **Caching:** Frequently accessed queries are cached in Redis for performance.
- **Error Handling:** Duplicate artwork titles return a friendly error message.

---

## 🗂️ Folder Structure

```
.
├── main.py                # FastAPI & GraphQL entrypoint
├── schemas/               # Pydantic and GraphQL schema definitions
├── db/                    # Database utilities
├── Dockerfile             # API container build instructions
├── docker-compose.yml     # Multi-service orchestration
└── README.md              # Project documentation
```

---

## 🌐 API Playground

Visit `/graphql` in your browser for an interactive GraphQL playground.  
Try out queries and mutations, inspect types, and explore relationships.

---

## 💡 Contributing

Pull requests and issues are welcome!  
Please follow the code style and add tests for new features.

---

## 📄 License

This project is licensed under the MIT License.

---

> "Art enables us to find ourselves and lose ourselves at the same time." — Thomas Merton

---