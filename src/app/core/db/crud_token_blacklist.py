from app.crud.crud_base import CRUDBase
from app.core.db.token_blacklist import TokenBlacklist
from app.core.schemas import TokenBlacklistCreate, TokenBlacklistUpdate

CRUDTokenBlacklist = CRUDBase[TokenBlacklist, TokenBlacklistCreate, TokenBlacklistUpdate, TokenBlacklistUpdate, None]
crud_token_blacklist = CRUDTokenBlacklist(TokenBlacklist)
