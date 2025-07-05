# server.py

from mcp.server.fastmcp import FastMCP
from educhain.core.educhain import Educhain

# Initialize MCP server
mcp = FastMCP("EduChainMCP")

# Initialize EduChain client
educhain = Educhain()

# ----------------------------
# Tool: Generate MCQs
# ----------------------------
@mcp.tool()
def generate_mcqs(topic: str = "Python Programming Basics", num: int = 5) -> list[dict]:
    """Generate multiple-choice questions for a given topic."""
    data = educhain.qna_engine.generate_questions(topic=topic, num=num)
    return [
        {
            "question": q.question,
            "options": q.options,
            "answer": q.answer,
            "explanation": q.explanation
        }
        for q in data.questions
    ]

# ----------------------------
# Resource: Get Lesson Plan
# ----------------------------
@mcp.resource("lesson://{subject}")
def get_lesson_plan(subject: str) -> dict:
    """Return a lesson plan for the given subject."""
    data = educhain.content_engine.generate_lesson_plan(subject)
    lesson = {
        "title": data.title,
        "subject": data.subject,
        "learning_objectives": data.learning_objectives,
        "lesson_introduction": data.lesson_introduction,
        "main_topics": [
            {
                "title": topic.title,
                "subtopics": [
                    {
                        "title": sub.title,
                        "key_concepts": [
                            {
                                "type": concept.type,
                                "content": concept.content
                            }
                            for concept in sub.key_concepts
                        ],
                        "discussion_questions": [
                            dq.question for dq in sub.discussion_questions
                        ],
                        "hands_on_activities": [
                            {
                                "title": act.title,
                                "description": act.description
                            }
                            for act in sub.hands_on_activities
                        ],
                        "reflective_questions": [
                            rq.question for rq in sub.reflective_questions
                        ],
                        "assessment_ideas": [
                            {
                                "type": assess.type,
                                "description": assess.description
                            }
                            for assess in sub.assessment_ideas
                        ]
                    }
                    for sub in topic.subtopics
                ]
            }
            for topic in data.main_topics
        ],
        "learning_adaptations": data.learning_adaptations,
        "real_world_applications": data.real_world_applications,
        "ethical_considerations": data.ethical_considerations
    }

    return lesson

# ----------------------------
# Tool: Generate Flashcards
# ----------------------------
@mcp.tool()
def generate_flashcards(topic: str = "Python", num: int = 5) -> list[dict]:
    """Generate flashcards for a topic."""
    concepts = educhain.content_engine.generate_flashcards(topic, num)
    return [
        {
            "question": c.front,
            "answer": c.back,
            "explanation": c.explanation
        }
        for c in concepts.flashcards
    ]

