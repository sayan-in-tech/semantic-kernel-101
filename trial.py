import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory, AuthorRole, ChatMessageContent
import os
import dotenv
dotenv.load_dotenv()

AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
AZURE_OPENAI_API_BASE = os.getenv("AZURE_OPENAI_API_BASE")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# --- Azure OpenAI credentials ---

async def main():
    kernel = sk.Kernel()

    chat_service = AzureChatCompletion(
        deployment_name=AZURE_OPENAI_CHAT_DEPLOYMENT,
        endpoint=AZURE_OPENAI_API_BASE,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION
    )
    kernel.add_service(chat_service)

    chat_history = ChatHistory()
    chat_history.add_message(
        ChatMessageContent(role=AuthorRole.USER, content="Write a short haiku about AI.")
    )

    settings = AzureChatPromptExecutionSettings(
        temperature=0.7,
        max_tokens=50
    )

    response = await chat_service.get_chat_message_content(chat_history, settings)
    print("Response:", response.content)  # Directly access .content

if __name__ == "__main__":
    asyncio.run(main())
