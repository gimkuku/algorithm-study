def solution(id_list, report, k):

    reported_count = {reportee: set([]) for reportee in id_list}
    mail_count = {reporter: 0 for reporter in id_list}

    for single_report in report:
        reporter, reportee = single_report.split()

        reported_count[reportee].add(reporter)

    for (reportee, reporters) in reported_count.items():
        if len(reporters) >= k:
            for reporter in reporters:
                mail_count[reporter] += 1

    return list(mail_count.values())


solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
