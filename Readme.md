EduChain MCP Server
This project implements an MCP (Modular Command Protocol) server using the MCP Python SDK and integrates it with EduChain. The server exposes tools and resources for educational content generation, including:

📚 MCQ generation
🧑‍🏫 Dynamic lesson planning
🧠 Flashcard generation

🧰 Tools & Technologies

✅ Python 3.11
✅ MCP Python SDK (FastMCP)
✅ EduChain Library
✅ uv (dependency manager)

🚀 Features

1. generate_mcqs (Tool)
   Generates multiple-choice questions based on any topic and quantity.
   Input:
   {
   "topic": "Python Loops",
   "num": 5
   }

Output:Returns a list of structured MCQs with questions, options, correct answer, and explanation.

2. lesson://{subject} (Resource)
   Returns a detailed lesson plan based on a given subject.
   Input: "Python Programming Basics"Output: Structured lesson plan with objectives, topics, hands-on activities, and ethical considerations.

3. generate_flashcards (Tool)
   Generates flashcards for any topic, useful for revision or self-study.
   Input:
   {
   "topic": "Python"
   }

Output:A list of flashcards with question (front), answer (back), and explanation.

🏁 How to Run
📦 Install dependencies

Make sure you're using Python 3.11

pip install uv
uv venv --python=3.11
uv pip install -r pyproject.toml

📝 Create a .env File
Create a .env file in the project root directory to store your API key securely. Add the following line, replacing your_grok_api_key_here with the key obtained from the xAI console:
GROQ_API_KEY=your_grok_api_key_here

To get your Grok API key, visit console.x.ai and sign up or log in to generate a new API key.
▶️ Run the MCP server in dev mode
uv run mcp dev server.py

You should see:
MCP Inspector is up and running at http://localhost:6274 🚀

Visit the inspector to test your tools interactively.

🧪 Claude Desktop Integration
To connect with Claude Desktop, add this to your claude_desktop_config.json:
{
"mcp_servers": [
{
"name": "EduChainMCP",
"host": "http://localhost:8000"
}
]
}

Then test with natural language prompts like:

“Generate 5 MCQs on Python functions.”
“Provide a lesson plan for data structures.”
“Create flashcards for object-oriented programming.”

📁 Project Structure
educhain-mcp-server/
├── server.py # MCP server using FastMCP
├── claude_desktop_config.json
├── lesson_plan.json # Sample output (optional)
├── Sample_Responses.txt # Required for submission
├── README.md # You're reading it!
├── .env # Environment file for API key

✅ Submission
Please email the GitHub repo link to:

📧 prathmesh@buildfastwithai.com
📧 shubham@buildfastwithai.com

Bonus points for including a short Loom video demo!

👨‍💻 Author
Akash KoleyB.Tech Graduate | EduChain Intern Assignment | Python & Data Science Enthusiast

📄 License
This project is intended for educational purposes and the BuildFastWithAI internship assignment. Please contact the author before reuse.
