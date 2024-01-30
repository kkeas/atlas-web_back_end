#!/usr/bin/env Python3

"""session authorization class"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """validate if everything inherits correctly without any overloading
        validate the “switch” by using environment variables"""

    user_id_by_session_id = {}
    
    def create_session(self, user_id=None):
        """create a session"""

        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        SessionAuth.user_id_by_session_id[user_id] = session_id

        return session_id
