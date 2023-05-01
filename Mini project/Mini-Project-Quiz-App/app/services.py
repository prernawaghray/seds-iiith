from sqlalchemy.orm.session import sessionmaker
from app.models import QuestionMaster, QuizInstance, QuizMaster, QuizQuestions, UserMaster, UserResponses, UserSession
from app import db
import uuid
from flask import session
import datetime
from typing import List

"""
[Services Module] Implement various helper functions here as a part of api
                    implementation using MVC Template
"""
def create_user(**kwargs):
    try:
        user = UserMaster(
            uuid.uuid4(),
            kwargs['name'],
            kwargs['username'],
            kwargs['password'],
            kwargs['is_admin']
        )

        db.session.add(user)
        db.session.commit()
    except Exception as err:
        raise err

def login_user(**kwargs):
    try:
        user = UserMaster.query.filter_by(username=kwargs['username'], password=kwargs['password'])
        if user:
            print('user logged in')
            is_active, session_id = check_user_session_is_active(user.id)
            if not is_active:
                session_id = uuid.uuid4()
                user_session = UserSession(uuid.uuid4(), user.id, session_id)
                db.session.add(user_session)
                db.session.commit()
            else:
                session['session_id'] = session_id
            session['session_id'] = session_id
            return True, session_id
        else:
            return False, None
    except Exception as err:
        raise err

def check_user_session_is_active(user_id):
    try:
        user_session = UserSession.query.filter_by(user_id=user_id, is_active=1).first()
        if user_session:
            return True, user_session
        else:
            return False, None
    except Exception as err:
        raise err

def logout_user(session_id):
    try:
        session_id = UserSession.query.filter_by(session_id=session_id, is_active=1).first()
        if session_id:

            session_id.is_active = 0  # instead of deleting record make session inactive
            session_id.updated_ts = datetime.utcnow()
            db.session.commit()
            return True

        else:
            return

    except Exception as err:
        raise err


def check_if_session_is_active(session_id):
    try:
        user_id = UserSession.query.filter_by(session_id=session_id, is_active=1).first().user_id
        if not user_id:
            return False, None
        else:
            return True, user_id

    except Exception as err:
        raise err


def check_if_admin(user_id):
    try:
        user_check = UserMaster.query.filter_by(id=user_id, is_admin=1).first()
        if not user_check:
            return False
        else:
            return True
    except Exception as err:
        raise err

def add_question(**kwargs):
    try:
        question = QuestionMaster(
            uuid.uuid4(),
            kwargs['question'],
            kwargs['choice1'],
            kwargs['choice2'],
            kwargs['choice3'],
            kwargs['choice4'],
            kwargs['answer'],
            kwargs['marks'],
            kwargs['remarks']

        )
        db.session.add(question)
        db.session.commit()
    except Exception as err:
        raise err

def list_questions():
    try:
        questions = QuestionMaster.query.all()
        question_list = list()
        for question in questions:
            question_dict = dict()
            question_dict['id'] = question.id
            question_dict['question'] = question.question
            question_dict['choice1'] = question.choice1
            question_dict['choice2'] = question.choice2
            question_dict['choice3'] = question.choice3
            question_dict['choice4'] = question.choice4
            question_dict['answer'] = question.answer
            question_dict['marks'] = question.marks
            question_dict['remarks'] = question.remarks

            question_list.append(question_dict)
        return question_list

    except Exception as err:
        raise err

def create_quiz(**kwargs):
    try:
        quizname = QuizMaster(
            uuid.uuid4(),
            kwargs['quiz_name']
            )
        db.session.add(quizname)
        # if list_questions():
        #     question_id = QuestionMaster.query.filterby(id=kwargs['question_ids'])
        #
        #     # question_id = list(question_id)
        for question_list in kwargs['question_ids']:
                # question_list = list(question_list)
                quesadd = QuizQuestions(
                    uuid.uuid4(),
                    quizname.id,
                    question_list
                 )
                db.session.add(quesadd)
                # question_dict['id'] = question.id

        db.session.commit()
        return True
    except Exception as err:
        raise err

def assign_quiz(**kwargs):
    try:
        assnquiz = QuizInstance(
            uuid.uuid4(),
            kwargs['quiz_id'],
            kwargs['user_id']
        )
        db.session.add(assnquiz)
        db.session.commit()
        return True
    except Exception as err:
        raise err


def check_quiz_access(quiz_id, user_id):
    try:
        quiz_id = QuizInstance.query.filter_by(user_id=user_id, quiz_id=quiz_id, is_active=1).first().quiz_id
        if quiz_id:
            print(quiz_id)
            return True
        else:
            print('not logged in')
            return False
    except Exception as err:
        raise err

def view_quiz(**kwargs):
    try:
        get_quesid = QuizQuestions.query.filter_by(quiz_id=kwargs["quiz_id"],is_active=1)
        question_list = list()
        for question in get_quesid:
            questions = QuestionMaster.query.filter_by(id=question.question_id).first()
            question_dict = dict()
            question_dict['question'] = questions.question
            question_list.append(question_dict)
        return question_list
    except Exception as err:
        raise err

def get_all_quiz_info(user_id):
    try:
        get_quizid = QuizInstance.query.all()
        print(get_quizid)
        quiz_list = list()
        for quiz1 in get_quizid:
            quiz = QuizInstance.query.filter_by(quiz_id=quiz1.quiz_id).first()
            quiz2 = QuizMaster.query.filter_by(id=quiz1.quiz_id).first()
            quiz3 = UserMaster.query.filter_by(id=quiz1.user_id).first()
            quiz_dict = dict()
            quiz_dict['User_Name'] = quiz3.name
            quiz_dict['Quiz_Name'] = quiz2.quiz_name
            quiz_dict['quiz'] = quiz.quiz_id
            quiz_dict['Score_achieved'] = quiz.score_achieved
            quiz_dict['Submit_Status'] = quiz.is_submitted
            quiz_list.append(quiz_dict)
        return quiz_list
    except Exception as err:
        raise err

def get_assigned_quiz_info(user_id):
    try:
        get_quizid = QuizInstance.query.filter_by(user_id=user_id,is_active=1)
        print(get_quizid)
        quiz_list = list()
        for quiz1 in get_quizid:
            quiz = QuizInstance.query.filter_by(quiz_id=quiz1.quiz_id).first()
            quiz_dict = dict()
            quiz_dict['quiz'] = quiz.quiz_id
            quiz_dict['Score_achieved'] = quiz.score_achieved
            quiz_dict['Submit_Status'] = quiz.is_submitted
            quiz_list.append(quiz_dict)
        return quiz_list
    except Exception as err:
        raise err

def attempt_quiz():
    try:
