from marshmallow import Schema, fields, base


"""
This module aims at providing the request and response format for the various api calls.
This also helpful for creating swagger docs for apis testing.
"""
class APIResponse(Schema):
    message = fields.String(default="Success")

class SignUpRequest(Schema):
    username = fields.String(default="username")
    password = fields.String(default="password")
    name = fields.String(default="name")
    is_admin = fields.Integer(default="0")

class LoginRequest(Schema):
    username = fields.String(default="username")
    password = fields.String(default="password")

class LogoutRequest(Schema):
    session_id = fields.String(default="session_id")

class QuestionsRequest(Schema):
    session_id = fields.String(default="session_id")

class ListQuestionsResponse(Schema):
    questions = fields.List(fields.Dict())

class AddQuestionRequest(Schema):
    session_id = fields.String(default="session_id")
    question = fields.String(default="question")
    choice1 = fields.String(default="choice1")
    choice2 = fields.String(default="choice2")
    choice3 = fields.String(default="choice3")
    choice4 = fields.String(default="choice4")
    marks = fields.Integer(default=0)
    remarks = fields.String(default="remarks")
    answer = fields.Integer(default=0)

class CreateQuizRequest(Schema):
    session_id = fields.String(default="session_id")
    quiz_name = fields.String(default="quiz_name")
    question_ids = fields.List(fields.String)

class AssignQuizRequest(Schema):
    session_id = fields.String(default="session_id")
    quiz_id = fields.String(default="quiz_id")
    user_id = fields.String(default="user_id")

class ViewQuizRequest(Schema):
    session_id = fields.String(default="session_id")
    quiz_id = fields.String(default="quiz_id")

class ViewQuizResponse(Schema):
    questions = fields.List(fields.Dict())

class AssignedQuizRequest(Schema):
    session_id = fields.String(default="session_id")

class AssignedQuizResponse(Schema):
    quiz_info = fields.List(fields.Dict())

class ViewAllQuizRequest(Schema):
    session_id = fields.String(default="session_id")

class ViewAllQuizResponse(Schema):
    quiz_info = fields.List(fields.Dict())

class AttemptQuizRequest(Schema):
    session_id = fields.String(default="session_id")
    quiz_id = fields.String(default="quiz_id")
    responses = fields.List(fields.Dict())

class AttemptQuizResponse(Schema):
    score_achieved = fields.Integer(default=0)

class QuizResultRequest(Schema):
    session_id = fields.String(default="session_id")
    quiz_id = fields.String(default="quiz_id")

class QuizResultResponse(Schema):
    results = fields.List(fields.Dict())