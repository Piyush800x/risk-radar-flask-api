from gemini import genAIModel


def get_high_critical(response):
    high_count = 0
    critical_count = 0

    results = response["results"]
    data = {}
    cveList = []
    for result in results:
        if (float(result["maxCvssBaseScore"])) > 9.0:

            critical_count += 1
        if (float(result["maxCvssBaseScore"]) > 7.5) & (float(result["maxCvssBaseScore"]) < 9.0):
            high += 1
        print(result["cveId"])

    data["high"] = high_count
    data["critical"] = critical_count
    return data


def get_solution(summary: str):
    pass
