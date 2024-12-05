def translate_transcript():
    import os
    import sys
    import subprocess
    if not "venv" in sys.executable:
        raise EnvironmentError("The script must be run in a virtual environment with ipykernel installed. Virtual environment name must contain 'venv' as a safeguard")

    subprocess.run(["pip3", "install", "-r", "additionalreqs.txt"])

    import pprint
    from transformers import MarianMTModel, MarianTokenizer
    import nltk


    with open("./raw_transcript.txt", "r") as file:
        transcript = file.read()
        
    
    nltk.download('punkt_tab')
    sentences = nltk.tokenize.sent_tokenize(transcript, language='french')

    sentences = [sentence.strip() for sentence in sentences]

    with open("./original_transcript.txt", "w") as file:
        for sentence in sentences:
            file.write(sentence + "\n")
    file.close()

    model_name = "Helsinki-NLP/opus-mt-fr-en"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    translation = []

    for sentence in sentences:
        input = tokenizer(sentence, return_tensors="pt", padding=True)
        output = model.generate(**input)
        translation.append([tokenizer.decode(t, skip_special_tokens=True) for t in output])
            
    with open("./translated_transcript.txt", "w") as file:
        for section in translation:
            file.write(section[0] + "\n")
    file.close()
    
if __name__ == "__main__":
    translate_transcript()    




