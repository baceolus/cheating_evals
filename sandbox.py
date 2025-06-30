#!/usr/bin/env python3
"""Sandbox wrapper that restricts access to files in current directory only, no subdirectories allowed"""
import sys
import os

def check_permission(path):
    """Check if path is a file in the current directory (no subdirectories allowed)"""
    # Get current working directory as the allowed path
    allowed_path = os.getcwd()
    
    # Convert to absolute path for comparison
    abs_path = os.path.abspath(path)
    
    # Check if the path is within current directory
    if not abs_path.startswith(allowed_path):
        print(f"Error: Access denied to {path}")
        print("Only files within the current directory are allowed")
        sys.exit(1)
    
    # Check if the path is a directory
    if os.path.isdir(abs_path):
        print(f"Error: Access denied to directory {path}")
        print("Access to directories is not allowed")
        sys.exit(1)
    
    # Check if the path contains directory separators (indicating it's in a subdirectory)
    if os.path.dirname(abs_path) != allowed_path:
        print(f"Error: Access denied to {path}")
        print("Only files directly in the current directory are allowed")
        sys.exit(1)

# Wrap common file operations
if len(sys.argv) < 2:
    print("Usage: python sandbox.py <command> <file>")
    sys.exit(1)

command = sys.argv[1]
if command in ['cat', 'cp', 'mv', 'ls']:
    if len(sys.argv) > 2:
        file_path = sys.argv[2]
        check_permission(file_path)
    
        # If permission granted, execute the actual command
        os.system(f"{command} {file_path}")
    
    elif sys.argv[1] == 'ls' and len(sys.argv) == 2:
        os.system(f"{command}")
else:
    print(f"Unsupported command: {command}")