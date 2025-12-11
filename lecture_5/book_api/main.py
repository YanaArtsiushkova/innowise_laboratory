from typing import List, Optional 
from fastapi import FastAPI, Depends, HTTPException 
from pydantic import BaseModel                      
from sqlalchemy import Column, Integer, String, create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker, Session


DATABASE_URL = "sqlite:///bookcollection.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}, 
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False, index=True)
    year = Column(Integer, nullable=True, index=True)


Base.metadata.create_all(bind=engine)


class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None 
    author: Optional[str] = None   
    year: Optional[int] = None     


class BookRead(BookBase):
    id: int 

    class Config:
        orm_mode = True


app = FastAPI(title="Books API")


from typing import Generator

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books/", response_model=BookRead)
def create_book(
    book: BookCreate,          
    db: Session = Depends(get_db),  
):
    db_book = Book(
        title=book.title,
        author=book.author,
        year=book.year,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=List[BookRead])
def read_books(
    skip: int = 0,              
    limit: int = 100,           
    db: Session = Depends(get_db), 
):
    books = db.query(Book).offset(skip).limit(limit).all()
    return books


@app.delete("/books/{book_id}")
def delete_book(
    book_id: int,              
    db: Session = Depends(get_db),
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"detail": "Book deleted"}


@app.put("/books/{book_id}", response_model=BookRead)
def update_book(
    book_id: int,                
    book_update: BookUpdate,     
    db: Session = Depends(get_db), 
):
    
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    if book_update.title is not None:
        book.title = book_update.title
    if book_update.author is not None:
        book.author = book_update.author
    if book_update.year is not None:
        book.year = book_update.year

    db.commit()
    db.refresh(book)
    return book


@app.get("/books/search/", response_model=List[BookRead])
def search_books(
    title: Optional[str] = None,    
    author: Optional[str] = None,   
    year: Optional[int] = None,    
    db: Session = Depends(get_db),  
):
    """
    Примеры запросов:
    - /books/search/?title=Harry
    - /books/search/?author=Rowling
    - /books/search/?year=2001
    - /books/search/?title=Harry&author=Rowling
    """

    query = db.query(Book)

    if title is not None:
        query = query.filter(Book.title.ilike(f"%{title}%"))

    if author is not None:
        query = query.filter(Book.author.ilike(f"%{author}%"))

    if year is not None:
        query = query.filter(Book.year == year)

    return query.all()