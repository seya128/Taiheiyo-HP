# コンテンツ更新ガイド

よく行う更新作業の手順です。すべて `public/` 配下の HTML を直接編集します。

## 施工実績を1件追加する

施工実績は「一覧ページ」と「詳細ページ」の2箇所で構成されています。
新規追加は次の流れです。

### 1. 画像を用意する

`public/img/` に画像を置きます。既存の命名に合わせると管理しやすいです。

- 一覧用サムネイル: `work12.jpg`
- 詳細ページ用: `work12_L.jpg`（大きい外観）、`work12_00.jpg`, `work12_01.jpg` …

> キャッシュ対策として、既存は `?20210816a` のようなクエリを付けています。
> 画像を差し替えた場合はこの値を変えると、閲覧者に新しい画像が確実に表示されます。

### 2. 詳細ページを作る

既存の詳細ページ（例: `works01.html`）をコピーして `works12.html` を作り、
以下を書き換えます。

- `<h3>新築：豊橋市　N邸</h3>` … 物件名
- 概要テキスト（竣工年月・延床面積・間取り・特徴）
- 各 `<img src="img/work01_*.jpg">` … 追加した画像に差し替え
- ページ下部の**ページャー（pagination）**の番号・リンク

### 3. 一覧ページ（works.html）にカードを追加する

`works.html` の該当カテゴリ（住宅 / 店舗 など）の `<div class="wrapper grid">`
内に、次のブロックを追加します。

```html
<div class="item">
    <a href="works12.html">
        <img src="img/work12.jpg?20210816a" alt="実例12">
        <p>新築：豊橋市：○○邸</p>
    </a>
</div>
```

### 4. 表示確認

[development.md](development.md) の手順でローカル表示し、
一覧カード → 詳細ページ → 画像拡大（Lightbox）が正しく動くか確認します。

## テキストを修正する

- 各ページの本文は該当 HTML を直接編集します。
- **ヘッダー・ナビ・フッターは共通化されていない**ため、ナビ項目の追加・変更は
  全 HTML ファイルに同じ修正を反映する必要があります（漏れに注意）。

## 公開（反映）する

編集したら、コミットして `main` に push すれば自動でデプロイされます。

```bash
git add public/
git commit -m "content: 施工実績にworks12を追加"
git push origin main
```

デプロイの確認方法は [deployment.md](deployment.md) を参照してください。

## 迷ったら

- ページの全体像 → [structure.md](structure.md)
- ローカル確認の方法 → [development.md](development.md)
