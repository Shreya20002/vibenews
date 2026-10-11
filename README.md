# NEWS but from Eminem

## Overview
This project is me trying out and experimenting with **AgentStack**. It takes **five recent news headlines** and fuses them into a single, rapid-fire rap verse styled after **Eminem**.

## How It Works
1. The **newresearcher** agent collects the **five latest news headlines** from online sources.  
2. The **eminem** agent analyzes these headlines and crafts a unified 5-7 line rap verse, blending all the headlines into one creative narrative with rapid-fire flow, multisyllabic rhymes and sharp punchlines.  
3. The output is an entertaining, lyrical summary of the day's top stories.

## Requirements
- Python 3.10 – 3.13
- [Poetry](https://python-poetry.org/)
- API keys for:
  - **OpenAI**: both agents run on `gpt-4o`
  - **AgentOps**: run tracking
  - **Perplexity**: news search
  - **Firecrawl**: scraping article pages

## Setup
```bash
cd storytime
poetry install
cp .env.example .env
```
Open `storytime/.env`, remove the `#` in front of `OPENAI_API_KEY` and `AGENTOPS_API_KEY`, and fill in all four keys. `.env` is gitignored, so your keys won't be committed.

## Run
From the `storytime` folder:
```bash
poetry run python src/main.py
```

## Customizing
- **Change the rapper or the style:** edit the `eminem` agent in `storytime/src/config/agents.yaml` and the `rap` task in `storytime/src/config/tasks.yaml`.
- **Change the researcher's tools:** see `storytime/src/crew.py`.
- **Change how recent the news is:** set `search_recency_filter` in `storytime/src/tools/perplexity_tool.py` (`"day"`, `"week"` or `"month"`).

## License
MIT, see [storytime/LICENSE.md](storytime/LICENSE.md).
