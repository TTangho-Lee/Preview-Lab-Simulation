#!/usr/bin/env python3
"""
remove_rpyc.py

현재 디렉터리(스크립트 실행 위치 또는 -p 로 지정한 경로)부터
하위 폴더까지 검색하여 .rpyc 파일을 나열하고,
--delete 옵션이 있을 때만 실제로 삭제합니다.
"""

import argparse
from pathlib import Path
import sys

def find_rpyc(root: Path):
    return list(root.rglob("*.rpyc"))

def main():
    parser = argparse.ArgumentParser(description="Find and optionally delete .rpyc files recursively.")
    parser.add_argument("-p", "--path", type=Path, default=Path.cwd(),
                        help="검색 시작 경로 (기본: 현재 작업 디렉터리)")
    parser.add_argument("--delete", action="store_true",
                        help="이 옵션을 주면 실제로 파일을 삭제합니다. 기본은 dry-run(목록만).")
    parser.add_argument("--yes", action="store_true",
                        help="--delete 와 함께 사용하면 추가 확인 없이 바로 삭제합니다.")
    parser.add_argument("-v", "--verbose", action="store_true", help="자세한 출력")
    args = parser.parse_args()

    root = args.path.resolve()


    files = find_rpyc(root)

    # 삭제 진행
    if not args.yes:
        confirm = input(f"\n정말로 {len(files)}개 파일을 삭제하시겠습니까? (yes/NO): ").strip().lower()
        if confirm not in ("y", "yes"):
            print("취소되었습니다.")
            return

    removed = 0
    errors = []
    for f in files:
        try:
            f.unlink()
            removed += 1
            if args.verbose:
                print(f"Deleted: {f}")
        except Exception as e:
            errors.append((f, e))
            print(f"Failed to delete {f}: {e}", file=sys.stderr)

    print(f"\n삭제 완료: {removed}개 삭제, {len(errors)}개 실패.")
    if errors:
        print("실패 목록:")
        for f, e in errors:
            print(f" - {f}: {e}")

if __name__ == "__main__":
    main()
