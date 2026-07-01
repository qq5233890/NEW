"""
AzurPilot 一键启动器。

双击运行即可启动 WebUI 并在浏览器中打开。
按 Ctrl+C 停止服务。
"""
import os
import sys
import subprocess
import time
import webbrowser
import signal
import threading


def get_venv_python():
    root = os.path.dirname(os.path.abspath(__file__))
    venv = os.path.join(root, '.venv')
    if sys.platform == 'win32':
        python = os.path.join(venv, 'Scripts', 'python.exe')
    else:
        python = os.path.join(venv, 'bin', 'python')
    if os.path.exists(python):
        return python
    return sys.executable


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    python = get_venv_python()
    gui_path = os.path.join(root, 'gui.py')
    port = '25548'

    print('=' * 60)
    print('  AzurPilot 启动中...')
    print('=' * 60)
    print()

    env = os.environ.copy()
    env['PYTHONUNBUFFERED'] = '1'

    proc = subprocess.Popen(
        [python, gui_path],
        cwd=root,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )

    def print_output():
        url_shown = False
        for line in proc.stdout:
            print(line, end='')
            if not url_shown and 'Uvicorn running on' in line:
                url_shown = True
                time.sleep(1)
                webbrowser.open(f'http://127.0.0.1:{port}')
                print()
                print('=' * 60)
                print(f'  浏览器已打开: http://127.0.0.1:{port}')
                print('  关闭本窗口即可停止 AzurPilot')
                print('=' * 60)

    thread = threading.Thread(target=print_output, daemon=True)
    thread.start()

    def shutdown(sig, frame):
        print()
        print('正在关闭 AzurPilot...')
        proc.terminate()
        proc.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    try:
        proc.wait()
    except KeyboardInterrupt:
        shutdown(None, None)


if __name__ == '__main__':
    main()