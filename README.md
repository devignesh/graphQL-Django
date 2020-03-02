# graphQL-Django

This is simple blog post app using django and graphQL, We design an api schema for blogpost and comment. 

In graphQL Queries and mutation for getting data and changing data in server.

Graphene we can use Django to create GraphQL APIs.

----------------------------------------------------------

# Start the project

Clone the repository :

1: git clone git@github.com:devignesh/graphQL-Django.git

2: cd graphQL-Django

    I. pipenv shell   

    II. pipenv install

    III. cd blog  # app name

3: python manage.py makemigrations  

4: python mange.py migrate

5: python mange.py runserver  

6: http://127.0.0.1:8000/graphql/    #open in your browser


----------------------------------------------------------


# queries

To get all the blog post 
----------------------------------------------------------

    query {
    blogpostall {
        id
        author
        title
        description
        publishedDate
        updatedAt
    }
    }

To get the blogpost with Comments
----------------------------------------------------------

    query {
    blogpostall {
        id
        author
        title
        description
        publishedDate
        commentSet {
        
        id
        comment
        }

    }
    }

Query for get the particular blogpost and comments based on its ID 
---------------------------------------------------------------------

    query {
    blogs(id:1) {
        id
        author
        title
        description
        publishedDate
        commentSet {
        
        id
        comment
        }

    }
    }


# Mutation 

Create a new blog post mutation 
----------------------------------------------------------

    mutation {
    createBlog (author:"vigneshkumar", title:"Test blog", description:"test description") {
        
        createblogpost {
        id
        author
        title
        description
        publishedDate
        updatedAt
        }
    }
    }

Update a existing blog post based on  blog ID,
----------------------------------------------------------

    mutation {
    updateblog (blogId:7, author:"updated", title:"updated title", description:"updated desc") {
        blogupdate {
        id
        author
        title
        description
        publishedDate
        updatedAt
        }
    }
    }

Create a New comment 
----------------------------------------------------------

    mutation {
    createcomment (author:"updated", comment:"test comment") {
        createcommentpost {
        id
        comment
        author {
            id
        }
    }
    }
    }

Delete a existing comment based on comment ID
----------------------------------------------------------

    mutation {
    deletecomment(commentId:1) {
        commentId
    }
    }
