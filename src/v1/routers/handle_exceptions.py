from fastapi import HTTPException


def invalid_arguments(code: int = None, msg: str = None):
    raise HTTPException(status_code=code or 400, detail=msg or "Invalid Arguments")


def error(code: int = None, msg: str = None):
    raise HTTPException(status_code=code or 400, detail=msg or "Unknown message")
