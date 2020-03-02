import graphene
import blogapp.schema

# Query for getting the data from the server.
class Query(blogapp.schema.Query, graphene.ObjectType):
    pass

# Mutation for Updating server data's
class Mutation(blogapp.schema.Mutation, graphene.ObjectType):
    pass

# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)