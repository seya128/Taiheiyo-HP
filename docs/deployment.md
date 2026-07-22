# デプロイ

## 現在の構成：GitHub Actions → GitHub Pages

`main` ブランチへ push すると、GitHub Actions が `public/` 配下を
GitHub Pages へ自動デプロイします。

### 仕組み

ワークフロー定義: [`.github/workflows/deploy.yml`](../.github/workflows/deploy.yml)

```
main に push
   ↓
① Checkout（リポジトリ取得）
   ↓
② public/ を公開用アーティファクトに変換
   ↓
③ GitHub Pages へデプロイ
   ↓
https://seya128.github.io/Taiheiyo-HP/ に反映（30秒〜1分程度）
```

`workflow_dispatch` も設定してあるので、GitHub の Actions タブから手動実行も可能です。

### 前提設定（設定済み）

- リポジトリ Settings → Pages → Source = **GitHub Actions**

### デプロイ結果の確認

```bash
gh run list --limit 5          # 直近の実行一覧
gh run watch <run-id>          # 実行中のログを追う
gh api repos/seya128/Taiheiyo-HP/pages --jq '.html_url,.status'
```

---

## 今後の構成案：main=本番FTPS / staging=確認用Pages

本番サーバーが用意でき次第、以下の2系統デプロイに拡張できます。

```
staging ブランチに push  →  GitHub Pages（確認用サイト）
main    ブランチに push  →  FTPS で本番サーバーへ
```

### 進め方の概要

1. ワークフローを2つに分ける
   - `deploy-pages.yml`: トリガーを `staging` に変更
   - `deploy-ftps.yml`: `main` で FTPS デプロイ（例: `SamKirkland/FTP-Deploy-Action`）
2. FTPS接続情報を GitHub Secrets に登録
   - `FTP_SERVER` / `FTP_USERNAME` / `FTP_PASSWORD`
3. `github-pages` 環境の Deployment branches で `staging` を許可
4. 本番サーバーの公開ディレクトリ名（例: `/public_html/`）を `server-dir` に設定

### 事前に確認が必要な情報

- 本番サーバーが **FTPS（暗号化FTP）** に対応しているか
  （可能なら SFTP/SSH の方がさらに安全）
- 本番の公開ディレクトリ名（`/public_html/` `/htdocs/` `/www/` など）
- 転送対象は `public/` 配下のみとする想定

この構成に進める際は、上記情報を揃えてから着手します。
