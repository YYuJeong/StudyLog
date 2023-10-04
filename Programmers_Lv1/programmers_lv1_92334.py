def solution(id_list, report, k):
    answer = []
    dic = {id: {"reported_me": set(), "mail": 0} for id in id_list}
    for rep in report:
        reporter, reported = rep.split()

        dic[reported]["reported_me"].add(reporter)

    for key in dic:
        if len(dic[key]["reported_me"]) >= k:
            for user in dic[key]["reported_me"]:
                dic[user]["mail"] += 1

    mails = [value["mail"] for value in dic.values()]
    return mails
