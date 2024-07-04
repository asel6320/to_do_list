def task_validate(task):
    errors = {}
    if not task.description:
        errors["description"] = "Task is mandatory"
    elif len(task.description) > 3:
        errors["description"] = "The length of this field should be less than 50"


    if not task.deadline:
        errors["deadline"] = "Deadline is mandatory"

    return errors