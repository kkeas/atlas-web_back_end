#!/usr/bin/env Python3

"""session authorization class"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """validate if everything inherits correctly without any overloading
        validate the “switch” by using environment variables"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create a session"""

        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Method for retrieving a User ID by session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
