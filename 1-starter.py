import os
from dotenv import load_dotenv
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

# Load environment variables
load_dotenv()

# Create kernel
kernel = sk.Kernel()

# Add Azure OpenAI chat completion service
kernel.add_service(
    AzureChatCompletion(
        deployment_name="gpt-35-turbo",  # Using GPT-3.5-turbo
        endpoint=os.getenv("AZURE_OPENAI_API_BASE"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION")
    )
)

# Import the cooking plugin
plugin = kernel.import_plugin_from_directory("plugins/cooking")
recipe_function = plugin["RecipeGenerator"]

# Test the recipe generator
print("Generating recipe for chocolate cake...")
result = recipe_function.invoke("chocolate cake")
print(result)