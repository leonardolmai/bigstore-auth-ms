from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse


async def check_company_cnpj_middleware(request: Request, call_next):
    try:
        excluded_paths = ["/docs/", "/docs", "/openapi.json", "/token"]

        path = request.url.path.rstrip("/")
        if str(path) not in excluded_paths:
            cnpj = request.headers.get("x-company-cnpj")
            if not cnpj:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="CNPJ is required in the request headers.",
                )

        response = await call_next(request)
        return response
    except HTTPException as exc:
        return JSONResponse(
            content={"error": exc.detail},
            status_code=exc.status_code,
        )
