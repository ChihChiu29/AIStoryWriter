# DEFAULT_MODEL_CONFIG = "ollama://llama3:70b"  # Can't load
# DEFAULT_MODEL_CONFIG = "ollama://llama3.1:8b@192.168.1.71:11434"  # OK-ish
# DEFAULT_MODEL_CONFIG = "ollama://gemma2:9b@192.168.1.71:11434"  # Best so far, score: 8
# DEFAULT_MODEL_CONFIG = "ollama://llama3-gradient:8b@192.168.1.71:11434"  # Not good at all
# DEFAULT_MODEL_CONFIG = "ollama://qwen2:7b@192.168.1.71:11434"  # Not good at all
# DEFAULT_MODEL_CONFIG = "ollama://gemma2:27b@192.168.1.71:11434"  # Too slow; a few words per min.
# DEFAULT_MODEL_CONFIG = "ollama://phi3:14b@192.168.1.71:11434"  # Went into a loop that seems to be about theory proving.
# DEFAULT_MODEL_CONFIG = "ollama://mistral:7b@192.168.1.71:11434"  # Waiting eval "Story_The_Forgotten_Kingdom"
# DEFAULT_MODEL_CONFIG = "ollama://mixtral:8x7b@192.168.1.71:11434"  # Too slow; a few words per min.
# DEFAULT_MODEL_CONFIG = "ollama://zephyr:7b@192.168.1.71:11434"  # Wait eval "The Lost City"
# DEFAULT_MODEL_CONFIG = "ollama://mistral-nemo:12b@192.168.1.71:11434"  # Wait eval "The Lost Heir"
# DEFAULT_MODEL_CONFIG = "ollama://dolphin-llama3:8b@192.168.1.71:11434"  # Wait eval "Supercatomeow's Adventure"
# DEFAULT_MODEL_CONFIG = "ollama://orca-mini:7b@192.168.1.71:11434"  # Doesn't work at all, 0 word generated.
# DEFAULT_MODEL_CONFIG = "ollama://yi:9b@192.168.1.71:11434"  # Doesn't work at all, 0 word generated.
# DEFAULT_MODEL_CONFIG = "ollama://mistral-openorca:7b@192.168.1.71:11434"  # "Supercatomeow and The Master's Enchanted Adventure", score: 4
# DEFAULT_MODEL_CONFIG = "ollama://llava-llama3:8b@192.168.1.71:11434"  # Wait eval "Supercatomeow and The Master"
# DEFAULT_MODEL_CONFIG = "ollama://wizard-vicuna-uncensored:13b@192.168.1.71:11434"  # "A Tale of Two Cities", score: 2
# DEFAULT_MODEL_CONFIG = "ollama://wizardlm2:7b@192.168.1.71:11434"  # Inf loop about JSON generation.
# DEFAULT_MODEL_CONFIG = "ollama://hermes3:8b@192.168.1.71:11434"  # Wait eval "The Enchanted Paintbrush"
DEFAULT_MODEL_CONFIG = "ollama://glm4:9b@192.168.1.71:11434"  # Wait eval "The Whiskers of the Wildwood"


INITIAL_OUTLINE_WRITER_MODEL = (
    DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
)
CHAPTER_OUTLINE_WRITER_MODEL = (
    DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
)
CHAPTER_STAGE1_WRITER_MODEL = DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
CHAPTER_STAGE2_WRITER_MODEL = DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
CHAPTER_STAGE3_WRITER_MODEL = DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
CHAPTER_STAGE4_WRITER_MODEL = DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
CHAPTER_REVISION_WRITER_MODEL = (
    DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
)
REVISION_MODEL = DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
EVAL_MODEL = DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
INFO_MODEL = DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
SCRUB_MODEL = DEFAULT_MODEL_CONFIG  # Note this value is overridden by the argparser
CHECKER_MODEL = DEFAULT_MODEL_CONFIG  # Model used to check results
TRANSLATOR_MODEL = DEFAULT_MODEL_CONFIG

# OLLAMA_HOST = "127.0.0.1:11434"
OLLAMA_HOST = "192.168.1.71:11434"

SEED = 12  # Note this value is overridden by the argparser

TRANSLATE_LANGUAGE = ""  # If the user wants to translate, this'll be changed from empty to a language e.g 'French' or 'Russian'
TRANSLATE_PROMPT_LANGUAGE = ""  # If the user wants to translate their prompt, this'll be changed from empty to a language e.g 'French' or 'Russian'

OUTLINE_QUALITY = 87  # Note this value is overridden by the argparser
OUTLINE_MIN_REVISIONS = 0  # Note this value is overridden by the argparser
OUTLINE_MAX_REVISIONS = 3  # Note this value is overridden by the argparser
CHAPTER_NO_REVISIONS = True  # Note this value is overridden by the argparser # disables all revision checks for the chapter, overriding any other chapter quality/revision settings
CHAPTER_QUALITY = 85  # Note this value is overridden by the argparser
CHAPTER_MIN_REVISIONS = 1  # Note this value is overridden by the argparser
CHAPTER_MAX_REVISIONS = 3  # Note this value is overridden by the argparser

SCRUB_NO_SCRUB = False  # Note this value is overridden by the argparser
EXPAND_OUTLINE = False  # Note this value is overridden by the argparser
ENABLE_FINAL_EDIT_PASS = False  # Note this value is overridden by the argparser

SCENE_GENERATION_PIPELINE = True

OPTIONAL_OUTPUT_NAME = ""

DEBUG = False

# Tested models:
"llama3:70b"  # works as editor model, DO NOT use as writer model, it sucks
"vanilj/midnight-miqu-70b-v1.5"  # works rather well as the writer, not well as anything else
"command-r"
"qwen:72b"
"command-r-plus"
"nous-hermes2"  # not big enough to really do a good job - do not use
"dbrx"  # sucks - do not use
