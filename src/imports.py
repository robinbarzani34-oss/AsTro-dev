import os
import sys
import json
import re
import time
import colorama
from colorama import Fore, Style
import datetime
import pathlib
import argparse
import webbrowser
import socket
import random
import string  
import subprocess
import platform
import shutil
import logging
import typer
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt, Confirm
from rich import print as rprint
from dotenv import load_dotenv
load_dotenv()
console = Console()
app = typer.Typer()