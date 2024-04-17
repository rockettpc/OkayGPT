# OkayGPT!

This is a fork of https://github.com/unconv/ok-gpt

Currently it can detect a wakeup keyphrase, such as "Ok, GPT!" and then listen to a voice command. Speech recognition is done with OpenAI Whisper, locally. The command is then sent to the ChatGPT API and the response is spoken via the OpenAI Text-to-Speech API.

You need to initialize it with the `init.py` script by saying the keyphrase you want to wake up the device with 10 times. After that you can run `recognize.py` and it will recognize when you say the keyphrase and then listen for the command.

## Quick Start

```shell
$ export OPENAI_API_KEY=YOUR_API_KEY
$ pip install -r requirements.txt
$ python3 init.py
$ python3 recognize.py
```

## Videos

The building of this project is documented on the Unconventional Coding YouTube channel.

- Video 1: https://www.youtube.com/watch?v=_vLKWNv4d5E
- Video 2: https://www.youtube.com/watch?v=xQdLiyCxyWQ

Additional Info: 

## When trying to install pygobject

you get this error or similar

```
ip install pygobject
Collecting pygobject
  Downloading pygobject-3.48.2.tar.gz (715 kB)
     |████████████████████████████████| 715 kB 4.3 MB/s 
  Installing build dependencies ... error
  ERROR: Command errored out with exit status 1:
   command: /home/ryan/Documents/VSCode/OkayGPT/okaygpt_venv/bin/python3 /home/ryan/Documents/VSCode/OkayGPT/okaygpt_venv/lib/python3.9/site-packages/pip install --ignore-installed --no-user --prefix /tmp/pip-build-env-68rnv4w5/overlay --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- 'meson-python>=0.12.1' 'pycairo>=1.16'
       cwd: None
  Complete output (46 lines):
  Collecting meson-python>=0.12.1
    Downloading meson_python-0.16.0-py3-none-any.whl (26 kB)
  Collecting pycairo>=1.16
    Using cached pycairo-1.26.0.tar.gz (346 kB)
    Installing build dependencies: started
    Installing build dependencies: finished with status 'done'
    Getting requirements to build wheel: started
    Getting requirements to build wheel: finished with status 'done'
    Installing backend dependencies: started
    Installing backend dependencies: finished with status 'done'
      Preparing wheel metadata: started
      Preparing wheel metadata: finished with status 'done'
  Collecting meson>=0.63.3
    Downloading meson-1.4.0-py3-none-any.whl (935 kB)
  Collecting pyproject-metadata>=0.7.1
    Downloading pyproject_metadata-0.7.1-py3-none-any.whl (7.4 kB)
  Collecting packaging>=19.0
    Downloading packaging-24.0-py3-none-any.whl (53 kB)
  Collecting tomli>=1.0.0
    Downloading tomli-2.0.1-py3-none-any.whl (12 kB)
  Building wheels for collected packages: pycairo
    Building wheel for pycairo (PEP 517): started
    Building wheel for pycairo (PEP 517): finished with status 'error'
    ERROR: Command errored out with exit status 1:
     command: /home/ryan/Documents/VSCode/OkayGPT/okaygpt_venv/bin/python3 /tmp/tmph6x9h6qn_in_process.py build_wheel /tmp/tmpqk0j9o4_
         cwd: /tmp/pip-install-qp4do_dn/pycairo_88d3f04fc39a4bfba44bdd27bdcea356
    Complete output (15 lines):
    running bdist_wheel
    running build
    running build_py
    creating build
    creating build/lib.linux-x86_64-cpython-39
    creating build/lib.linux-x86_64-cpython-39/cairo
    copying cairo/__init__.py -> build/lib.linux-x86_64-cpython-39/cairo
    copying cairo/__init__.pyi -> build/lib.linux-x86_64-cpython-39/cairo
    copying cairo/py.typed -> build/lib.linux-x86_64-cpython-39/cairo
    running build_ext
    Package cairo was not found in the pkg-config search path.
    Perhaps you should add the directory containing `cairo.pc'
    to the PKG_CONFIG_PATH environment variable
    No package 'cairo' found
    Command '['pkg-config', '--print-errors', '--exists', 'cairo >= 1.15.10']' returned non-zero exit status 1.
    ----------------------------------------
    ERROR: Failed building wheel for pycairo
  Failed to build pycairo
  ERROR: Could not build wheels for pycairo which use PEP 517 and cannot be installed directly
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/f9/9e/6bab1ed3bd878f0912d9a0600c21f3d88bab0e8a8d4c3ce50f5cf336faaf/pygobject-3.48.2.tar.gz#sha256=c3c0a7afbe5b2c1c64dc0530109b4dd571085153dbedfbccb8ec7c5ad233f977 (from https://pypi.org/simple/pygobject/) (requires-python:<4,>=3.8). Command errored out with exit status 1: /home/ryan/Documents/VSCode/OkayGPT/okaygpt_venv/bin/python3 /home/ryan/Documents/VSCode/OkayGPT/okaygpt_venv/lib/python3.9/site-packages/pip install --ignore-installed --no-user --prefix /tmp/pip-build-env-68rnv4w5/overlay --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- 'meson-python>=0.12.1' 'pycairo>=1.16' Check the logs for full command output.
```

Then:

```
sudo apt-get update
sudo apt-get install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
```
