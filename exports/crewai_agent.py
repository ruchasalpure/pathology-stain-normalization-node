from crewai import Agent

pathology_stain_normalization_node = Agent(
    role="Pathology Stain Normalization Node",
    goal="Deliver high-precision autonomous Pathology Stain Normalization Node operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
