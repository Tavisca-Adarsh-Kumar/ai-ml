Azure AI Language Service
---

- It is a cloud-based service that includes features for understanding and analyzing text.
- It includes various features that support sentiment analysis, key phrase identification, text summarization, and conversational language understanding.

# Understand Text Analytics

## Tokenization

- The first step in analyzing a corpus is to break it down into tokens.
- For the sake of simplicity, you can think of each distinct word in the training text as a token, though in reality, tokens can be generated for partial words, or combinations of words and punctuation.

### Text normalization

- Before generating tokens, you may choose to normalize the text by removing punctuation and changing all words to lower case.
- For analysis that relies purely on word frequency, this approach improves overall performance. However, some semantic meaning may be lost.

### Stop word removal

- Stop words are words that should be excluded from the analysis. For example, "the", "a", or "it" make text easier for people to read but add little semantic meaning. 
- By excluding these words, a text analysis solution may be better able to identify the important words.
- n-grams are multi-term phrases such as "I have" or "he walked".
- A single word phrase is a unigram, a two-word phrase is a bi-gram, a three-word phrase is a tri-gram, and so on. By considering words as groups, a machine learning model can make better sense of the text.

### Stemming

- It is a technique in which `algorithms are applied to consolidate words before counting them`, so that words with the same root, like "power", "powered", and "powerful", are interpreted as being the same token.

## Frequency Analysis

- After tokenizing the words, you can perform some analysis to count the number of occurrences of each token.
- The most commonly used words (other than stop words such as "a", "the", and so on) can often provide a clue as to the main subject of a text corpus.
- For example, the most common words in the entire text of the "go to the moon" speech we considered previously include "new", "go", "space", and "moon".
- If we were to tokenize the text as bi-grams (word pairs), the most common bi-gram in the speech is "the moon". From this information, we can easily surmise that the text is primarily concerned with space travel and going to the moon.

## Machine learning for text classification

- Uses a classification algorithm, such as `logistic regression`, to train a machine learning model that classifies text based on a known set of categorizations.
- A common application of this technique is to train a model that classifies text as positive or negative in order to perform `sentiment analysis or opinion mining`.

# Azure AI Language Features

- Named entity recognition
    - Identifies people, places, events, and more. This feature can also be customized to extract custom categories.
- Entity linking
    - Identifies known entities together with a link to Wikipedia.
- Personal identifying information (PII) detection
    - Identifies personally sensitive information, including personal health information (PHI).
- Language detection
    - Identifies the language of the text and returns a language code such as "en" for English.
- Sentiment analysis and opinion mining
    - Identifies whether text is positive or negative.
- Summarization
    - Summarizes text by identifying the most important information.
- Key phrase extraction
    - Lists the main concepts from unstructured text.
- Question Answers

# Translation Service

## Understand translation concepts

### Literal and semantic translation

- Early attempts at machine translation applied `literal translations`.
- A literal translation is where each word is translated to the corresponding word in the target language.
- This approach presents some issues. For one case, there may not be an equivalent word in the target language.
- Another case is where literal translation can change the meaning of the phrase or not get the context correct.
- AI systems must be able to understand, not only the words, but also the semantic context in which they're used.
- In this way, the service can return a more accurate translation of the input phrase or phrases.
- The grammar rules, formal versus informal, and colloquialisms all need to be considered.

### Text and speech translation

- `Text translation` can be used to translate documents from one language to another, translate email communications that come from foreign governments, and even provide the ability to translate web pages on the Internet.
- Many times you see a Translate option for posts on social media sites, or the Bing search engine can offer to translate entire web pages that are returned in search results.
- `Speech translation` is used to translate between spoken languages, sometimes directly (speech-to-speech translation) and sometimes by translating to an intermediary text format (speech-to-text translation).

## Understand translation in Azure

### Azure AI Translator service

- It supports text-to-text translation.
- It is easy to integrate in your applications, websites, tools, and solutions.
- It uses a `Neural Machine Translation (NMT)` model for translation, which analyzes the semantic context of the text and renders a more accurate and complete translation as a result.

#### Language support

- It supports more than 130 languages.
- You must specify the language you are translating from and the language you are translating to using ISO 639-1 language codes, such as en for English, fr for French, and zh for Chinese.
- Alternatively, you can specify cultural variants of languages by extending the language code with the appropriate 3166-1 cultural code - for example, en-US for US English, en-GB for British English, or fr-CA for Canadian French.
- You can specify one from language with multiple to languages, enabling you to simultaneously translate a source document into multiple languages.

### Azure AI Speech service

- It enables speech to text and speech-to-speech translation.
- Translate spoken audio from a streaming source, such as a microphone or audio file, and return the translation as text or an audio stream. This enables scenarios such as real-time closed captioning for a speech or simultaneous two-way translation of a spoken conversation.

#### Language support

- You can specify one source language and one or more target languages to which the source should be translated with Azure AI Speech.
- You can translate speech into over 90 languages.
- The source language must be specified using the extended language and culture code format, such as es-US for American Spanish.
- The target languages must be specified using a two-character language code, such as en for English or de for German.

## Get started with translation in Azure

### Azure resources for Azure AI Translator and Azure AI Speech

- There are `dedicated Translator and Speech resource` types for these services, which you can use if you want to manage access and billing for each service individually.
- You can create an Azure AI services resource that provides access to both services through a single Azure resource, consolidating billing and enabling applications to access both services through a single endpoint and authentication key.

#### Using Azure AI Translator

- Text translation
    - Used for quick and accurate text translation in real time across all supported languages.
- Document translation
    - Used to translate multiple documents across all supported languages while preserving original document structure.
- Custom translation
    - Used to enable enterprises, app developers, and language service providers to build customized neural machine translation (NMT) systems.

##### Azure AI Translator's application programming interface (API)

- It offers some optional configuration to help you fine-tune the results that are returned, including:
    - Profanity filtering
        - Without any configuration, the service will translate the input text, without filtering out profanity.
        - Profanity levels are typically culture-specific but you can control profanity translation by either marking the translated text as profane or by omitting it in the results.
    - Selective translation
        - You can tag content so that it isn't translated.
        - For example, you may want to tag code, a brand name, or a word/phrase that doesn't make sense when localized.

#### Speech translation with Azure AI Speech

##### Speech to text

- Used to transcribe speech from an audio source to text format.

##### Text to speech

- Used to generate spoken audio from a text source.

##### Speech Translation

- Used to translate speech in one language to text or speech in another.

