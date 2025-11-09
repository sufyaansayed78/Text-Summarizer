import logging
import os
import sys
from pathlib import Path  
from datetime import datetime    
log_dir = "LOGS" 
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_name = f"log_{timestamp}.log"
log_file_pth = os.path.join(log_dir, log_file_name)
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s]',
                    handlers=[
                        logging.FileHandler(log_file_pth),
                        logging.StreamHandler(sys.stdout)
                    ])
logger = logging.getLogger()