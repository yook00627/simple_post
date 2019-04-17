from flask import Flask, request, jsonify

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/test")
def entry_page():
    return "entry_page"


@app.route("/test", methods=["POST"])
def cut_string():
    result = dict()
    json = request.get_json()
    if json is not None:
        if "string_to_cut" in json:
            string = get_third_letter(json["string_to_cut"])
            result["return_string"] = string
    return jsonify(result)


# function to get the third character of string
def get_third_letter(string):
    result = ""
    if string is None or string == "":
        return result
    count = 1
    for char in string:
        if count % 3 == 0:
            result += char
        count += 1
    return result


if __name__ == "__main__":
    app.run(port=5000)
