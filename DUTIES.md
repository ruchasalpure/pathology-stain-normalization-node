# Duties and Responsibilities for Pathology Stain Normalization Node Agent

## Dual-Control Architecture
Maker:
stain-vector-estimator

Checker:
color-constancy-checker

## Operational Workflow
1. The Maker (stain-vector-estimator) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (color-constancy-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
