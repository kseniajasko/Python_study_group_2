from flask import Blueprint, request, abort, jsonify

from .models import Task

from ..utils.binary_search import binary_search

bp = Blueprint('task', __name__)

@bp.route('/', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        data = request.get_json(force=True)
        new_task = Task(**data)
        return new_task.to_json()
    return Task.list_to_json()

@bp.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@bp.route('/<int:task_id>')
def task_detail(task_id):
    # HW
    temp_id = binary_search(Task.task_id, task_id)

    if temp_id:
        for task in Task.objects:
            if task.id == task_id:
                return task.to_json()
    else:
        return abort(404, description="Task ID not found")

