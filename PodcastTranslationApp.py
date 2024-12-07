from nicegui import ui

with open("original_transcript.txt", "r") as file:
    transcript = [line.strip() for line in file]
file.close()
with open("translated_transcript.txt", "r") as file:
    translation = [line.strip() for line in file]
file.close()

# Dictionary of French sentences as keys and English translations as values
transcript_to_translation = {}
for idx, sentence in enumerate(transcript):
    transcript_to_translation[sentence] = translation[idx]
    
# Function to toggle sentences
def toggle_sentence(label, french, english):
    if label.text == french:
        label.text = english
    else:
        label.text = french

# Set styles to prevent scrolling outside UI
ui.add_head_html("""
<style>
    html, body {
        margin: 0;
        padding: 0;
        height: 100%;
        overflow: hidden; /* Disable scrolling on the page itself */
    }
</style>
""")

# Enable dark mode
ui.dark_mode()

# Generate the full-screen, scrollable GUI
with ui.column().classes("w-full h-screen bg-gray-900 overflow-y-auto"):
    # Title
    ui.label("French Transcript (click sentences to translate)").classes(
        "text-3xl font-extrabold text-white mb-4 px-6 py-6 text-center"
    )
    
    # Sentence list
    for french, english in transcript_to_translation.items():
        label = ui.label(french).classes(
            "text-lg text-gray-300 mb-4 px-6 py-3 rounded-lg transition-all duration-300 cursor-pointer hover:bg-gray-700 hover:text-white"
        )
        label.on("click", lambda e, l=label, f=french, en=english: toggle_sentence(l, f, en))

# Start the NiceGUI app
ui.run()