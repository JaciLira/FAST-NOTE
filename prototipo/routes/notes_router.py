from fastapi import Depends,APIRouter,status

from sqlalchemy.orm import Session

from use_case.notes_use_cases import Notes_Use_Case

from db.deps import get_conection
from db.model import Notes

from schema.notes_schema import Note_Schema,Note_Schema_Output

note_router=APIRouter(prefix="/note",tags=["Notes"])


@note_router.post("/post")
def post_note(note:Note_Schema,db_session:Session= Depends(get_conection)):
    uc = Notes_Use_Case(db_session=db_session)
    uc.post_not(notes=note)
    return status.HTTP_200_OK
    




