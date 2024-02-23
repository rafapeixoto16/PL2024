import re

fileRM = open("./Exemplo.md", "r", encoding="utf-8").read()

fileRM = re.sub(r"###### (.*)", lambda x: "<h6>" + x[1] + "</h6>", fileRM)
fileRM = re.sub(r"##### (.*)", lambda x: "<h5>" + x[1] + "</h5>", fileRM)
fileRM = re.sub(r"#### (.*)", lambda x: "<h4>" + x[1] + "</h4>", fileRM)
fileRM = re.sub(r"### (.*)", lambda x: "<h3>" + x[1] + "</h3>", fileRM)
fileRM = re.sub(r"## (.*)", lambda x: "<h2>" + x[1] + "</h2>", fileRM)
fileRM = re.sub(r"# (.*)", lambda x: "<h1>" + x[1] + "</h1>", fileRM)

fileRM = re.sub(r"> (.*)", lambda x: r"<blockquote>" + x[1] + "</blockquote>", fileRM)
fileRM = re.sub(r"`(.*)`", lambda x: r"<code>" + x[1] + "</code>", fileRM)
fileRM = re.sub(r"---", r"<hr>", fileRM)

#fileRM = re.sub(r"- (.*)",lambda x:"<li>"+x[1]+"</li>", fileRM)

fileRM = re.sub(r"\*\*(.*?)\*\*$", lambda x: "<b>" + str(x[1]) + "</b>", fileRM)
fileRM = re.sub(r"__(.*?)__$", lambda x: "<b>" + str(x[1]) + "</b>", fileRM)
fileRM = re.sub(r"\*(.*?)\*", lambda x: "<i>" + str(x[1]) + "</i>", fileRM)
fileRM = re.sub(r"_(.*?)_", lambda x: "<i>" + str(x[1]) + "</i>", fileRM)
fileRM = re.sub(r"\[(.+?)](\(.*?\))", lambda x: "<a href=" + str('"') + x[2] + '">' + x[1] + '</a>', fileRM)

fileRM = re.sub(r"(1\.) (.+)", lambda x: r"<ol><li>" + x[2] + r"</li>", fileRM)
fileRM = re.sub(r"(\d\.) (.+?)\n([\D|\s])", lambda x: r"<li>" + x[2] + "</li></ol>" + x[3], fileRM)
fileRM = re.sub(r"(\d\.) (.+)", lambda x: r"<li>" + x[2] + "</li>", fileRM)

file2 = open("./readMe.html", "w", encoding="UTF-8")
file2.write(fileRM)
file2.close()
