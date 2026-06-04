#PHASE 2 IMPLEMENTATION (RESEARCH LAYER)
# HALLUCINATION VERIFIER

def verify_answer(answer, context):
    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())

    overlap = len(answer_words.intersection(context_words))
    score = overlap / (len(answer_words) + 1)

    return score > 0.3  # threshold
