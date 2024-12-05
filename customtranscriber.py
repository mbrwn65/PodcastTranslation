def transcribe_podcast():
    import os
    import sys
    import subprocess
    if not "venv" in sys.executable:
        raise EnvironmentError("The script must be run in a virtual environment with ipykernel installed. Virtual environment name must contain 'venv' as a safeguard")

    #saves current packages to uninstall.txt
    with open("./uninstall.txt", "w") as file:
        subprocess.run(["pip3", "freeze"], stdout=file) 
    file.close()
    #uninstalls all non-essential packages in environment
    subprocess.run(["pip3", "uninstall", "-r", "uninstall.txt", "-y"])
    #installs necessary packages
    subprocess.run(["pip3", "install", "-r", "startingreqs.txt"])

    from faster_whisper import WhisperModel
    import ctranslate2


    podcastfolder = "./Podcasts"
    podcastfiles = []
    for file in os.listdir(podcastfolder):
        if file != ".DS_Store":
            podcastfiles.append(file)
    podcastaudio = podcastfolder + "/" + podcastfiles[0]


    #BELOW IS CODE USED TO CONVERT TURBO WHISPER MODEL TO CT2 INT8 QUANTIZED MODEL (STORED AT huggingface Mbwn/whisper-turbo-ct2)
    # turbo_model = "openai/whisper-large-v3-turbo"
    # ct2_output_dir = "whisper-large-v3-turbo-ct2"

    # converter = ctranslate2.converters.TransformersConverter(
    #     model_name_or_path=turbo_model, copy_files=["tokenizer.json", "preprocessor_config.json"]
    # )
    # converter.convert(output_dir=ct2_output_dir, quantization="int8", force=True)


    # Optimized Turbo Model With Int8 Quantization
    model_name = "Mbrwn/whisper-turbo-ct2"
    model = WhisperModel(model_name, device = "cpu", compute_type="int8")
    segments, info = model.transcribe(podcastaudio, beam_size=5, language="fr")
    transcript = []

    for segment in segments:
        transcript.append(segment.text)

    output = ""
    for section in transcript:
        output += section
        
    with open("./raw_transcript.txt", "w") as file:
        file.write(output)
    file.close()

if __name__ == "__main__":
    transcribe_podcast()

