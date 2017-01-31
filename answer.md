このスクリプトではキーワードごとにAPIにリクエストを行い、レスポンス中の ```numFound``` を使ってそれぞれのキーワードの出現回数を数えました。

例えば

```
AKB NMB HKT SKE JKT
```

という入力では

```
http://54.92.123.84/search?ackey=869388c0968ae503614699f99e09d960f9ad3e12&sort=ReleaseDate asc&rows=1&q=Body:AKB
http://54.92.123.84/search?ackey=869388c0968ae503614699f99e09d960f9ad3e12&sort=ReleaseDate asc&rows=1&q=Body:NMB
http://54.92.123.84/search?ackey=869388c0968ae503614699f99e09d960f9ad3e12&sort=ReleaseDate asc&rows=1&q=Body:HKT
http://54.92.123.84/search?ackey=869388c0968ae503614699f99e09d960f9ad3e12&sort=ReleaseDate asc&rows=1&q=Body:SKE
http://54.92.123.84/search?ackey=869388c0968ae503614699f99e09d960f9ad3e12&sort=ReleaseDate asc&rows=1&q=Body:JKT
```

というURLが5つ生成されデータの取得を行います。

苦労したところは特にありませんが、ローカルで ```codecheck``` コマンドを実行するとテストケースはすべて通過したのにもかかわらず、オンラインでは何らかの理由により4つほどしか通過しませんでした。

ローカルで実行した時のログを ```result.txt``` に出力してあります。
