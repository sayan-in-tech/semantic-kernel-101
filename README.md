# Semantic Kernel 101 - Azure OpenAI

This project demonstrates how to use Microsoft Semantic Kernel with Azure OpenAI services.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables:**
   The project uses a `.env` file for configuration. Make sure your `.env` file contains:
   ```
   AZURE_OPENAI_API_KEY="your-api-key"
   AZURE_OPENAI_API_BASE="https://STD-INS-GenAI-01.openai.azure.com/"
   AZURE_OPENAI_CHAT_DEPLOYMENT="gpt-4o-mini"
   AZURE_OPENAI_EMBEDDING_DEPLOYMENT="text-embedding-ada-002"
   AZURE_OPENAI_API_VERSION="2024-02-01"
   ```

## Running the Application

After setting up the `.env` file, run:

```bash
python 1-starter.py
```

This will:
1. Connect to your Azure OpenAI instance
2. Load the cooking plugin
3. Generate a recipe for chocolate cake using the RecipeGenerator function

## Project Structure

- `1-starter.py` - Main application file
- `.env` - Environment variables configuration
- `plugins/cooking/RecipeGenerator/` - Cooking plugin with recipe generation functionality
- `requirements.txt` - Python dependencies

## Azure OpenAI Configuration

The project is configured to use:
- **Chat Model:** gpt-4o-mini
- **Embedding Model:** text-embedding-ada-002
- **API Version:** 2024-02-01
- **Endpoint:** STD-INS-GenAI-01.openai.azure.com

## Troubleshooting

If you encounter issues:

1. **Authentication Error:** Verify your API key is correct in the `.env` file
2. **Connection Error:** Check your internet connection and Azure endpoint
3. **Import Error:** Make sure you've installed all dependencies with `pip install -r requirements.txt` 