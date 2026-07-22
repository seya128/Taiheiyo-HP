# デプロイ

ブランチごとに 2 系統でデプロイします。

```
staging ブランチに push  →  GitHub Pages（確認用サイト）
main    ブランチに push  →  FTPS で本番サーバーへ
```

いずれも公開対象は `public/` 配下のみです。

| ブランチ | デプロイ先 | ワークフロー |
|---|---|---|
| `staging` | GitHub Pages（確認用） | [`deploy-pages.yml`](../.github/workflows/deploy-pages.yml) |
| `main` | 本番サーバー（FTPS） | [`deploy-ftps.yml`](../.github/workflows/deploy-ftps.yml) |

どちらも `workflow_dispatch` を設定しているので、GitHub の Actions タブから手動実行も可能です。

---

## staging → GitHub Pages（確認用）

`staging` ブランチへ push すると、`public/` 配下が
GitHub Pages（https://seya128.github.io/Taiheiyo-HP/）へデプロイされます。

```
staging に push
   ↓
① Checkout（リポジトリ取得）
   ↓
② public/ を公開用アーティファクトに変換
   ↓
③ GitHub Pages へデプロイ
   ↓
確認用サイトに反映（30秒〜1分程度）
```

### 前提設定

- リポジトリ Settings → Pages → Source = **GitHub Actions**
- `github-pages` 環境の Deployment branches に **`staging`** を許可
  （Settings → Environments → github-pages → Deployment branches and tags）

---

## main → FTPS 本番サーバー

`main` ブランチへ push すると、`public/` 配下が FTPS で本番サーバーの
`/public_html/` へ転送されます（[`SamKirkland/FTP-Deploy-Action`](https://github.com/SamKirkland/FTP-Deploy-Action) を使用）。

```
main に push
   ↓
① Checkout（リポジトリ取得）
   ↓
② FTPS で public/ を本番サーバーへ転送
   ↓
本番サイトに反映
```

### 前提設定：GitHub Secrets

リポジトリ Settings → Secrets and variables → Actions で以下を登録します。

| Secret | 内容 |
|---|---|
| `FTP_SERVER` | 本番サーバーのホスト名（例: `ftp.example.com`） |
| `FTP_USERNAME` | FTPS ユーザー名 |
| `FTP_PASSWORD` | FTPS パスワード |

### 設定値

- プロトコル: **FTPS**（暗号化FTP）
- 転送元: `./public/`
- 転送先（server-dir）: `/public_html/`

※ 転送先ディレクトリやポートが異なる場合は
  [`deploy-ftps.yml`](../.github/workflows/deploy-ftps.yml) の `server-dir` などを調整してください。

---

## デプロイ結果の確認

```bash
gh run list --limit 5          # 直近の実行一覧
gh run watch <run-id>          # 実行中のログを追う
gh api repos/seya128/Taiheiyo-HP/pages --jq '.html_url,.status'  # Pages の状態
```
