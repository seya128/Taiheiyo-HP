#!/usr/bin/env python3
"""public/ 配下を FTPS で本番サーバー(/public_html)へアップロードする。

BIGLOBE の FTPS サーバーは MLSD を広告しておらず、
FTP-Deploy-Action(MLSD前提) や lftp のディレクトリ走査と相性が悪い。
動作実証済みの標準ライブラリ ftplib(FTP_TLS) で確実に転送する。

必要な環境変数:
  FTP_SERVER   ホスト名 (例: ftps.biglobe.ne.jp)
  FTP_USERNAME ユーザー名
  FTP_PASSWORD パスワード

既定では既存ファイルの削除は行わず、上書き・追加のみ。
"""
import os
import ssl
import sys
from ftplib import FTP_TLS, error_perm

LOCAL_DIR = "public"
REMOTE_DIR = "/public_html"


def cd_or_make(ftp, path):
    """path まで移動。無ければ 1 階層ずつ作成して移動する。"""
    if path in ("", "/"):
        ftp.cwd("/")
        return
    try:
        ftp.cwd(path)
        return
    except error_perm:
        pass
    parent, _, child = path.rpartition("/")
    cd_or_make(ftp, parent)
    try:
        ftp.mkd(child)
        print(f"  📁 created {path}")
    except error_perm as e:
        # 既に存在する等は無視
        if not str(e).startswith(("550", "521")):
            raise
    ftp.cwd(child)


def main():
    try:
        server = os.environ["FTP_SERVER"]
        user = os.environ["FTP_USERNAME"]
        password = os.environ["FTP_PASSWORD"]
    except KeyError as e:
        sys.exit(f"環境変数が未設定です: {e}")

    ctx = ssl._create_unverified_context()
    ftp = FTP_TLS(context=ctx)
    ftp.encoding = "utf-8"
    print(f"接続中: {server}")
    ftp.connect(server, 21, timeout=30)
    ftp.login(user, password)
    ftp.prot_p()          # データチャネルも暗号化
    ftp.set_pasv(True)
    print("ログイン成功")

    # 診断: ランナーから CWD が通るか（IP制限の切り分け）
    try:
        ftp.cwd(REMOTE_DIR)
        print(f"CWD {REMOTE_DIR} OK")
    except Exception as e:
        print(f"CWD {REMOTE_DIR} 失敗: {e!r}")
        raise

    count = 0
    # top-down: 親ディレクトリから順に処理される
    for root, _dirs, files in os.walk(LOCAL_DIR):
        rel = os.path.relpath(root, LOCAL_DIR)
        if rel == ".":
            remote_dir = REMOTE_DIR
        else:
            remote_dir = f"{REMOTE_DIR}/{rel.replace(os.sep, '/')}"
        cd_or_make(ftp, remote_dir)
        for name in sorted(files):
            local_path = os.path.join(root, name)
            with open(local_path, "rb") as fh:
                ftp.storbinary(f"STOR {name}", fh)
            count += 1
            print(f"  ⬆ {remote_dir}/{name}")

    ftp.quit()
    print(f"完了: {count} ファイルを転送しました。")


if __name__ == "__main__":
    main()
