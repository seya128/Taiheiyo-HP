# サイト構成

## ディレクトリ構成

```
public/
├── index.html              トップページ
├── works.html              施工実績の一覧
├── concept.html            コンセプト
├── about.html              会社概要（COMPANY）
├── service.html            サービス紹介
├── contact.html            お問い合わせ
├── faq.html                よくある質問
├── before.html             （下書き／作業用ページ）
│
├── works01.html 〜 works11.html          施工実績の詳細（11件）
├── works-Store01.html 〜 Store04.html    店舗系の実績詳細（4件）
├── works-project01.html / 02.html        プロジェクト系の実績詳細（2件）
│
├── style.css               メインスタイル
├── ress.css                リセットCSS（ress）
├── lightbox.css /          画像拡大表示（Lightbox）用スタイル
│   lightbox.min.css
├── js/lightbox.js          Lightbox 本体
│
├── favicon.ico             ファビコン（img/favicon.ico にも同じものあり）
├── img/                    画像一式（約190ファイル）
└── work003_*.jpg /         一部の実績画像（ルート直下に配置）
    work004_*.jpg
```

## ナビゲーション

全ページ共通のグローバルナビ:

| ラベル | リンク先 |
|---|---|
| WORKS | works.html |
| CONCEPT | concept.html |
| ABOUT | about.html |
| CONTACT | contact.html |
| FAQ | faq.html |

- ロゴ（`img/logo.svg`）クリックで `index.html` に戻ります。
- スマホ幅ではハンバーガーメニューが表示され、TOP を含む同じ項目が並びます。

## ページの役割

- **index.html** — トップ。メインビジュアルと各セクションへの導線。
- **works.html** — 施工実績の一覧。各 `works*.html` 詳細ページへリンク。
- **concept.html / about.html / service.html** — 事務所の紹介系ページ。
- **contact.html** — お問い合わせ（Googleフォーム等へ誘導）。
- **faq.html** — よくある質問。
- **before.html** — 現状は作業用・下書きと思われるページ。公開ナビからは未リンク。

## 外部依存（CDN・外部サービス）

- jQuery（code.jquery.com）
- Font Awesome（use.fontawesome.com）
- Googleマップ 埋め込み（事務所所在地）
- Googleフォーム（お問い合わせ）

これらはインターネット接続時のみ機能します。

## 既知の気づき（改善候補・任意）

以下は動作に必須ではありませんが、今後整理する場合の候補です。

- 一部ページの `<title>` に表記ゆれ・誤字があります
  （例: `CONSEPT` → `CONCEPT`、contact.html のタイトルが「CONSEPT」、
  about.html / faq.html がともに「COMPANY」）。
- 実績画像の一部（`work003_*` / `work004_*`）が `public/` 直下にあり、
  他は `img/` 配下にあります。将来的に `img/` へ統一すると整理しやすくなります。
- ファビコンが `favicon.ico`（ルート）と `img/favicon.ico` の2箇所に重複しています。
