music_session = {
    "version": "1",
    "session_id": "1",
    "participants" : {
        "Summer" : {
            "websocket": websocket,
            "persona": "singer"
        },
        "Weijia": {
            "websocket": websocket,
            "persona": "producer"
        }
    }
}


# Register a connection
register_connection_data = {
    "version": "1",
    "session_id": "1",
    "type": "register", # register, connect
    "value": "Summer Fang"
}

# Sign up a user
signup_data = {
    "version": "1",
    "sessionn_id": "1",
    "name": "Summer Fang",
    "password": "xyz1999"
}
