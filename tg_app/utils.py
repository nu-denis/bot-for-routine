def get_last_message_id_by_chat_id(last_updates):
    res = {}
    for upd in last_updates:
        print('upd.message\n\n', upd.message)
        if not upd.message:
            continue
        chat_info = upd.message.chat
        chat_id = chat_info.id
        message_id = upd.message.id
        if chat_id not in res:
            res[chat_id] = message_id
        else:
            res[chat_id] = max(message_id, res[chat_id])
    return res
