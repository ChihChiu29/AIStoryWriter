INITIAL_OUTLINE_WRITER_MODEL="llama3:70b" # Note this value is overridden by the argparser
CHAPTER_OUTLINE_WRITER_MODEL="llama3:70b" # Note this value is overridden by the argparser
CHAPTER_STAGE1_WRITER_MODEL="llama3:70b" # Note this value is overridden by the argparser
CHAPTER_STAGE2_WRITER_MODEL="llama3:70b" # Note this value is overridden by the argparser
CHAPTER_STAGE3_WRITER_MODEL="llama3:70b`" # Note this value is overridden by the argparser
CHAPTER_STAGE4_WRITER_MODEL="llama3:70b" # Note this value is overridden by the argparser
CHAPTER_REVISION_WRITER_MODEL="llama3:70b" # Note this value is overridden by the argparser
REVISION_MODEL="llama3:70b" # Note this value is overridden by the argparser
EVAL_MODEL="llama3:70b" # Note this value is overridden by the argparser
INFO_MODEL="llama3:70b" # Note this value is overridden by the argparser
SCRUB_MODEL="llama3:70b" # Note this value is overridden by the argparser
CHECKER_MODEL="llama3" # Model used to check results

SEED=12 # Note this value is overridden by the argparser

OUTLINE_QUALITY=87 # Note this value is overridden by the argparser
OUTLINE_MIN_REVISIONS=0 # Note this value is overridden by the argparser
OUTLINE_MAX_REVISIONS=3 # Note this value is overridden by the argparser
CHAPTER_NO_REVISIONS=True # Note this value is overridden by the argparser # disables all revision checks for the chapter, overriding any other chapter quality/revision settings
CHAPTER_QUALITY=85 # Note this value is overridden by the argparser
CHAPTER_MIN_REVISIONS=1 # Note this value is overridden by the argparser
CHAPTER_MAX_REVISIONS=3 # Note this value is overridden by the argparser

SCRUB_NO_SCRUB=False # Note this value is overridden by the argparser
EXPAND_OUTLINE=False # Note this value is overridden by the argparser
ENABLE_FINAL_EDIT_PASS=False # Note this value is overridden by the argparser

OPTIONAL_OUTPUT_NAME=""

DEBUG=False

# Tested models:
"llama3:70b" # works as editor model, DO NOT use as writer model, it sucks
"vanilj/midnight-miqu-70b-v1.5" # works rather well as the writer, not well as anything else
"command-r"
"qwen:72b"
"command-r-plus"
"nous-hermes2" # not big enough to really do a good job - do not use
"dbrx" # sucks - do not use