from essay_writer import ewriter
from gui import writer_gui

if __name__ == "__main__":
    # Create an instance of your ewriter (essay writer graph)
    essay_agent = ewriter()

    # Create an instance of your writer_gui, passing the graph to it
    gui = writer_gui(essay_agent.graph)

    # Launch the Gradio interface
    gui.launch()