#!/usr/bin/env python3
"""
onboard.py
The Wake-Up Script. Runs at the start of an agent session to load active context.
"""
import os
import json
from pathlib import Path

def generate_spawn_context():
    base_dir = Path(__file__).parent.resolve()
    memory_dir = base_dir / "memory"
    
    # Read the core genome
    try:
        with open(base_dir / "axiom.md", "r") as f:
            axiom = f.read()
    except FileNotFoundError:
        axiom = "No genome found. You are uninitialized."

    # Read the active context
    try:
        with open(memory_dir / "hot.md", "r") as f:
            hot_memory = f.read()
    except FileNotFoundError:
        hot_memory = "No active context."

    # Read hardwired instincts
    try:
        with open(base_dir / "instincts.md", "r") as f:
            instincts = f.read()
    except FileNotFoundError:
        instincts = "No hardwired instincts."

    print("## AGENT CONTEXT — T=spawn")
    print("> You are awake. Read this to know your current state.")
    print("\n### Genome")
    print(axiom)
    print("\n### Hardwired Instincts")
    print(instincts)
    print("\n### Active Memory & Context")
    print(hot_memory)

if __name__ == "__main__":
    _ = generate_spawn_context()
