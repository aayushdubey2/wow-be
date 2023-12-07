from flask_restx import fields
from .extensions import api

query_model = api.model('Category', {
    'query': fields.String
})

query_model_output = api.model('Project', {
    'output': fields.String
})

category_model = api.model('Category', {
    'category_id': fields.Integer,
    'name': fields.String
})

project_model = api.model('Project', {
    'project_id': fields.Integer,
    'name': fields.String,
    'categories': fields.List(fields.Nested(category_model))
})

customer_info_model = api.model('CustomerInfo', {
    'full_name': fields.String,
    'email': fields.String,
    'type': fields.String
})

role_model = api.model('Role', {
    'role_id': fields.Integer,
    'role_name': fields.String
})

user_model = api.model( 'User', {
    'user_id': fields.Integer,
    'firstName': fields.String,
    'lastName': fields.String,
    'email': fields.String,
    'role_id': fields.Integer
})

chat_model = api.model( 'Chat', {
    'chat_id': fields.Integer,
    'user_id': fields.Integer,
    'modified_at': fields.DateTime
})

message_model = api.model('Message', {
    'message_id': fields.Integer,
    'text': fields.String,
    'timestamp': fields.DateTime,
    'type': fields.String,
    'chat_id': fields.Integer,
    'modified_at': fields.DateTime
})

# API models for request payload
project_input_model = api.model('ProjectInput', {
    'name': fields.String(required=True)
})

category_input_model = api.model('CategoryInput', {
    'name': fields.String(required=True)
})

# API models for response payload
project_output_model = api.model('ProjectOutput', {
    'project_id': fields.Integer,
    'name': fields.String,
    'modified_at': fields.DateTime
})

category_output_model = api.model('CategoryOutput', {
    'category_id': fields.Integer,
    'name': fields.String,
    'modified_at': fields.DateTime
})


user_project_input_model = api.model('UserProjectInput', {
    'user_id': fields.Integer(required=True),
    'project_id': fields.Integer(required=True)
})

# API model for response payload
user_project_output_model = api.model('UserProjectOutput', {
    'user_project_id': fields.Integer,
    'user_id': fields.Integer,
    'project_id': fields.Integer,
    'modified_at': fields.DateTime
})

project_category_input_model = api.model('ProjectCategoryInput', {
    'project_id': fields.Integer(required=True),
    'category_id': fields.Integer(required=True)
})

project_category_output_model = api.model('ProjectCategoryOutput', {
    'project_category_id': fields.Integer,
    'project_id': fields.Integer,
    'category_id': fields.Integer,
    'modified_at': fields.DateTime
})

user_category_permission_input_model = api.model('UserCategoryPermissionInput', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'category_id': fields.Integer(required=True, description='Category ID'),
    'project_id': fields.Integer(required=True, description='Project ID'),
})

user_category_permission_output_model = api.model('UserCategoryPermissionOutput', {
    'user_category_permission_id': fields.Integer(description='User Category Permission ID'),
    'user_id': fields.Integer(description='User ID'),
    'category_id': fields.Integer(description='Category ID'),
    'project_id': fields.Integer(description='Project ID'),
    'modified_at': fields.DateTime(description='Modified At'),
})

