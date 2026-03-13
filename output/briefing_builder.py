# Briefing Builder
# This module formats the final report based on the analysis results.

def build_briefing(analysis_results):
    briefing = "Weekly Competitive Intelligence Briefing\n\n"
    for result in analysis_results:
        briefing += f"- {result}\n"
    return briefing

if __name__ == "__main__":
    analysis_results = [
        "Competitor A launched a new product.",
        "Competitor B is hiring aggressively.",
        "Competitor C reduced pricing on key products."
    ]

    briefing = build_briefing(analysis_results)
    print(briefing)
