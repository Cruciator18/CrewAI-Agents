#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from autocoder.crew import AutoCoder


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
assignment = "Write a python program to calculate the following for 10,000 terms \
    , multiplying the total by 4 : 1- 1/3 +1/5 -1/7 ....."

def run():
    """
    Run the crew.
    """
    inputs = {"assignment": assignment}
    result = AutoCoder().crew().kickoff(inputs=inputs)
    print(result.raw)
    
