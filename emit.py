#!/usr/bin/env python3
"""
emit.py
The Event Ledger. Logs significant agent decisions and context shifts to memory.
Usage: python3 emit.py event <type> <message>
"""
import sys
import json
import time
from pathlib import Path

def emit_event(event_type: str, message: str):
    base_dir = Path(__file__).parent.resolve()
    memory_dir = base_dir / "memory"
    ledger_file = memory_dir / "events.jsonl"
    
    memory_dir.mkdir(parents=True, exist_ok=True)
    
    event = {
        "timestamp": time.time(),
        "type": event_type,
        "message": message
    }
    
    with open(ledger_file, "a") as f:
        f.write(json.dumps(event) + "\n")
        
    print(f"[{event_type.upper()}] logged to ledger.")

if __name__ == "__main__":
    if len(sys.argv) < 4 or sys.argv[1] != "event":
        print("Usage: python3 emit.py event <type> <message>")
        print("Types: decision, lesson, file_edit, error")
        sys.exit(1)
        
    emit_event(sys.argv[2], sys.argv[3])
