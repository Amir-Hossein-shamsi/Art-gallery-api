type_defs = """
    type Artwork {
        id: String!
        title: String!
        description: String
        artistName: String!
        comments: [Comment!]!
    }

    type Comment {
        id: String!
        author: String!
        text: String!
        artworkId: String!
    }

    type Query {
        all_artworks: [Artwork!]!
        artwork_by_id(id: String!): Artwork
    }

    type Mutation {
        createArtwork(title: String!, description: String, artistName: String!): CreateArtworkResult!
        createComment(artworkId: String!, author: String!, text: String!): CreateCommentResult!
        updateArtwork(id: String!, title: String, description: String, artistName: String): UpdateArtworkResult!
        deleteArtwork(id: String!): DeleteArtworkResult!
        updateComment(id: String!, author: String, text: String): UpdateCommentResult!
        deleteComment(id: String!): DeleteCommentResult!
    }

    type CreateArtworkResult {
        ok: Boolean!
        artwork: Artwork
    }

    type CreateCommentResult {
        ok: Boolean!
        comment: Comment
    }
    
     type UpdateArtworkResult {
        ok: Boolean!
        artwork: Artwork
    }

    type DeleteArtworkResult {
        ok: Boolean!
    }

    type UpdateCommentResult {
        ok: Boolean!
        comment: Comment
    }

    type DeleteCommentResult {
        ok: Boolean!
    }
    
"""