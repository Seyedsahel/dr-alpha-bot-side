appointment_states = {}


def set_state(chat_id, step, data=None):

    chat_id = str(chat_id)
    state = appointment_states.get(chat_id, {})
    state["step"] = step

    if data:
        state.update(data)

    appointment_states[chat_id] = state


def get_state(chat_id):
    return appointment_states.get(str(chat_id))


def clear_state(chat_id):
    appointment_states.pop(str(chat_id), None)


def is_in_appointment_flow(chat_id):
    return str(chat_id) in appointment_states