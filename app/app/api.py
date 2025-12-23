from fastapi import APIRouter

router = APIRouter()

@router.get("/analyze/{sector}")
async def analyze_sector(sector: str):
    return {
        "sector": sector,
        "report_markdown": f"## Market Analysis for {sector}\n\nComing soon..."
    }
