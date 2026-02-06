from research_blog.crew import ResearchBlog


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI agents in coding'
      
    }

    try:
        ResearchBlog().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


