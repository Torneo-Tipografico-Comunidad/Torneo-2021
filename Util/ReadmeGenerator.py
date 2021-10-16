"""
Genera los archivos README.md para cada equipo
"""

import os
import pathlib

repoPath = pathlib.Path(__file__).parent.parent.resolve()
equiposPath = f'{repoPath}/Equipos'

print(os.listdir(equiposPath))
