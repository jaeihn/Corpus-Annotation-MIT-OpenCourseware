# Milestone 2 
## Corpus analysis (Optional)

For statistical properties comparison, I choose treebank corpus and webtext corpus, because I think both MIT syllabus corpus and treebank corpus have high amount of proper nouns and terminologies, and the content of both MIT syllabus corpus and webtext corpus are collected from online websites. For analysis, all the calculations of statistical properties can be found in [corpus_analysis.ipynb](corpus_analysis.ipynb).

### Number of words

For number of words, MIT syllabus corpus has 6256086 words, treebank corpus has 100676 words, and webtext corpus has 396733 words. I think the reason why MIT syllabus corpus has much more words is because there are around 2500 syllabuses and each syllabus has very detailed description of a course.

### Average word length

For average word length, MIT syllabus corpus's is 6.143507298333175, treebank's is 4.406154396281139, webtext's is 3.552701691061747. I think the reason why the average word length of MIT syllabus corpus is the highest is because it has more proper nouns including author's name and academic terminology. Webtext has the lowest may be because most of the word in webtext comes from online discussion forums and they are mostly simple daily English words.

### Average text lengths

For Average text lengths, MIT syllabus corpus's is 2560.821121571838, webtext's is 66122.16666666667, treebank's is 505.90954773869345. I think the reason why webtext's is the highest is because it has least amount of texts which is only 6.

### Type token radio

For type token radio, MIT syllabus corpus's is 0.11294314048751887, webtext's is 0.05428840051117502, treebank's is 0.12324685128531129. MIT syllabus corpus's is close to treebank's and webtext's is much lower. I think MIT syllabus corpus and treebank have higher lexical richness may be because they have more proper nouns and terminologies.

### Associated words

MIT syllabus corpus
['chapters', 'urban', 'learning', 'their', 'd.', 'write', 'case', 'video', 'de', 'may', 'presentation', 'c.', 'data', 'american', 'assignments', 'sessions', 'development', 'used', 'exam', 'due', '5', 'study', '=', 'week,', 'reading', 'assignment', 'following', 'use', 'our', 'writing', 'questions', 'introduction', 'r.', 'google', 's.', 'part', 'discussion', 'ed.', '[preview', 'social', 'theory', 'session', 'p.', 'an', 'student', 'a.', 'readings', 'analysis', 'al.', 'research', 'm.', 'problem', 'edited', 'these', '(pdf)', '4', 'science', 'review', 'this', 'et', 'journal', 'york,', '(pdf', 'design', 'ny:', 'lecture', 'j.', 'mit', 'paper', 'we', '/', 'with', '3', 'as', 'project', 'or', 'final', 'each', '“the', 'are', 'how', 'university', 'set', 'by', 'chapter', 'be', 'class', 'students', 'press,', 'pp.', 'your', 'no.', 'course', 'for', 'will', 'isbn:', 'in', 'the', 'of', 'and']

treebank
['many', 'bonds', 'but', 'investment', 'recent', 'companies', 'such', 'last', 'profit', 'department', 'executive', 'yesterday', 'bank', 'price', 'funds', 'exchange', 'cents', 'investors', 'stocks', 'board', 'could', '*ich*-1', 'index', 'futures', 'because', 'japan', 'federal', 'co.', 'sales', 'york', 'from', 'government', 'they', 'japanese', 'who', 'prices', 'their', 'years', 'more', 'inc.', '*t*-3', 'new', 'been', 'also', 'had', '-lrb-', 'an', 'than', '-rrb-', 'shares', 'share', 'corp.', 'as', 'program', 'were', 'would', 'he', '*-3', ';', 'which', 'billion', 'president', 'for', 'was', 'trading', 'stock', 'by', 'market', '--', 'at', 'year', 'says', 'u.s.', 'that', 'has', 'company', 'of', 'in', 'its', "n't", '*t*-2', '*-2', 'mr.', 'million', 'to', '%', 'a', 'said', "''", '``', '$', '*u*', '*t*-1', "'s", '*', '0', '*-1', 'the', '.', ',']

webtext
['too', 'shit', 'little', 'after', 'back', 'have', 'think', 'manager', 'got', 'want', 'crash', 'dude', 'll', 'there', 'him', 'black', 'button', 'old', 'going', 'well', 'very', 'her', 'really', 'download', 'url', 'out', 'jack', 'right', 'good', 'go', 'bookmark', 'browser', 'boy', '***', 'all', 'lady', 'cell', 'toolbar', 'bar', 'tab', 'menu', 'does', 'he', 'up', 'firebird', 'do', 'but', 'teen', 'bookmarks', 'doesn', 'open', 'if', 'she', 'window', 'can', 'oh', ')', 'get', 'chick', 'page', 're', 'what', 'just', 'firefox', 'yeah', '(', 'know', 'on', 'woman', 'man', 'so', 'm', 'no', 'don', '[', ']', '2', 'me', 'my', 'like', 'when', '...', 'it', '1', 'not', '"', ',', '-', 'guy', 'girl', 's', 't', '#', '!', '?', 'you', 'i', '.', "'", ':']

According to the result above, I think the words associated with MIT syllabus corpus are mostly academic missions for the course, such as reading, assignment, discussion, lecture, etc. And I think those are the metadata of the MIT syllabus corpus. Because of those metadata, MIT syllabus corpus has more proper nouns and academic terminologies so that average word length and type token radio are higher. The words associated with treebank are from different backgrounds since they are from different journal articles. And the words associated with webtext are mostly daily English words and pronouns because they are collected mostly from online discussion forums.
