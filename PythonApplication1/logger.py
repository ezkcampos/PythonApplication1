import logging
import os
import sys

file_handler = logging.FileHandler(
    filename="E:/Cursos/Udemi/Python3/PythonApplication1/PythonApplication1/log/app1.log"
)
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(filename)s] %(levelname)s: %(message)s",
    handlers=handlers,
)
