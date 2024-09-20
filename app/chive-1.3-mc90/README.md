_(See [GitHub - WorksApplications/chiVe](https://github.com/WorksApplications/chiVe) for the latest README)_

[日本語 README](#chive-sudachi-による日本語単語ベクトル)

# chiVe: Japanese Word Embedding with Sudachi

## Abstract

"chiVe" (Suda**chi Ve**ctor) is a Japanese pre-trained word embedding resource using large-scale corpus and multi-granular tokenization.

Based on the [skip-gram algorithm](https://arxiv.org/abs/1301.3781), we used word2vec ([gensim](https://radimrehurek.com/gensim/)) to train the vectors.

For v1.3, we used texts taken from [CommonCrawl](https://commoncrawl.org/) as a training corpus.

We used [Sudachi](https://github.com/WorksApplications/Sudachi) by Works Applications for tokenization.
We used Sudachi's multi-granular tokenziation results of the corpus to train word vectors.

## Licence

Copyright (c) 2024 Works Applications Co., Ltd. All rights reserved.

"chiVe" v1.3 is distributed by [Works Applications Co.,Ltd.](https://www.worksap.co.jp/) under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Slack

We have a Slack workspace for developers and users to ask questions and discuss a variety of topics.

- https://sudachi-dev.slack.com/
- (Please get an invite from [here](https://join.slack.com/t/sudachi-dev/shared_invite/enQtMzg2NTI2NjYxNTUyLTMyYmNkZWQ0Y2E5NmQxMTI3ZGM3NDU0NzU4NGE1Y2UwYTVmNTViYjJmNDI0MWZiYTg4ODNmMzgxYTQ3ZmI2OWU))

## Citing chiVe

We have published a following paper about chiVe;

- 真鍋陽俊, 岡照晃, 海川祥毅, 髙岡一馬, 内田佳孝, 浅原正幸. [複数粒度の分割結果に基づく日本語単語分散表現](https://www.anlp.jp/proceedings/annual_meeting/2019/pdf_dir/P8-5.pdf) _(Japanese Word Embedding based on Multi-granular Tokenization Results, in Japanese)_. 言語処理学会第 25 回年次大会, 2019.
- 河村宗一郎, 久本空海, 真鍋陽俊, 高岡一馬, 内田佳孝, 岡照晃, 浅原正幸. [chiVe 2.0: Sudachi と NWJC を用いた実用的な日本語単語ベクトルの実現へ向けて](https://www.anlp.jp/proceedings/annual_meeting/2020/pdf_dir/P6-16.pdf) _(chiVe 2.0: Towards Prctical Japanese Embedding wiht Sudachi and NWJC, in Japanese)_. 言語処理学会第 26 回年次大会, 2020.
- 久本空海, 山村崇, 勝田哲弘, 竹林佑斗, 髙岡一馬, 内田佳孝, 岡照晃, 浅原正幸. [chiVe: 製品利用可能な日本語単語ベクトル資源の実現へ向けて](https://www.ieice.org/ken/paper/20200910U1zQ/) _(chiVe: Towards Industrial-strength Japanese Word Vector Resources, in Japanese)_. 第 16 回テキストアナリティクス・シンポジウム, 2020. ([slides](https://speakerdeck.com/sorami/chive-zhi-pin-li-yong-ke-neng-nari-ben-yu-dan-yu-bekutoruzi-yuan-falseshi-xian-hexiang-kete))

When citing chiVe in papers, books, or services, please use the follow BibTex entries (Generally, please cite the first paper, (Manabe+ 2019));

```
@INPROCEEDINGS{manabe2019chive,
    author    = {真鍋陽俊, 岡照晃, 海川祥毅, 髙岡一馬, 内田佳孝, 浅原正幸},
    title     = {複数粒度の分割結果に基づく日本語単語分散表現},
    booktitle = "言語処理学会第25回年次大会(NLP2019)",
    year      = "2019",
    pages     = "NLP2019-P8-5",
    publisher = "言語処理学会",
}
```

```
@INPROCEEDINGS{kawamura2020chive,
    author    = {河村宗一郎, 久本空海, 真鍋陽俊, 高岡一馬, 内田佳孝, 岡照晃, 浅原正幸},
    title     = {chiVe 2.0: SudachiとNWJCを用いた実用的な日本語単語ベクトルの実現へ向けて},
    booktitle = "言語処理学会第26回年次大会(NLP2020)",
    year      = "2020",
    pages     = "NLP2020-P6-16",
    publisher = "言語処理学会",
}
```

```
@INPROCEEDINGS{hisamoto2020chive,
    author    = {久本空海, 山村崇, 勝田哲弘, 竹林佑斗, 髙岡一馬, 内田佳孝, 岡照晃, 浅原正幸},
    title     = {chiVe: 製品利用可能な日本語単語ベクトル資源の実現へ向けて},
    booktitle = "第16回テキストアナリティクス・シンポジウム",
    year      = "2020",
    pages     = "IEICE-NLC2020-9",
    publisher = "電子情報通信学会",
}
```

---

_（最新の README は [GitHub - WorksApplications/chiVe](https://github.com/WorksApplications/chiVe) を参照してください）_

# chiVe: Sudachi による日本語単語ベクトル

[English README](#chive-japanese-word-embedding-with-sudachi)

## 概要

"chiVe" (チャイブ, Suda**chi Vec**tor) は、大規模コーパスと複数粒度分割に基づく日本語単語ベクトルです。

[Skip-gram アルゴリズム](https://arxiv.org/abs/1301.3781)を元に、word2vec （[gensim](https://radimrehurek.com/gensim/)） を使用して単語分散表現を構築しています。

v1.3 では [CommonCrawl](https://commoncrawl.org/) から取得したウェブページ文章を学習コーパスに採用しています。

分かち書きにはワークスアプリケーションズの形態素解析器 [Sudachi](https://github.com/WorksApplications/Sudachi) を使用しています。
Sudachi で定義されている A/B/C の 3 つの分割単位でコーパスを解析した結果を元に分散表現の学習を行なっています。

## ライセンス

Copyright (c) 2024 Works Applications Co., Ltd. All rights reserved.

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) の下で[株式会社ワークスアプリケーションズ](https://www.worksap.co.jp/)によって提供されています。

## Slack

開発者やユーザーの方々が質問したり議論するための Slack ワークスペースを用意しています。

- https://sudachi-dev.slack.com/
- ([こちら](https://join.slack.com/t/sudachi-dev/shared_invite/enQtMzg2NTI2NjYxNTUyLTMyYmNkZWQ0Y2E5NmQxMTI3ZGM3NDU0NzU4NGE1Y2UwYTVmNTViYjJmNDI0MWZiYTg4ODNmMzgxYTQ3ZmI2OWU)から招待を受けてください)

## chiVe の引用

chiVe について、論文を発表しています;

- 真鍋陽俊, 岡照晃, 海川祥毅, 髙岡一馬, 内田佳孝, 浅原正幸. [複数粒度の分割結果に基づく日本語単語分散表現](https://www.anlp.jp/proceedings/annual_meeting/2019/pdf_dir/P8-5.pdf). 言語処理学会第 25 回年次大会, 2019.
- 河村宗一郎, 久本空海, 真鍋陽俊, 高岡一馬, 内田佳孝, 岡照晃, 浅原正幸. [chiVe 2.0: Sudachi と NWJC を用いた実用的な日本語単語ベクトルの実現へ向けて](https://www.anlp.jp/proceedings/annual_meeting/2020/pdf_dir/P6-16.pdf). 言語処理学会第 26 回年次大会, 2020.
- 久本空海, 山村崇, 勝田哲弘, 竹林佑斗, 髙岡一馬, 内田佳孝, 岡照晃, 浅原正幸. [chiVe: 製品利用可能な日本語単語ベクトル資源の実現へ向けて](https://www.ieice.org/ken/paper/20200910U1zQ/). 第 16 回テキストアナリティクス・シンポジウム, 2020. （[スライド](https://speakerdeck.com/sorami/chive-zhi-pin-li-yong-ke-neng-nari-ben-yu-dan-yu-bekutoruzi-yuan-falseshi-xian-hexiang-kete)）

chiVe を論文や書籍、サービスなどで引用される際には、以下の BibTex をご利用ください（基本的には、1 本目の(真鍋+ 2019)を引用してください）。

```
@INPROCEEDINGS{manabe2019chive,
    author    = {真鍋陽俊, 岡照晃, 海川祥毅, 髙岡一馬, 内田佳孝, 浅原正幸},
    title     = {複数粒度の分割結果に基づく日本語単語分散表現},
    booktitle = "言語処理学会第25回年次大会(NLP2019)",
    year      = "2019",
    pages     = "NLP2019-P8-5",
    publisher = "言語処理学会",
}
```

```
@INPROCEEDINGS{kawamura2020chive,
    author    = {河村宗一郎, 久本空海, 真鍋陽俊, 高岡一馬, 内田佳孝, 岡照晃, 浅原正幸},
    title     = {chiVe 2.0: SudachiとNWJCを用いた実用的な日本語単語ベクトルの実現へ向けて},
    booktitle = "言語処理学会第26回年次大会(NLP2020)",
    year      = "2020",
    pages     = "NLP2020-P6-16",
    publisher = "言語処理学会",
}
```

```
@INPROCEEDINGS{hisamoto2020chive,
    author    = {久本空海, 山村崇, 勝田哲弘, 竹林佑斗, 髙岡一馬, 内田佳孝, 岡照晃, 浅原正幸},
    title     = {chiVe: 製品利用可能な日本語単語ベクトル資源の実現へ向けて},
    booktitle = "第16回テキストアナリティクス・シンポジウム",
    year      = "2020",
    pages     = "IEICE-NLC2020-9",
    publisher = "電子情報通信学会",
}
```
