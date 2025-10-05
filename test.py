from pathlib import Path
import json

# Define job search parameters
job_parameters = {
    "level": "Senior",
    "position": "Software Engineer",
    "location": "San Francisco, CA"
}

# Example resume (this would be dynamically loaded in a real system)
user_resume = {
    "name": "Jane Doe",
    "skills": ["Python", "AWS", "Docker", "Kubernetes"],
    "experience": [
        {
            "company": "TechCorp",
            "role": "Senior Software Engineer",
            "years": 3,
            "tech_stack": ["Python", "Flask", "AWS"]
        },
        {
            "company": "WebSolutions",
            "role": "Backend Developer",
            "years": 2,
            "tech_stack": ["Django", "PostgreSQL", "Docker"]
        }
    ],
    "preferences": {
        "industry": "Tech",
        "company_size": "Startup",
        "remote": True,
        "salary_expectation": 150000
    }
}

# Simulated job listings
job_list = [
    {
        "job_title": "Senior Software Engineer",
        "company_name": "Innovatech",
        "location": "San Francisco, CA",
        "tech_stack": ["Python", "AWS", "React"],
        "remote": True,
        "salary_range": [140000, 160000],
        "contract_type": "Full-time"
    },
    {
        "job_title": "Lead Backend Developer",
        "company_name": "EnterprizeX",
        "location": "San Francisco, CA",
        "tech_stack": ["Java", "Spring", "Oracle"],
        "remote": False,
        "salary_range": [130000, 150000],
        "contract_type": "Full-time"
    }
]

# Match scoring logic
def compute_match_score(job, resume):
    score = 1
    reason = []

    if job["remote"] == resume["preferences"]["remote"]:
        score += 1
        reason.append("Matches remote preference")

    if job["contract_type"] == "Full-time":
        score += 1
        reason.append("Full-time role matches preference")

    tech_match = len(set(job["tech_stack"]).intersection(set(sum((e["tech_stack"] for e in resume["experience"]), []))))
    if tech_match >= 2:
        score += 1
        reason.append("Strong tech stack alignment")

    salary_match = job["salary_range"][0] <= resume["preferences"]["salary_expectation"] <= job["salary_range"][1]
    if salary_match:
        score += 1
        reason.append("Salary within expected range")

    return min(score, 5), "; ".join(reason)

# Score jobs
for job in job_list:
    match_score, reason = compute_match_score(job, user_resume)
    job["match_score"] = match_score
    job["reason"] = reason

# Select the best job
best_job = max(job_list, key=lambda j: j["match_score"])
for job in job_list:
    job["selected"] = (job == best_job)

# Output paths
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# Save rewritten resume (simulated)
rewritten_resume = f"""# Resume: {user_resume['name']}

## Summary
Experienced software engineer with strong background in Python and AWS. Proven ability to deliver scalable backend systems.

## Experience
"""
for exp in user_resume["experience"]:
    rewritten_resume += f"- **{exp['role']}**, {exp['company']} ({exp['years']} years) — Stack: {', '.join(exp['tech_stack'])}\n"

(Path(output_dir) / "rewritten_resume.md").write_text(rewritten_resume, encoding="utf-8")

# Save company research (simulated)
company_research = f"""## Company Overview
**{best_job['company_name']}** is a tech company based in {best_job['location']}.

## Mission and Values
Focusing on innovation and scalable engineering.

## Recent News or Changes
[Placeholder] Recently expanded product lines in cloud services.

## Role Context and Product Involvement
Position: {best_job['job_title']} — working with {', '.join(best_job['tech_stack'])} stack.

## Likely Interview Topics
- Python system design
- AWS architecture
- CI/CD and DevOps

## Suggested Questions to Ask
- How is engineering success measured?
- What’s the team’s deployment pipeline?
"""

(Path(output_dir) / "company_research.md").write_text(company_research, encoding="utf-8")

# Save interview prep (simulated)
interview_prep = f"""# Interview Prep: {best_job['company_name']} – {best_job['job_title']}

## Job Overview
{best_job['job_title']} at {best_job['company_name']}, located in {best_job['location']}.

## Why This Job Is a Fit
- Aligns with your remote work preference
- Uses familiar tech stack: {', '.join(best_job['tech_stack'])}
- Salary within your expectations

## Resume Highlights for This Role
See rewritten resume in `rewritten_resume.md`.

## Company Summary
See `company_research.md`.

## Predicted Interview Questions
- Tell us about a time you scaled a backend system
- How do you ensure security in AWS-based services?

## Questions to Ask Them
- How is mentorship structured on your team?
- What’s the current tech debt and how is it managed?

## Concepts To Know/Review
- AWS Lambda, EC2, VPC networking
- REST API scaling
- CI/CD best practices

## Strategic Advice
Stay focused on your impact in previous roles. Emphasize collaborative experience and DevOps tooling expertise.
"""

(Path(output_dir) / "interview_prep.md").write_text(interview_prep, encoding="utf-8")
