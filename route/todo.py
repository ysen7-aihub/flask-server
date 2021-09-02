from flask import request
from flask_restx import Resource, Api, Namespace, fields

todos = {}
count = 1

Todo = Namespace(name='Todos',
                 description="Todo 리스트를 작성하기 위해 사용하는 API")

todo_fields = Todo.model('Todo', {  # Model 객체 생성
    'data': fields.String(description='a Todo', required=True, example="what to do")
})

todo_fields_with_id = Todo.inherit('Todo With ID', todo_fields, {  # todo_fields 상속 받음
    'todo_id': fields.Integer(description='a Todo ID')
})

@Todo.route('/')
class TodoPost(Resource):
    @Todo.expect(todo_fields) # 특정 스키마가 들어올 것을 기대한다. 모델 등록
    @Todo.response(201, 'Success', todo_fields_with_id) # 특정 스키마가 반환된다.
    def post(self):
        """Todo 리스트에 할 일을 등록합니다."""
        global count
        global todos

        idx = count
        count += 1
        todos[idx] = request.json.get('data')

        return {
            'todo_id': idx,
            'data': todos[idx]
        }


@Todo.route('/<int:todo_id>')
@Todo.doc(params={'todo_id': 'An ID'}) # 설명 추가
class TodoSimple(Resource):
    def get(self, todo_id):
        """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 가져옵니다."""
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }
    @Todo.doc(response={202:'Success'})
    @Todo.doc(response={500:'Failed'})
    def put(self, todo_id):
        """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 수정합니다."""
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }, 202

    def delete(self, todo_id):
        """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 삭제합니다."""
        del todos[todo_id]
        return {
            "delete": "success"
        }, 202