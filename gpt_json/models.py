from dataclasses import dataclass
from enum import Enum, unique


@unique
class ResponseType(Enum):
    DICTIONARY = "DICTIONARY"
    LIST = "LIST"


@unique
class GPTMessageRole(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


@unique
class GPTModelVersion(Enum):
    GPT_3_5 = "gpt-3.5-turbo"
    GPT_3_5_0301 = "gpt-3.5-turbo-0301"
    GPT_4 = "gpt-4"
    GPT_4_0341 = "gpt-4-0314"
    GPT_3_5_DAVINCI_003 = "text-davinci-003"
    GPT_3_5_DAVINCI_002 = "text-davinci-002"
    # GPT_3_CURIE_001 = "text-curie-001"
    # GPT_3_BABBAGE_001 = "text-babbage-001"
    # GPT_3_ADA_001 = "text-ada-001"


@unique
class GPTChatModelVersion(Enum):
    GPT_3_5 = "gpt-3.5-turbo"
    GPT_3_5_0301 = "gpt-3.5-turbo-0301"
    GPT_4 = "gpt-4"
    GPT_4_0341 = "gpt-4-0314"


@unique
class GPTCompletionModelVersion(Enum):
    GPT_3_5_DAVINCI_003 = "text-davinci-003"
    GPT_3_5_DAVINCI_002 = "text-davinci-002"
    # GPT_3_CURIE_001 = "text-curie-001"
    # GPT_3_BABBAGE_001 = "text-babbage-001"
    # GPT_3_ADA_001 = "text-ada-001"

@dataclass
class FixTransforms:
    """
    How a gpt payload was modified to be valid
    """
    fixed_truncation: bool = False
    fixed_bools: bool = False


@dataclass
class GPTMessage:
    """
    A single message in the chat sequence
    """
    role: GPTMessageRole
    content: str
