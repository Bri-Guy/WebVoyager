# Agent-A11y-Bench: Accessibility Benchmark for Computer Use Agents
> Madi, Brian, Jason
> Credits to Webvoyager team for the underlying benchmark

## Quickstart
1. `uv sync`
2. `source .venv/bin/activate`

Done!

## Other setup

Make a `run.sh` file, and make sure to fill in the `api_key` with your own `OPENAI_API_KEY`.

nohup python -u run.py \
    --test_file ./data/tasks_test.jsonl \
    --api_key IT_GOES_HERE \
    --max_iter 15 \
    --max_attached_imgs 3 \
    --temperature 1 \
    --fix_box_color \
    --seed 42 > test_tasks.log &

https://leaderboard.steel.dev/
