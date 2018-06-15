# Assignment 3 Delivery

Please follow the provided structure carefully and complete all of the sections described below. The parts that you need to complete are marked with *TODO*.

## Personal information

**Name**: Jostein Hagen Lindhom

List the GitHub usernames of your team here. If you are working alone, then write your GitHub username as the team leader and leave the list of additional team members empty.

**Team leader**: JosteinLindhom

**Additional team members**: KriPet

If you are working as a part of a team, only the a single person, the *team leader* needs to submit the report. If that is not you, then do not edit anything below this point.

----

## Baseline retrieval

Complete the table with baseline retrieval results.

  - For this part, you need to report numbers using the Elasticsearch instance that you access via the API.
  - For the anchor text field, limit results to documents that are present in the "Category B" subset of the collection.

| **Field** | **Output file** | **NDCG@10** | **NDCG@20** |
| -- | -- | -- | -- |
| Title | title_output.txt | 0.128 | 0.114 |
| Content | content_output.txt | 0.138 | 0.128 |
| Anchors | anchors_output.txt | 0.0902 | 0.078 |


List the names of Jupyter notebooks or other code files that were used for producing the results in the above table:
  - 1_Baseline.ipynb


## Learning-to-Rank

Complete the table with learning-to-rank results.

  - These numbers should be obtained using 5-fold cross-validation on the provided queries and relevance judgments.
  - We distinguish between 3 feature groups:
      - [QD] Query-document features
      - [Q] Query features
      - [D] Document features
  - Report on four combinations of feature groups: QD, QD+Q, QD+D, QD+Q+D
  - Use the same training/test folds to make sure the numbers are comparable!

| **Features** | **Output file** | **NDCG@10** | **NDCG@20** |
| -- | -- | -- | -- |
| Only QD features | ltr_qd.txt | 0.1515 | 0.1484 |
| QD + Q features | ltr_qd_q.txt | 0.1520 | 0.1502 |
| QD + D features | ltr_qd_d.txt | 0.1821 | 0.1714 |
| ALL features (QD + Q + D) | ltr_qd_q_d.txt | 0.1663 | 0.1623 |


List the features used with a brief explanation:
  - Query-document features [QD] (min. 6)
    1. BM25 score for Content
    2. BM25 score for Title
    3. BM25 score for Anchors
    4. LM score for Content
    5. LM score for Title
    6. LM score for Anchors
  - Query features [Q] (min. 2)
    1. Query length (sum of terms in query)
    2. Total hits (total hits for a given query)
  - Document features [D] (min. 2)
    1. PageRanks of documents (WE RENAMED THE pagerank.docNameOrder to pagerank.txt)
    2. Content length
	3. Title length

List the names of Jupyter notebooks or other code files that were used for producing the results in the above table:
  - 3_LTR.ipynb
  - 3_LTR_QD.ipynb
  - 3_LTR_QD_Q.ipynb
  - 3_LTR_QD_D.ipynb
  - 3_LTR_QD_Q_D.ipynb
  - pagerank.txt (we renamed pagerank.docNameOrder)
