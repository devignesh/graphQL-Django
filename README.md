# graphQL-Django

This is simple blog post app using django and graphQL, We design an api schema for blogpost and comment. 

In graphQL Queries and mutation for getting data and changing data in server.

Graphene we can use Django to create GraphQL APIs.

--------------------------------------------------------

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
        updatedAt
        commentSet {
            id
            comment
        }

    }
    }
    
    # Response
    
            {
          "data": {
            "blogpostall": [
              {
                "id": "1",
                "author": "vignesh",
                "title": "Python Django",
                "description": "Sample Blog",
                "publishedDate": "2020-03-03T02:31:22+00:00",
                "updatedAt": null,
                "commentSet": [
                  {
                    "id": "13",
                    "comment": "comment"
                  },
                  {
                    "id": "3",
                    "comment": "Third comment"
                  }
                ]
              },
              {
                "id": "2",
                "author": "vicky",
                "title": "Django graphQL",
                "description": "Django testing",
                "publishedDate": "2020-03-02T21:04:18.194415+00:00",
                "updatedAt": null,
                "commentSet": [
                  {
                    "id": "19",
                    "comment": "test"
                  },
                  {
                    "id": "16",
                    "comment": "vv"
                  },
                  {
                    "id": "15",
                    "comment": "vv"
                  },
                  {
                    "id": "14",
                    "comment": "vv"
                  },
                  {
                    "id": "12",
                    "comment": "value"
                  },
                  {
                    "id": "5",
                    "comment": "File performance"
                  },
                  {
                    "id": "4",
                    "comment": "Mannual data"
                  }
                ]
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
    
    # Response 
                {
          "data": {
            "createBlog": {
              "createblogpost": {
                "id": "8",
                "author": "vickykumar",
                "title": "test create blog",
                "description": "test blog description",
                "publishedDate": "2020-03-03T06:56:12.902488+00:00"
                "updatedAt": null
              }
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
