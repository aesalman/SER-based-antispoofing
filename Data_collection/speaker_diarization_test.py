from pyannote.audio import Pipeline

from huggingface_hub import HfApi

available_pipelines = [p.modelId for p in HfApi().list_models(filter="pyannote-audio-pipeline")]

list(filter(lambda p: p.startswith("pyannote/"), available_pipelines))

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token='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')

audio_file = "../Famous_Figures/Audio/audio_files/Rogan 07.wav"
diarization = pipeline(audio_file)

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")