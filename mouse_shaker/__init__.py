import sys, random, time
import pyautogui


def shake_mouse(duration: float):
    W, H = pyautogui.size()
    pyautogui.moveTo(100, 100)
    start = time.time()

    num_shakes = 0
    while time.time() - start < duration:
        pyautogui.moveTo(
            x=random.randint(0, W),
            y=random.randint(0, H),
            duration=random.uniform(0.5, 3),
            tween=pyautogui.easeInOutQuad,
        )
        num_shakes += 1
    print(f"Total number of shakes: {num_shakes}")


def parse_duration(arg: str):
    if "s" in arg:
        return float(arg.replace("s", ""))
    elif "min" in arg:
        return float(arg.replace("min", "")) * 60
    else:
        return float(arg)

def cli_main():
    duration = 5  # default seconds
    if len(sys.argv) > 1:
        duration = parse_duration(sys.argv[1].lower())
    shake_mouse(duration)
    

if __name__ == "__main__":
    cli_main()

    