from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

engine = create_async_engine(
    "localhost:5432",
    echo=False,
    future=True,
    pool_pre_ping=True,  # ensures dead connections are revived
    pool_size=10,  # keep 10 connections in the connection pool
    max_overflow=20,  # maximum number of connections that can be opened beyond pool_size
)


AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
