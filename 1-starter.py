import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

kernel = sk.Kernel()
api_key, org_id = sk.get_openai_api_key()
kernel.add_chat_completion_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

skill = kernel.import_skill_from_directory("plugins", "cooking")
recipe_function = skill["RecipeGenerator"]

print(recipe_function.invoke("chocolate cake"))