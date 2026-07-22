# 太平洋設計事務所 Webサイト

愛知県豊橋市の設計事務所「太平洋設計事務所」の公式Webサイトです。
ビルドツールを使わない静的なHTML / CSS / JavaScript で構成されています。

## 公開URL

- 本番（FTPS）: 本番サーバー（`/public_html/`）
- 確認用（GitHub Pages）: https://seya128.github.io/Taiheiyo-HP/

GitHub Actions により、ブランチごとに以下の2系統でデプロイされます。

- `main` へ push → **FTPS で本番サーバーへ**転送
- `staging` へ push → **GitHub Pages（確認用）**へデプロイ

いずれも `public/` 配下のみが対象です。

## リポジトリ構成

```
Taiheiyo-HP/
├── README.md              このファイル
├── docs/                  プロジェクトのドキュメント
├── public/                公開されるサイト本体（HTML/CSS/JS/画像）
└── .github/workflows/     GitHub Actions（deploy-ftps.yml / deploy-pages.yml）
```

## ドキュメント

| ドキュメント | 内容 |
|---|---|
| [docs/development.md](docs/development.md) | ローカルでの表示確認・開発手順 |
| [docs/structure.md](docs/structure.md) | サイトのページ構成・ディレクトリ構成 |
| [docs/deployment.md](docs/deployment.md) | デプロイの仕組みと今後の構成（本番FTPS化） |
| [docs/content-guide.md](docs/content-guide.md) | コンテンツ（施工実績など）の更新手順 |

## クイックスタート

```bash
# ローカルで表示確認（Python が入っていれば）
cd public
python3 -m http.server 8000
# → ブラウザで http://localhost:8000 を開く
```

詳細は [docs/development.md](docs/development.md) を参照してください。
