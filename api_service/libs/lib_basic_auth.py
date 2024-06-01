
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security.base import SecurityBase
from fastapi.security import HTTPBasic
from fastapi.security.utils import get_authorization_scheme_param

from starlette.status import HTTP_403_FORBIDDEN
from starlette.requests import Request
from typing import Optional

from libs import lib_consts as lib_consts

class BasicAuth(SecurityBase):
    def __init__(self, scheme_name: str = None, auto_error: bool = True):
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error
        self.model = HTTPBasic(description="Basic authentication with custom validation")

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.headers.get("Authorization")
        callerfrom: Optional[str] = request.headers.get("From")
        if callerfrom is None:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Not authenticated Error 00"
            )
        if callerfrom != lib_consts.apicallerid:
            raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="Not authenticated Error 0"
            )
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "basic":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
                )
            else:
                return None
        return param