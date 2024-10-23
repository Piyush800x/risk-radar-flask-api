from gemini import genAIModel


def get_high_critical(response):
    high_count = 0
    critical_count = 0

    results = response["results"]
    print(response)
    data = {}
    cveResults = []

    temp = {}
    for result in results:
        if (float(result["maxCvssBaseScore"])) > 9.0:
            temp["cveId"] = result["cveId"]
            temp["maxCvssBaseScore"] = result["maxCvssBaseScore"]
            temp["aiSolution"] = get_solution(
                result["summary"], response["productData"]["vendorName"],
                response["productData"]["productName"])

            temp["nvdVulnStatus"] = result["nvdVulnStatus"]
            temp["epssScore"] = result["epssScore"]

            cveResults.append(temp)
            critical_count += 1
        if (float(result["maxCvssBaseScore"]) > 7.5) & (float(result["maxCvssBaseScore"]) < 9.0):
            temp["cveId"] = result["cveId"]
            temp["maxCvssBaseScore"] = result["maxCvssBaseScore"]
            temp["aiSolution"] = get_solution(
                result["summary"], response["productData"]["vendorName"],
                response["productData"]["productName"])

            temp["nvdVulnStatus"] = result["nvdVulnStatus"]
            temp["epssScore"] = result["epssScore"]

            cveResults.append(temp)
            high_count += 1
        print(result["cveId"])

    data["high"] = high_count
    data["critical"] = critical_count
    data["cveResults"] = cveResults
    return data


def get_solution(summary: str, vendorName: str, productName: str):
    prompt = f"""
        Here I have a product named {productName} from {vendorName}.
        This product has a vulnerability and here is the summary: 
        {summary}.
        I want you to give a straight forward solution so that end users can quickly understand what to do to fix the vulnerability.
    """
    response = genAIModel.generate_content(prompt)
    return response.text
