import sys
import os
from datetime import datetime, timezone
from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl, Field

# Add the .antigravity/skills folder to Python path to import compliance_tools
skills_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.antigravity/skills"))
if skills_path not in sys.path:
    sys.path.append(skills_path)

import compliance_tools

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
