def get_day(s):
    y, m, d = map(int, s.split('.'))
    return ((y*12)+m)*28+d

def solution(today, terms, privacies):
    terms_dict = {}
    for term in terms:
        term_type, month = term.split()
        terms_dict[term_type] = int(month)
    
    answer = []
    today_int = get_day(today)
    for i, privacy in enumerate(privacies):
        start, term_type = privacy.split()
        start_int = get_day(start)
        term_month = terms_dict[term_type]
        end_int = start_int + term_month*28
        if end_int<=today_int: answer.append(i+1)
    return answer