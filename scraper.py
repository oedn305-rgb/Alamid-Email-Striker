import os

def run_radar():
    if os.path.exists("emails.txt"):
        with open("emails.txt", "r") as f:
            lines = f.readlines()
        clean_lines = list(set([line.strip() for line in lines if "@" in line]))
        with open("emails.txt", "w") as f:
            for line in clean_lines:
                f.write(line + "\n")
        print(f"✅ الرادار جاهز. القائمة منقحة وتضم {len(clean_lines)} هدف.")

if __name__ == "__main__":
    run_radar()
