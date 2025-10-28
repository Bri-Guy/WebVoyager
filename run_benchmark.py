"""
WebVoyager Benchmark Runner

This script provides a programmatic interface to run the WebVoyager benchmark
with predefined settings. It calls run_agent() directly with parameters instead
of using command-line arguments.
"""

from run_single_test import run_agent
from dotenv import load_dotenv

load_dotenv()

def run_benchmark():
    """
    Run the WebVoyager benchmark with predefined settings.
    This is equivalent to run.sh but uses proper Python function calls.
    """
    print("=" * 60)
    print("WebVoyager Benchmark")
    print("=" * 60)
    
    # Configuration
    config = {
        'test_file': './data/tasks_test.jsonl',
        'api_key': os.getenv('OPENAI_API_KEY'),
        'max_iter': 15,
        'max_attached_imgs': 3,
        'temperature': 1.0,
        'seed': 42,
        'api_model': 'gpt-4o',
        'output_dir': 'results',
        'download_dir': 'downloads',
        'window_width': 1024,
        'window_height': 768,
        'fix_box_color': True,
        'headless': False,
        'text_only': False,
        'save_accessibility_tree': False,
        'force_device_scale': False,
    }
    
    # Print configuration
    print("\nConfiguration:")
    print(f"  Test file: {config['test_file']}")
    print(f"  Model: {config['api_model']}")
    print(f"  Max iterations: {config['max_iter']}")
    print(f"  Max attached images: {config['max_attached_imgs']}")
    print(f"  Temperature: {config['temperature']}")
    print(f"  Seed: {config['seed']}")
    print(f"  Window size: {config['window_width']}x{config['window_height']}")
    print(f"  Fix box color: {config['fix_box_color']}")
    print(f"  Headless mode: {config['headless']}")
    print(f"  Output directory: {config['output_dir']}")
    print("=" * 60)
    print()
    
    try:
        # Call run_agent directly with parameters
        run_agent(
            test_file=config['test_file'],
            api_key=config['api_key'],
            max_iter=config['max_iter'],
            max_attached_imgs=config['max_attached_imgs'],
            temperature=config['temperature'],
            seed=config['seed'],
            api_model=config['api_model'],
            output_dir=config['output_dir'],
            download_dir=config['download_dir'],
            window_width=config['window_width'],
            window_height=config['window_height'],
            fix_box_color=config['fix_box_color'],
            headless=config['headless'],
            text_only=config['text_only'],
            save_accessibility_tree=config['save_accessibility_tree'],
            force_device_scale=config['force_device_scale'],
        )
        
        print()
        print("=" * 60)
        print("Benchmark completed successfully!")
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n\nBenchmark interrupted by user.")
        return 1
    except Exception as e:
        print(f"\n\nError during benchmark execution:")
        print(f"  {type(e).__name__}: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(run_benchmark())
