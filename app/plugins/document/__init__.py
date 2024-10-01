from app.models.prompt import Prompt
from collections import OrderedDict
from app.models.request import ConnectionArgument

# Plugin Metadata
__version__ = '1.0.0'
__plugin_name__ = 'document'
__display_name__ = 'document loader'
__description__ = 'document integration for handling document data'
__icon__ = '/assets/plugins/logos/document.svg'
__category__ = 4

# Connection arguments
__connection_args__ = OrderedDict(
    document_file= ConnectionArgument(
        type = 8,
        generic_name= 'document file',
        description = 'Supports only .pdf, .yaml, .txt, and .docx files.',
        order = 1,
        required = True,
        value = None,
        slug = "document_file"
    )
)

# Prompt
__prompt__ = Prompt(**{
        "base_prompt": "{system_prompt}{user_prompt}",
        "system_prompt": {
            "template": """
            You are an Chatbot designed to answer user questions based only on the context given to you.
            Use the details enclosed in `[context][/context]` to generate answer

            [context]
            {context}
            [/context]

            Adhere to these rules while generating query:
            - Deliberately go through the question and context word by word to appropriately answer the question
            """
        },
        "user_prompt":{
            "template": """
            User question is "$question"
            generate a json in the following format without any formatting.
            {
                "explanation": "Explain how you finalized the sql query using the schemas and rules provided",
                "operation_kind" : "none",
                "general_message": "answer to user question based on the context",
                "confidence" : "confidence in 100",
                "main_entity": "document"
            }
            """
        },
        "regeneration_prompt": {
            "template": """
            User question is "$question"
            generate a json in the following format without any formatting.
            {
                "explanation": "Explain how you finalized the sql query using the schemas and rules provided",
                "operation_kind" : "none",
                "general_message": "answer to user question based on the context",
                "confidence" : "confidence in 100",
                "main_entity": "document"
            }
            """
        }
    })



__all__ = [
    __version__, __plugin_name__, __display_name__ , __description__, __icon__, __category__, __prompt__
]