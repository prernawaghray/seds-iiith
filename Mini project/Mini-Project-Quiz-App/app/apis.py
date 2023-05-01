from app.models import *
from app import *
from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from app.schemas import *
from app.services import *

"""
[Sign Up API] : Its responsibility is to perform the signup activity for the user.
"""
#  Restful way of creating APIs through Flask Restful
class SignUpAPI(MethodResource, Resource):
    @doc(description='Sign Up API)', tags=['SignUp API'])
    @use_kwargs(SignUpRequest, location='json')
    @marshal_with(APIResponse)
    def post(self, **kwargs):
        try:
            create_user(**kwargs)
            return APIResponse().dump(dict(message='User is successfully registered')), 200

        except Exception as err:
            return APIResponse().dump(dict(message=f'Not able to register user : {str(err)}')), 400

api.add_resource(SignUpAPI, '/signup')
docs.register(SignUpAPI)

"""
[Login API] : Its responsibility is to perform the login activity for the user and 
create session id which will be used for all subsequent operations.
"""
class LoginAPI(MethodResource, Resource):
    @doc(description='Login API', tags=['Login API'])
    @use_kwargs(LoginRequest, location='json')
    @marshal_with(APIResponse)
    def post(self, **kwargs):
        try:
            is_logged_in, session_id = login_user(**kwargs)
            if is_logged_in:
            # user = UserMaster.query.filter_by(username=kwargs['username'], password=kwargs['password']).first()
            # if user:
            #     print('logged in')
            #     session['user_id'] = user.id
            #     print(f'User_id : {str(session["user_id"])}')
                return APIResponse().dump(dict(message='User is successfully logged in')), 200
            else:
                return APIResponse().dump(dict(message='User not found')), 404
        except Exception as e:
            print(str(e))
            return APIResponse().dump(dict(message=f'Not able to login user : {str(e)}')), 400


api.add_resource(LoginAPI, '/login')
docs.register(LoginAPI)

"""
[Logout API] : Its responsibility is to perform the logout activity for the user.
"""
class LogoutAPI(MethodResource, Resource):
    @doc(description='Logout API', tags=['Logout API'])
    @use_kwargs(LogoutRequest, location='json')
    @marshal_with(APIResponse)
    def post(self, **kwargs):
        try:
            is_logged_out = logout_user(kwargs['session_id'])
            if is_logged_out:
                return APIResponse().dump(dict(message='User is successfully logged out')), 200
            else:
                return APIResponse().dump(dict(message='User is not logged in')), 401
        except Exception as err:
            return APIResponse().dump(dict(message=f'Not able to logout user : {str(err)}')), 400

api.add_resource(LogoutAPI, '/logout')
docs.register(LogoutAPI)


"""
[Add Question API] : Its responsibility is to add question to the question bank.
Admin has only the rights to perform this activity.
"""

class AddQuestionAPI(MethodResource, Resource):
    @doc(description='Add Question API', tags=['Question'])
    @use_kwargs(AddQuestionRequest, location='json')
    @marshal_with(APIResponse)
    def post(self, **kwargs):
        try:
            is_active, user_id = check_if_session_is_active(kwargs['session_id'])
            if not is_active:
                return APIResponse().dump(dict(message='User is not logged in')), 404
            is_admin = check_if_admin(user_id)
            if not is_admin:
                return APIResponse().dump(dict(message='Logged in user is not have admin Rights')), 401
            add_question(**kwargs)
            return APIResponse().dump(dict(message='question is successfully added')), 200
        except Exception as err:
            return APIResponse().dump(dict(message=f' Not able to add question : {str(err)}')), 400

api.add_resource(AddQuestionAPI, '/add.question')
docs.register(AddQuestionAPI)

"""
[List Questions API] : Its responsibility is to list all questions present actively in the question bank.
Here only Admin can access all the questions.
"""
class ListQuestionAPI(MethodResource, Resource):
    @doc(description='List Question API', tags=['Question'])
    @use_kwargs(QuestionsRequest, location='json')
    @marshal_with(ListQuestionsResponse)
    def post(self, **kwargs):
        try:
            is_active, user_id = check_if_session_is_active(kwargs['session_id'])
            print(is_active, user_id)
            if not is_active:
                return APIResponse().dump(dict(message='User is not logged in')), 404
            is_admin = check_if_admin(user_id)
            if not is_admin:
                return APIResponse().dump(dict(message='Logged in user is not have admin Rights')), 401
            questions_list = list_questions()
            return ListQuestionsResponse().dump(dict(questions=questions_list)), 200
        except Exception as err:
            return APIResponse().dump(dict(message=f' Not able to List question : /n{str(err)}')), 400

api.add_resource(ListQuestionAPI, '/list.questions')
docs.register(ListQuestionAPI)

"""
[Create Quiz API] : Its responsibility is to create quiz and only admin can create quiz using this API.
"""
class CreateQuizAPI(MethodResource, Resource):
    @doc(description='Create Quiz API', tags=['Quiz'])
    @use_kwargs(CreateQuizRequest, location='json')
    @marshal_with(APIResponse)
    def post(self, **kwargs):
        try:
            is_active, user_id = check_if_session_is_active(kwargs['session_id'])
            if not is_active:
                return APIResponse().dump(dict(message='User is not logged in')), 404
            else:
                is_admin = check_if_admin(user_id)
                if is_admin:
                    create_quiz(**kwargs)
                    if create_quiz:
                        return APIResponse().dump(dict(message='Quiz has been created successfully')), 201
                    else:
                        return APIResponse().dump(dict(message="Please check the input credentials & try again.")), 400
                else:
                    return APIResponse().dump(dict(message='Logged in user does not have admin Rights')), 401
        except Exception as err:
            return APIResponse().dump(dict(message=f' Not able to create question : /n{str(err)}')), 400

api.add_resource(CreateQuizAPI, '/create.quiz')
docs.register(CreateQuizAPI)

"""
[Assign Quiz API] : Its responsibility is to assign quiz to the user. Only Admin can perform this API call.
"""
class AssignQuizAPI(MethodResource, Resource):
    @doc(description='Assign Quiz API', tags=['Quiz'])
    @use_kwargs(AssignQuizRequest, location='json')
    @marshal_with(APIResponse)
    def post(self, **kwargs):
        try:
            is_active, user_id = check_if_session_is_active(kwargs['session_id'])
            if not is_active:
                return APIResponse().dump(dict(message='User is not logged in')), 404
            else:
                is_admin = check_if_admin(user_id)
                if is_admin:
                    assign_quiz(**kwargs)
                    if assign_quiz:
                        return APIResponse().dump(dict(message='Quiz has been assigned successfully')), 201
                    else:
                        return APIResponse().dump(dict(message="Please check the input credentials & try again.")), 400
                else:
                    return APIResponse().dump(dict(message='Logged in user does not have admin Rights')), 401
        except Exception as err:
            return APIResponse().dump(dict(message=f' Not able to Assign Quiz to User : /n{str(err)}')), 400

api.add_resource(AssignQuizAPI, '/assign.quiz')
docs.register(AssignQuizAPI)

"""
[View Quiz API] : Its responsibility is to view the quiz details.
Only Admin and the assigned users to this quiz can access the quiz details.
"""
class ViewQuizAPI(MethodResource, Resource):
    @doc(description='View Quiz API', tags=['Quiz'])
    @use_kwargs(ViewQuizRequest, location='json')
    @marshal_with(ViewQuizResponse)
    def post(self, **kwargs):
        try:
            is_active, user_id = check_if_session_is_active(kwargs['session_id'])
            print(is_active, user_id)
            if not is_active:
                return APIResponse().dump(dict(message='User is not logged in')), 404
            print('Checking')
            has_access = check_quiz_access(kwargs['quiz_id'], user_id)
            print(has_access)
            if not has_access:
                return APIResponse().dump(dict(message='user have no access for the requested quiz')), 401
            questions = view_quiz(**kwargs)
            return ViewQuizResponse().dump(dict(questions=questions)), 200
        except Exception as err:
            print(str(err))
            return APIResponse().dump(dict(message=f'Error in accessing quiz: {str(err)}')), 400

api.add_resource(ViewQuizAPI, '/view.quiz')
docs.register(ViewQuizAPI)

"""
[View Assigned Quiz API] : Its responsibility is to list all the assigned quizzes 
                            with there submittion status and achieved scores.
"""
class ViewAssignedQuizAPI(MethodResource, Resource):
    @doc(description='View Assigned Quiz API', tags=['Quiz'])
    @use_kwargs(AssignedQuizRequest, location='json')
    @marshal_with(AssignedQuizResponse)
    def post(self, **kwargs):
        try:
            is_active, user_id = check_if_session_is_active(kwargs['session_id'])
            if not is_active:
                return APIResponse().dump(dict(message='User is not logged in')), 404
            quiz_info = get_assigned_quiz_info(user_id)
            if len(quiz_info) == 0:
                return APIResponse().dump(dict(message='No quiz is assigned to the user')), 401
            return AssignedQuizResponse().dump(dict(quiz_info=quiz_info)), 200
        except Exception as err:
            return APIResponse().dump(dict(message=f'Error in accessing quiz info: {str(err)}')), 400

api.add_resource(ViewAssignedQuizAPI, '/assigned.quizzes')
docs.register(ViewAssignedQuizAPI)


"""
[View All Quiz API] : Its responsibility is to list all the created quizzes. Admin can only list all quizzes.
"""
class ViewAllQuizAPI(MethodResource, Resource):
    @doc(description='View All Quiz API', tags=['Quiz'])
    @use_kwargs(ViewAllQuizRequest, location='json')
    @marshal_with(ViewAllQuizResponse)
    def post(self, **kwargs):
        try:
            is_active, user_id = check_if_session_is_active(kwargs['session_id'])
            if not is_active:
                return APIResponse().dump(dict(message='User is not logged in')), 404
            is_admin = check_if_admin(user_id)
            if not is_admin:
                return APIResponse().dump(dict(message='Logged in user is not have admin Rights')), 401
            quiz_info = get_all_quiz_info(user_id)
            if len(quiz_info) == 0:
                return APIResponse().dump(dict(message='No quiz is available to view')), 401
            return ViewAllQuizResponse().dump(dict(quiz_info=quiz_info)), 200
        except Exception as err:
            return APIResponse().dump(dict(message=f'Error in accessing quiz info: {str(err)}')), 400

api.add_resource(ViewAllQuizAPI, '/all.quizzes')
docs.register(ViewAllQuizAPI)

"""
[Attempt Quiz API] : Its responsibility is to perform quiz attempt activity by 
                        the user and the score will be shown as a result of the submitted attempt.
"""
class AttemptQuizAPI(MethodResource, Resource):
    @doc(description='Attempt Quiz API', tags=['Quiz'])
    @use_kwargs(AttemptQuizRequest, location='json')
    @marshal_with(AttemptQuizResponse)
    def post(self, **kwargs):
        try:
            is_active, user_id = check_if_session_is_active(kwargs['session_id'])
            if not is_active:
                return APIResponse().dump(dict(message='User is not logged in')), 404
            has_access = check_quiz_access(kwargs['quiz_id'], user_id)
            if not has_access:
                return APIResponse().dump(dict(message='user have no access for the requested quiz')), 401
            score_achieved = attempt_quiz(user_id, kwargs['quiz_id'], kwargs['responses'],
                                          kwargs['question_id'])  # missed code
            return AttemptQuizResponse().dump(dict(score_achieved=score_achieved)), 200
        except Exception as err:
            print(str(err))
            return APIResponse().dump(dict(message=f'Error in attempting the given quiz: {str(err)}')), 400

api.add_resource(AttemptQuizAPI, '/attempt.quiz')
docs.register(AttemptQuizAPI)

"""
[Quiz Results API] : Its responsibility is to provide the quiz results in which the users 
                        having the scores sorted in descending order are displayed, 
                        also the ones who have not attempted are also shown.
                        Admin has only acess to this functionality.
"""
class QuizResultAPI(MethodResource, Resource):
    @doc(description='Quiz Result API', tags=['Quiz'])
    @use_kwargs(QuizResultRequest, location=('json'))
    @marshal_with(QuizResultResponse)
    def post(self, **kwargs):
        try:
            is_active, user_id = check_if_session_is_active(kwargs['session_id'])
            if not is_active:
                return APIResponse().dump(dict(message='user is not logged in.')), 404
            is_admin = check_if_admin(user_id)
            if not is_admin:
                return APIResponse().dump(dict(message="user is not admin")), 401
            results = quiz_results(kwargs['quiz_id'])
            if len(results) == 0:
                return APIResponse().dump(dict(message="No result for the quiz is available")), 405
            return QuizResultResponse().dump(dict(results=results)), 200
        except Exception as err:
            print(str(err))
            return APIResponse().dump(dict(message=f' Not able to add question : {str(err)}')), 400

api.add_resource(QuizResultAPI, '/quiz.results')
docs.register(QuizResultAPI)


