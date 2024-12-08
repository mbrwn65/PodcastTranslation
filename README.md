# Podcast Translation
Takes podcast audio as input, transcribes the audio to text using a modified whisper model with faster-whisper, then translates that text using the MarianMT transformer, then finally displays the transcript with an interactive GUI that lets the user click a sentence to change it to its english translation.

https://github.com/user-attachments/assets/94936c14-f660-417f-8ed4-d9adbd75e3ae
_____________________________________
## Transcript Generation
For this project, I converted the [whisper-large-v3-turbo model](https://huggingface.co/openai/whisper-large-v3-turbo) to be usable with [faster-whisper](https://github.com/SYSTRAN/faster-whisper?tab=readme-ov-file), which uses CTranslate2 for more efficient computation. In addition, I used quantization to convert the model to int8 for faster speeds on a cpu. The custom model and code used to convert it are available at https://huggingface.co/Mbrwn/whisper-turbo-ct2.

With the converted model, computation times for the transcript were around 2x faster (~28s vs. ~1m 10s) when tested in similar conditions on a 1-minute audio segment. Their outputs were almost identical, and transcription accuracy showed no noticeable loss.

### The converted model using faster-whisper:
<img width="1329" alt="Converted Turbo" src="https://github.com/user-attachments/assets/063165ee-1530-45d4-a8b6-0f8345d0708f">


### The original whisper turbo model:
<img width="1325" alt="Turbo Baseline" src="https://github.com/user-attachments/assets/90b2cfc2-133a-44b5-bd84-afaea4f2ecb3">

<img width="1101" alt="Turbo Output" src="https://github.com/user-attachments/assets/0b784b26-71d1-44b5-bb28-d7bf6542305d">

______________________________________
## Sentence Tokenization
After generating the transcript and saving it as a .txt, I used [nltk](https://www.nltk.org/api/nltk.tokenize.punkt.html) to tokenize it into sentences to be used in the GUI, and for easier mapping to the translations.
_______________________________________
## Translation Generation
Next, I used the [MarianMT](https://huggingface.co/docs/transformers/en/model_doc/marian) framework to generate a translation of the podcast's transcript, specifically using the [Opus-MT Helenski-NLP model](https://github.com/Helsinki-NLP/Opus-MT). 

Below is the implementation:

<img width="655" alt="Translation Model" src="https://github.com/user-attachments/assets/b8934bcb-90b9-437c-9c11-dd204ac1974e">

The output from this model is added to the "translation" list, then saved as a .txt file in the same format as the transcript to be made into a dictionary for mapping transcript:translation in the GUI.

________________________________________
## Interactive GUI

The GUI (demoed in the introduction) was created using NiceGUI, and uses the dictionary mentioned above to map french to english sentences from the transcript & translation. Each sentence is displayed as an object and when clicked switches to the translation or back to the original (english if currently french, & vice versa.). The GUI can also handle long sentences and has a scroll bar for when text cannot entirely be displayed on the users screen.

________________________________________
## Additional Info
To run, download the repository and run the PodcastTranslation.py file. If all other files are installed, this will run the transcriber, translator, & app .py files. There is a prompt about package installation, since the project requires multiple dependencies that all need to be installed in order to avoid conflicts (this is also why the project is split into different .py files, since combining them created conflict between the faster-whisper & torch package causing the kernel to crash). The .py file may take a bit to install all dependencies and generate the transcript & translation from the model, but then should open and provide a link to the NiceGUI app when running.
