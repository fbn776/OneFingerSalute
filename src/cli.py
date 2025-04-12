import argparse

from src.main import do_hand_detection


def main():
    try:
        argparse.ArgumentParser(description="")
        do_hand_detection()
    except:
        print("An unknown error occurred.")

if __name__ == "__main__":
    main()
