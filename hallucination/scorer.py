#CONFIDENCE SCORING
def confidence_score(query, docs):
    return min(len(docs) / 5.0, 1.0)
