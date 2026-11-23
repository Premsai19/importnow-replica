import os
import shutil

src = r"C:\Users\chith\.gemini\antigravity\scratch\importnow-replica"
dest_dirs = [
    r"C:\Users\chith\Desktop\importnow-replica",
    r"C:\Users\chith\OneDrive\Desktop\importnow-replica"
]

pdf_targets = [
    r"C:\Users\chith\Desktop\ImportNow_Assignment_Explanation_Premsai.pdf",
    r"C:\Users\chith\OneDrive\Desktop\ImportNow_Assignment_Explanation_Premsai.pdf"
]

pdf_src = os.path.join(src, "ImportNow_Assignment_Explanation_Premsai.pdf")

for dest in dest_dirs:
    parent = os.path.dirname(dest)
    if os.path.exists(parent):
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
        print(f"Copied full project to {dest}")

for target in pdf_targets:
    parent = os.path.dirname(target)
    if os.path.exists(parent):
        shutil.copy2(pdf_src, target)
        print(f"Copied PDF to {target}")

print("All copies completed successfully!")
