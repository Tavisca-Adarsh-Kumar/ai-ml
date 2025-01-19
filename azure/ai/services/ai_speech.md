Azure AI Speech
---

# Understand speech recognition and synthesis

## Speech Recognition

- `Speech recognition` takes the spoken word and `converts it into data that can be processed` - often by transcribing it into text.
- The spoken words can be in the form of a recorded voice in an audio file, or live audio from a microphone.
- Speech patterns are analyzed in the audio to determine recognizable patterns that are mapped to words. To accomplish this, the software typically uses multiple models.
    - An acoustic model
        - Converts the audio signal into phonemes (representations of specific sounds).
    - A language model
        - Maps phonemes to words, usually using a statistical algorithm that predicts the most probable sequence of words based on the phonemes.
- The recognized words are typically converted to text, which you can use for various purposes.

## Speech Synthesis

- `Speech synthesis` is concerned with vocalizing data, usually by `converting text to speech`.
- To synthesize speech, the system typically tokenizes the text to break it down into individual words, and assigns phonetic sounds to each word.
- It then breaks the phonetic transcription into prosodic units (such as phrases, clauses, or sentences) to create phonemes that will be converted to audio format.
- These phonemes are then synthesized as audio and can be assigned a particular voice, speaking rate, pitch, and volume.
- You can use the output of speech synthesis for many purposes.

# Azure AI Speech Service

## Speech to text

- Used to perform real-time or batch transcription of audio into a text format

### Real-time transcription

- Allows you to transcribe text in audio `streams`.
- You can use real-time transcription for presentations, demos, or any other scenario where a person is speaking.
- In order for real-time transcription to work, your application needs to be listening for incoming audio from a microphone, or other audio input source such as an audio file.
- Your application code streams the audio to the service, which returns the transcribed text.

### Batch transcription

- You can point to audio files with a shared access signature (SAS) URI and asynchronously receive transcription results.
- It should be run in an asynchronous manner because the batch jobs are scheduled on a best-effort basis.
- Normally a job starts executing within minutes of the request but there's no estimate for when a job changes into the running state.

## Text to speech

- The text to speech API enables you to `convert text input to audible speech`, which can either be played directly through a computer speaker or written to an audio file.

### Speech synthesis voices

- When you use the text to speech API, you can specify the voice to be used to vocalize the text.
- This capability offers you the flexibility to personalize your speech synthesis solution and give it a specific character.
- The service includes `multiple pre-defined voices` with support for `multiple languages and regional pronunciation`, including neural voices that leverage neural networks to overcome common limitations in speech synthesis with regard to intonation, resulting in a more natural sounding voice.
- You can also develop `custom voices` and use them with the text to speech API.

# Use Azure AI Speech

- Azure AI Speech is available for use through several tools and programming languages including:
    - Studio interfaces
    - Command Line Interface (CLI)
    - REST APIs and Software Development Kits (SDKs)

## Azure resources for Azure AI Speech

You can choose to create either of the following types of resource:

- A Speech resource
    - If you only plan to use Azure AI Speech
    - If you want to manage access and billing for the resource separately from other services.
- An Azure AI services resource
    - If you plan to use Azure AI Speech in combination with other Azure AI services, and you want to manage access and billing for these services together.

