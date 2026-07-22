# 開発ガイド

ローカルでサイトを表示・確認するための手順です。ビルドツールは不要です。

## ローカルでの表示確認

サイト本体は `public/` 配下にあります。相対パスで画像やCSSを参照しているため、
ファイルを直接ブラウザで開くのではなく、簡易HTTPサーバー経由での確認を推奨します。

### 方法1: Python（追加インストール不要なことが多い）

```bash
cd public
python3 -m http.server 8000
```

ブラウザで http://localhost:8000 を開きます。

### 方法2: Node.js の場合

```bash
cd public
npx serve .
```

### 方法3: VS Code

拡張機能「Live Server」を入れ、`public/index.html` を右クリック →
「Open with Live Server」。

## 編集の基本

- ページはすべて `public/*.html`。共通スタイルは `public/style.css`。
- ヘッダー / ナビ / フッターは各HTMLに直接書かれています（共通テンプレート機構はありません）。
  そのため**ナビの変更は全ページに手作業で反映**する必要があります。
- CSSの反映が古い場合、`style.css?20210816` のようにクエリでキャッシュ管理しています。
  大きくCSSを変えたら、このバージョン文字列を更新するとキャッシュ切れを防げます。

## 確認しておきたいポイント

- 画像・リンク・レイアウトがPC / スマホ幅の両方で崩れていないか
  （ハンバーガーメニューはスマホ幅で表示されます）
- 外部サービス（Googleマップ、Googleフォーム、jQuery CDN、Font Awesome CDN）は
  オンライン環境でのみ表示されます。

## 関連ドキュメント

- ページ構成の詳細 → [structure.md](structure.md)
- デプロイの流れ → [deployment.md](deployment.md)
- コンテンツ更新手順 → [content-guide.md](content-guide.md)
