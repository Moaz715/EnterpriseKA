


class User():
    __tablename__ = "users"
    
    id: int
    email: str
    hashed_pasword: str