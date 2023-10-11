ls = [
    
    "erd14r7m6drneg69jyxvxxnrsss6x5gg2cqqwreyhdwanj0fcza0ynnq5jmy4g",
    "moa14r7m6drneg69jyxvxxnrsss6x5gg2cqqwreyhdwanj0fcza0ynnqe2atfc",
    
    "erd1qqqqqqqqqqqqqpgq5400a82at6ttplyrdhyn8kk9lhxaed5d0n4s9s77kz",
    "moa1qqqqqqqqqqqqqpgq5400a82at6ttplyrdhyn8kk9lhxaed5d0n4sggc32j",

    "erd1qqqqqqqqqqqqqpgquu5rsa4ee6l4azz6vdu4hjp8z4p6tt8m0n4suht3dy",
    "moa1qqqqqqqqqqqqqpgquu5rsa4ee6l4azz6vdu4hjp8z4p6tt8m0n4s30d735",

    "erd1qqqqqqqqqqqqqpgq4nlkk7jwhqgp4r08lal46tqt70jdv0685u7qrr3l2d",
    "moa1qqqqqqqqqqqqqpgq4nlkk7jwhqgp4r08lal46tqt70jdv0685u7qwmhska",

    "erd1uh67c2lkhyj4vh73akv7jky9sfgvus8awwcj64uju69mmfne5u7q299t7g",
    "moa1uh67c2lkhyj4vh73akv7jky9sfgvus8awwcj64uju69mmfne5u7q8aryzc", 

    "erd1qqqqqqqqqqqqqpgqshqmekudxlxwp0d9j368etjamr5dw7k45u7qx40w6h",
    "erd1qqqqqqqqqqqqqpgqllqglpjdrz5kn3m0k9uf9hdqjmg3xdhk6r7se3wvlk",
    "erd1dyxrt6ky32hpvqh9w9kgt262z4c6su65myzy33styw47m9nkrplqrtnc5r",
    "erd1qqqqqqqqqqqqqpgqju6muu3kj2uqpqwz798g2jeepyn8jwn5rkqsgwvu0x",
    "erd1qqqqqqqqqqqqqpgqfzydqmdw7m2vazsp6u5p95yxz76t2p9rd8ss0zp9ts",
    "erd1spyavw0956vq68xj8y4tenjpq2wd5a9p2c6j8gsz7ztyrnpxrruqzu66jx",
    "erd1l453hd0gt5gzdp7czpuall8ggt2dcv5zwmfdf3sd3lguxseux2fsmsgldz",
    "erd1qqqqqqqqqqqqqpgqcy2wua5cq59y6sxqj2ka3scayh5e5ms7cthqht8xtp",

    "erd1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssycr6th",
    "moa1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssfq94h8",

    "erd1k2s324ww2g0yj38qn2ch2jwctdy8mnfxep94q9arncc6xecg3xaq6mjse8",
    "erd1kyaqzaprcdnv4luvanah0gfxzzsnpaygsy6pytrexll2urtd05ts9vegu7",
    "erd18tudnj2z8vjh0339yu3vrkgzz2jpz8mjq0uhgnmklnap6z33qqeszq2yn4",
    "erd1kdl46yctawygtwg2k462307dmz2v55c605737dp3zkxh04sct7asqylhyv",
    "erd1r69gk66fmedhhcg24g2c5kn2f2a5k4kvpr6jfw67dn2lyydd8cfswy6ede",
    "erd1dc3yzxxeq69wvf583gw0h67td226gu2ahpk3k50qdgzzym8npltq7ndgha",
    "erd13x29rvmp4qlgn4emgztd8jgvyzdj0p6vn37tqxas3v9mfhq4dy7shalqrx",
    "erd1fggp5ru0jhcjrp5rjqyqrnvhr3sz3v2e0fm3ktknvlg7mcyan54qzccnan",
    "erd1z32fx8l6wk9tx4j555sxk28fm0clhr0cl88dpyam9zr7kw0hu7hsx2j524",
    "erd1uv40ahysflse896x4ktnh6ecx43u7cmy9wnxnvcyp7deg299a4sq6vaywa",
    "erd1932eft30w753xyvme8d49qejgkjc09n5e49w4mwdjtm0neld797su0dlxp",
    "erd1pdv0h3ddqyzlraek02y5rhmjnwwapjyhqm983kfcdfzmr6axqhdsfg4akx",
    "erd1rh5ws22jxm9pe7dtvhfy6j3uttuupkepferdwtmslms5fydtrh5sx3xr8r",
    "erd1qqqqqqqqqqqqqpgqhn3ae8dpc957t7jadn7kywtg503dy7pnj9ts3umqxx",
    "erd1qqqqqqqqqqqqqpgqhn3ae8dpc957t7jadn7kywtg503dy7pnj9ts3umqxx",
    "erd1qqqqqqqqqqqqqpgqyfjjn43spw7teklwtpz4x5waygq2mluyj9ts0mdwn6",
    "erd1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqzllls8a5w6u"
]
def checker(tocken, tocken_ls = ls):
    if tocken not in tocken_ls:
        tocken_ls.append(tocken)
        print(f"Tocken added to tocken ls {tocken}")
    else:
        print("Tocken alredy having in ls")

checker("erd1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssycr6th")