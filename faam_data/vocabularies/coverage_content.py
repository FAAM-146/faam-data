class CoverageContentTypes:
    COVERAGE_CONTENT_TYPES = (
        "image",
        "thematicClassification",
        "physicalMeasurement",
        "auxiliaryInformation",
        "qualityInformation",
        "referenceInformation",
        "modelResult",
        "coordinate",
    )

    def __contains__(self, item: str) -> bool:
        return item in CoverageContentTypes.COVERAGE_CONTENT_TYPES
    
    def __str__(self) -> str:
        return "Coverage Content Type (ISO 19115-1)"
