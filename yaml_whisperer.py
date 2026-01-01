#!/usr/bin/env python3
"""YAML Whisperer - Because YAML should whisper, not scream in production."""

import sys
import yaml
from pathlib import Path

# YAML: Yet Another Markup Language (or Yelling At My Laptop)

def whisper_to_yaml(filepath):
    """Gently ask YAML if it's feeling okay today."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # The moment of truth - will YAML cooperate or throw a tantrum?
        yaml.safe_load(content)
        print(f"✅ {filepath}: YAML is whispering sweet nothings (valid!)")
        return True
    except yaml.YAMLError as e:
        # YAML decided to speak up about its feelings
        print(f"🔴 {filepath}: YAML is screaming about indentation!")
        print(f"   Error: {str(e).split('line')[0] if 'line' in str(e) else str(e)[:60]}...")
        return False
    except Exception as e:
        # Something else went wrong - probably a missing file
        print(f"❓ {filepath}: YAML is hiding! {e}")
        return False

def main():
    """Main function - because every script needs one, apparently."""
    if len(sys.argv) < 2:
        print("Usage: python yaml_whisperer.py <file1.yaml> [file2.yaml ...]")
        print("Example: python yaml_whisperer.py k8s/*.yaml")
        sys.exit(1)
    
    print("🔍 Listening for YAML whispers...\n")
    
    all_valid = True
    for arg in sys.argv[1:]:
        path = Path(arg)
        if path.is_file() and (path.suffix in ['.yaml', '.yml']):
            if not whisper_to_yaml(path):
                all_valid = False
        elif path.is_dir():
            # Recursively check all YAML files in directory
            for yaml_file in path.rglob('*.yaml'):
                if not whisper_to_yaml(yaml_file):
                    all_valid = False
            for yml_file in path.rglob('*.yml'):
                if not whisper_to_yaml(yml_file):
                    all_valid = False
    
    print("\n" + "="*50)
    if all_valid:
        print("🎉 All YAML files are whispering peacefully!")
        sys.exit(0)
    else:
        print("💥 Some YAML files are screaming! Check above.")
        sys.exit(1)

if __name__ == "__main__":
    # PyYAML is the only non-stdlib dependency - worth it to avoid regex hell
    try:
        import yaml
    except ImportError:
        print("Error: PyYAML not found. Install with: pip install pyyaml")
        sys.exit(1)
    
    main()