# -*- coding: utf-8 -*-
"""从 skills-bundle.md 还原技能包（Windows / PowerShell 环境）。

  py install_bundle.py skills-bundle.md              # 装全部
  py install_bundle.py skills-bundle.md 技能A 技能B   # 只装指定
  py install_bundle.py skills-bundle.md --list       # 只看包里有什么
  py install_bundle.py skills-bundle.md --dir <技能目录>
"""
import base64
import io
import os
import re
import sys
import zipfile

SKILLS_DIR = os.path.join(
    os.environ.get("LOCALAPPDATA", os.path.expanduser("~/.local/share")),
    "Hermes Agent CN Desktop", "data", "hermes-home", "skills")


def load_bundle(md_path):
    text = io.open(md_path, encoding="utf-8", errors="replace").read()
    if "SKILLBUNDLE-B64" not in text:
        raise SystemExit("文件里没有 SKILLBUNDLE-B64 段，确认拿到的是完整的 skills-bundle.md")
    blocks = re.findall(r"```[a-zA-Z]*\n(.+?)```", text, re.S)
    b64 = ""
    for b in blocks:
        cand = "".join(b.split())
        if b.startswith("SKILLBUNDLE-B64"):
            cand = cand[len("SKILLBUNDLE-B64"):].replace("ENDBUNDLE", "")
        if len(cand) > 1000:
            b64 = cand
            break
    if not b64:
        raise SystemExit("没找到 base64 数据块，文件可能被截断")
    return base64.b64decode(b64)


def main():
    argv = sys.argv[1:]
    if not argv or argv[0].startswith("--"):
        print(__doc__)
        return
    md = argv[0]
    rest = argv[1:]
    skills_dir = SKILLS_DIR
    if "--dir" in rest:
        i = rest.index("--dir")
        skills_dir = rest[i + 1]
        rest = rest[:i] + rest[i + 2:]
    want = {a for a in rest if not a.startswith("--")}

    data = load_bundle(md)
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        tops = sorted({x.split("/")[0] for x in z.namelist() if "/" in x})
        if "--list" in argv:
            print(len(tops), "个技能:", ", ".join(tops))
            return
        n = 0
        for x in z.namelist():
            top = x.split("/")[0]
            if want and top not in want:
                continue
            if x.endswith("/"):
                continue
            dst = os.path.join(skills_dir, x.replace("/", os.sep))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, "wb") as f:
                f.write(z.read(x))
            n += 1
    print("已写入 %d 个文件到 %s" % (n, skills_dir))
    print("重启 Hermes 会话后生效；技能靠 SKILL.md 的 description 触发。")


if __name__ == "__main__":
    main()
