from elasticsearch import Elasticsearch

INDEX_NAME = "aquaint"
DOC_TYPE = "doc"
FIELDS = ["title", "content"]


def average():
	es = Elasticsearch()
	page = es.search(
		index=INDEX_NAME,
		doc_type=DOC_TYPE,
		scroll='2m',
		size=10000,
		body={
			"query": {
				"match_all": {}
			}
		}
	)

	titles = []
	contents = []
	scroll_id = page['_scroll_id']
	size = page['hits']['total']
	print("Starting ...")
	progress = 100 / 103.3461
	current = 0.0
	while size > 0:
		res = page['hits']['hits']
		for hit in res:
			titles.append(len(hit['_source']['title']))
			contents.append(len(hit['_source']['content']))
		page = es.scroll(scroll_id=scroll_id, scroll='1m')

		scroll_id = page['_scroll_id']
		current += (1 * 10000/ size)
		print(str(round(progress * current, 2)) + "%")
		size = len(page['hits']['hits'])
		

	len_titles = 0
	len_content = 0
	for title in titles:
		len_titles += title
	for content in contents:
		len_content += content
	avg_title =  len_titles / len(titles)
	avg_content = len_content / len(contents)
	print("Average title length: " + str(round(avg_title, 2)))
	print("Average content length: " + str(round(avg_content, 2)))

average()