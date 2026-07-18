import os

routers = ['energy', 'market', 'grid', 'assets', 'analytics', 'forecast', 'operations', 'reference']

for r in routers:
    filepath = f"app/api/v1/routers/{r}.py"
    with open(filepath, "w") as f:
        f.write(f'''from fastapi import APIRouter
from app.schemas.responses import MessageResponse

router = APIRouter()

@router.get("/", response_model=MessageResponse)
async def placeholder():
    """Placeholder endpoint for {r.capitalize()} API."""
    return MessageResponse(message="{r.capitalize()} API is under construction.")
''')
