# デプロイ

デプロイ先は2系統です。

| 対象 | デプロイ先 | 実行方法 |
|---|---|---|
| 確認用 | GitHub Pages | `staging` へ push（GitHub Actions が自動デプロイ） |
| 本番 | BIGLOBE（FTPS） | **ローカルからスクリプト実行**（下記参照） |

いずれも公開対象は `public/` 配下のみです。

---

## 確認用: staging → GitHub Pages（自動）

`staging` ブランチへ push すると、GitHub Actions が `public/` 配下を
GitHub Pages（https://seya128.github.io/Taiheiyo-HP/）へ自動デプロイします。

ワークフロー: [`.github/workflows/deploy-pages.yml`](../.github/workflows/deploy-pages.yml)

### 前提設定

- リポジトリ Settings → Pages → Source = **GitHub Actions**
- `github-pages` 環境の Deployment branches に **`staging`** を許可

---

## 本番: BIGLOBE へ FTPS（ローカルから手動）

### なぜローカル実行なのか

BIGLOBE の FTPS サーバー（`ftps.biglobe.ne.jp`）は、**接続元IPを国内（ISP網）に制限**しています。
このため GitHub Actions などクラウド（海外IP）のランナーからは、ログインはできても
`/public_html` にアクセスできず（`550 Permission denied` / `No such file or directory`）、
自動デプロイができません。

> 検証済みの事実:
> - 海外IP（GitHub ランナー）: ログイン成功 → `PWD`/`CWD` が拒否される
> - 国内IP（手元の回線）: すべて成功
>
> さらにこのサーバーは `MLSD` 非対応のため、`SamKirkland/FTP-Deploy-Action` や
> `lftp` のディレクトリ走査とも相性が悪い。標準ライブラリ `ftplib` を使う
> [`scripts/deploy_ftps.py`](../scripts/deploy_ftps.py) で確実に転送する。

### 手順

1. `main` に最新の変更が反映されていることを確認（通常は staging で確認後に main へマージ）
2. **日本国内の回線から**、リポジトリのルートで以下を実行:

   ```bash
   bash scripts/deploy.local.sh
   ```

   `scripts/deploy.local.sh` は認証情報を含むため `.gitignore` 済み（リポジトリには入っていない）。
   手元に無い場合は、以下の内容で作成する:

   ```bash
   #!/usr/bin/env bash
   set -euo pipefail
   cd "$(dirname "$0")/.."
   export FTP_SERVER="ftps.biglobe.ne.jp"
   export FTP_USERNAME="<ユーザー名>"
   export FTP_PASSWORD="<パスワード>"
   python3 scripts/deploy_ftps.py
   ```

   または環境変数を直接指定して実行:

   ```bash
   FTP_SERVER="ftps.biglobe.ne.jp" FTP_USERNAME="<ユーザー名>" FTP_PASSWORD="<パスワード>" \
     python3 scripts/deploy_ftps.py
   ```

3. `完了: N ファイルを転送しました。` と表示されれば本番反映完了。

### 挙動

- `public/` 配下を `/public_html/` へ**上書き・追加**する（既存ファイルの削除はしない）。
- サブディレクトリ（`img/` `js/` など）が無ければ自動作成する。

### 参考: 転送先の確認（読み取り）

```bash
curl -s --ftp-ssl -k --list-only "ftp://ftps.biglobe.ne.jp/public_html/" \
  --user "<ユーザー名>:<パスワード>"
```
