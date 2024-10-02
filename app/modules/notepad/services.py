from app.modules.notepad.repositories import NotepadRepository
from core.services.BaseService import BaseService
from app.modules.notepad.models import Notepad
from core.repositories.BaseRepository import BaseRepository

class NotepadService(BaseService):
    def __init__(self):
        super().__init__(NotepadRepository())

    def get_all_by_user(self, user_id):
        return self.repository.get_all_by_user(user_id)
    
    
    
class NotepadRepository(BaseRepository):
    def __init__(self):
        super().__init__(Notepad)

    def get_all_by_user(self, user_id):
        return Notepad.query.filter_by(user_id=user_id).all()

