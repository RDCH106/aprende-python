# Aprende Python
[![Python España](https://img.shields.io/badge/Python-Espa%C3%B1a-blue.svg?maxAge=31536000&logo=github&colorA=e60000&colorB=ffcc12&style=flat)](https://www.es.python.org)
[![License](https://img.shields.io/github/license/rdch106/aprende-python.svg)](https://github.com/RDCH106/aprende-python/blob/master/LICENSE)

📚 Aprende a programar en 🐍 Python

- ⌨️ [Consola Python Online](https://raw.githack.com/RDCH106/aprende-python/master/python-console.html) 
- ⌨️ [IDE Python Online](https://raw.githack.com/RDCH106/aprende-python/master/python-editor.html)

_\*Ambas herramientas usan el proyecto [Brython](https://github.com/brython-dev/brython) como base._

#### ⚖️ Licencia

Toda la obra expuesta en este repositorio está sujeta a licencia [MIT](https://github.com/RDCH106/aprende-python/blob/master/LICENSE), incluyendo tanto las herramientas como el código de snippets y ejercicios.

La obra incluye el software Brython con licencia [BSD 3-Clause](https://github.com/brython-dev/brython/blob/master/LICENCE.txt) compatible con la licencia MIT. El repositorio incluye la licencia en:

https://github.com/RDCH106/aprende-python/blob/master/brython/LICENSE.txt

## Consola Python Online

La Consola Python Online permite usar el intérprete [Brython](https://github.com/brython-dev/brython) como si se tratase del intérprete de Python desde una consola.

Actualmente la Consola Python Online corre sobre: [![Brython](https://img.shields.io/badge/🐍_Brython-3.7.0-blue.svg?style=flat)](https://github.com/brython-dev/brython/releases/tag/3.7.0)

## IDE Python Online 

El IDE Python Online es una adaptación del intérprete [Brython](https://github.com/brython-dev/brython) que permite ejecutar código Python como si del intérprete oficial se tratase.

Actualmente el IDE Python Online corre sobre: [![Brython](https://img.shields.io/badge/🐍_Brython-3.7.0-blue.svg?style=flat)](https://github.com/brython-dev/brython/releases/tag/3.7.0)

Adicionalmente se le ha incluido la posibilidad de cargar código si se facilita la fuente de código durante la llamada al editor usando el parámetro  `code_source`.

**Ejemplo**

Si tenemos el siguiente código de ejemplo en un repositorio GitHub:

- https://github.com/RDCH106/aprende-python/blob/master/js/code_loader/python_code.py

Le damos el botón que pone "*Raw*" y copiamos la url a la que nos lleva:

- https://raw.githubusercontent.com/RDCH106/aprende-python/master/js/code_loader/python_code.py

Con esta url sólo tenemos que llamar al editor de la siguiente forma:

```
https://raw.githack.com/RDCH106/aprende-python/master/python-editor.html?code_source=https://raw.githubusercontent.com/RDCH106/aprende-python/master/js/code_loader/python_code.py
```

👉 [Ver resultado](https://raw.githack.com/RDCH106/aprende-python/master/python-editor.html?code_source=https://raw.githubusercontent.com/RDCH106/aprende-python/master/js/code_loader/python_code.py)

👀 El IDE Python Online puede cargar cualquier código, si la url apunta al recursos directamente, pudiendo cargar código no sólamente alojado en GitHub
