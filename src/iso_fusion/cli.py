"""Safe planning CLI. No disk, mount, chroot or ISO modifications."""
import argparse
import json
from pathlib import Path

def plan(paths,workspace_gb):
    if not 1 <= len(paths) <= 3: raise ValueError("Select one to three ISO images")
    if workspace_gb < 80: raise ValueError("At least 80 GiB workspace required")
    return {"mode":"dry-run","inputs":[str(Path(p)) for p in paths],"workspace_gib":workspace_gb,"operations_performed":[],"next_steps":["verify ISO hashes and distro compatibility","inspect package manifests","review filesystem plan","explicitly approve destructive actions"]}

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("isos",nargs="+"); parser.add_argument("--workspace-gib",type=int,default=80); args=parser.parse_args(); print(json.dumps(plan(args.isos,args.workspace_gib),indent=2))
if __name__=="__main__": main()
