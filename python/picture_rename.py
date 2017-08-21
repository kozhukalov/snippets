import argparse
import os
import subprocess
import hashlib
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", action="store", dest="path_to_image_dir",
                        required=True, help="Path to a directory with images")

    parser.add_argument("--dry-run", action="store_true", dest="dry_run",
                        required=False, default=False, help="Dry run")
    known, others = parser.parse_known_args()

    move_dict = {}
    for n, fn in enumerate(sorted(os.listdir(known.path_to_image_dir))):
        ext = fn.split(".")[-1].lower()
        if ext not in ("png", "jpg", "jpeg"):
            continue
        old = os.path.abspath(os.path.join(known.path_to_image_dir, fn))
        with open(old) as f:
            sha = hashlib.sha256(f.read()).hexdigest()
        new = os.path.abspath(os.path.join(
            known.path_to_image_dir, "{0:03}_{1}.{2}".format(n, sha[:8], ext)))
        move_dict[old] = new
        print("mv {0} {1}".format(old, new))


    if not known.dry_run:
        for old, new in move_dict.items():
            shutil.move(old, new)

        print "ls {0}".format(known.path_to_image_dir)
        for fn in sorted(os.listdir(known.path_to_image_dir)):
            print os.path.abspath(os.path.join(known.path_to_image_dir, fn))


if __name__ == "__main__":
    main()
