
from datetime import datetime, timezone
from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl, Field



from antigravity.skills import compliance_tools

router = APIRouter()

class ComplianceRequest(BaseModel):
    realtor_license_id: str = Field(..., min_length=8, max_length=8, description="Exactly 8 characters as per rules")
    image_url: HttpUrl
    is_structural_change: bool
    ai_confidence_score: float

@router.post("/verify-image")
def verify_image(request: ComplianceRequest):
    # Calculate risk using our securely registered custom skill
    risk = compliance_tools.calculate_risk(
        confidence=request.ai_confidence_score, 
        is_structural=request.is_structural_change
    )
    
    return {
        "realtor_license_id": request.realtor_license_id,
        "risk_rating": risk,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
